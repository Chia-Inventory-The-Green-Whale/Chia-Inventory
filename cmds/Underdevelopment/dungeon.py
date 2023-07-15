from discord.ext import commands
from library.locations import *
from library.stamina_setting import *
import time
import datetime
from library.json_db import *
from library.room_creator import *
from cmds.hunt import fight
from library.character import *
import discord
import urllib3
from bs4 import BeautifulSoup
from library.mobile_object import encounter
from cmds.hunt import find_nft_id

http = urllib3.PoolManager()


class Dungeon(commands.Cog, description='Commands related to dungeon'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True,
                      brief='input !investigate to obtain more information a structure!',
                      description='investigate a structure', aliases=["smell", "listen", "inves"])
    async def investigate(self, ctx, *, construction_name):
        player_name = ctx.message.author
        players = open_player_db()
        locations = open_locations_db()
        dungeons = open_dungeons_db()
        location = players[str(player_name)]['Location']
        location = locate(str(location))
        area_type = str(location.area_type)
        if construction_name in location.construction:
            if area_type == "Dungeon":
                investigate_status = location.construction[construction_name].get("investigate")
                if investigate_status == False or investigate_status == None:
                    log = "You investigated " + str(construction_name)
                    locations[location.id]["constructions"][construction_name]["investigate"] = True
                    save_location_db(locations)
                    listen = location.construction[construction_name].get("listen")
                    if listen == None:
                        listen = ""
                    smell = location.construction[construction_name].get("smell")
                    if smell == None:
                        smell = ""

                    information = listen + smell
                    if information != "":
                        stats = character(player_name)
                        stats.read_account()
                        stats.check_equipment()
                        stats.assign_attribute()
                        ability_check = random.choice(location.construction[construction_name].get("ability check"))
                        difficulty = location.construction[construction_name].get("difficulty")
                        success = False
                        if ability_check == "int":
                            dice = random.randint(1, int(stats.int))
                            if dice >= difficulty:
                                success = True
                        if ability_check == "wis":
                            dice = random.randint(1, int(stats.wis))
                            if dice >= difficulty:
                                success = True
                        if ability_check == "luc":
                            dice = random.randint(1, int(stats.luc))
                            if dice >= difficulty:
                                success = True
                        log += "\n" + "🎲" + ability_check + " = " + str(dice) + ", target = " + str(difficulty)
                        if success == True:
                            log += " Success! "
                            log += "\n" + information
                        else:
                            log += " Failed! "

                        embed = discord.Embed(
                            description=yaml(log)
                        )
                        await ctx.reply(embed=embed)
                    else:
                        await ctx.reply("There is nothing interesting about this structure...")
                else:
                    await ctx.reply("You already investigated this structure!")
            else:
                await ctx.reply("There is no need to investigate this structure.")
        else:
            await ctx.reply("There is no such a thing!")

    @commands.command(pass_context=True,
                      brief='input !explore to explore a dungeon!',
                      description='explore a construction', aliases=["exp"])
    async def explore(self, ctx):
        player_name = ctx.message.author
        players = open_player_db()
        locations = open_locations_db()
        mobile_objects = open_mobile_object_db()
        with open('./library/dungeons.json', 'r') as file:
            dungeons = json.load(file)
            file.close()
        location = players[str(player_name)]['Location']
        location = locate(str(location))
        if location.area_type == "Dungeon":
            dungeon_length = locations[str(location.id)]["dungeon_length"]
            dungeon_exit = dungeons[str(location.name)]["exit"]
            if dungeon_length > 0:
                stats = character(player_name)
                stats.read_account()
                stats.check_equipment()
                stats.assign_attribute()
                explore_log, combatlog, monster_name = await explore_dungeon(player_name, stats, location)

                if combatlog != None:
                    combatlog = "\n" + "👿 You encountered a " + str(monster_name) + "!" + "\n" + combatlog
                    if mobile_objects[monster_name].get("portrait") != None:
                        icon = mobile_objects[monster_name].get("portrait")
                    else:
                        icon = ""
                    embed = discord.Embed(
                        title=str(player_name) + "'s Combat Log",
                        description=css(combatlog)
                    )
                    embed.set_image(url=icon)
                    await ctx.reply(embed=embed)

                log, icon, location_name, constructions, exits, mobs, target_type, items = await look(str(player_name),
                                                                                                      None)

                embed = discord.Embed(
                    title="🏰" + str(location_name),
                    description="Events" + yaml(explore_log) + "Location" + log
                )
                embed.set_image(url=icon)
                if mobs != "":
                    embed.add_field(name="Monsters & NPC", value=yaml(mobs), inline=False)
                if items != "":
                    embed.add_field(name="Items", value=yaml(items), inline=True)
                if constructions != "":
                    embed.add_field(name="Structures", value=yaml(constructions), inline=True)
                if exits != "":
                    embed.add_field(name="Exits", value=yaml(exits), inline=True)
                hint = ""
                if target_type == "Location":
                    hint += "Hint: Please input !go <direction> or !go <structure name> to move location, or input !k <monster name> for hunting."
                    # hint += "請輸入 !go <方向> 或 !go <建築物名稱> 進行移動。輸入 !k <怪物名稱> 進行狩獵。"
                await ctx.reply(hint, embed=embed)
            else:
                players[str(player_name)]['Location'] = dungeon_exit
                locations.pop(str(location.id))
                await save_player_db(players)
                log = "You finished exploration and found a way to leave this dungeon!"
                embed = discord.Embed(
                    title=log
                )
                await ctx.reply(embed=embed)
        else:
            log = "You are not in a dungeon, and there is nothing to explore here!"
            embed = discord.Embed(
                description=log
            )
            await ctx.reply(embed=embed)


def create_dungeon(dungeon_name, dungeon_type):
    locations = open_locations_db()
    with open('./library/dungeons.json', 'r') as file:
        dungeons = json.load(file)
        file.close()
    length = dungeons[str(dungeon_type)]["length"]
    icon = random.choice(dungeons[str(dungeon_type)]["icon"])
    exit = random.choice(dungeons[str(dungeon_type)]["paths"])
    boss = dungeons[str(dungeon_type)]["monsters"]["boss"]
    if dungeon_name not in locations:
        locations[dungeon_name] = {}
        locations[dungeon_name]["dungeon_length"] = length
        locations[dungeon_name]["icon"] = icon
        locations[dungeon_name]["boss"] = boss
    else:
        locations[dungeon_name]["icon"] = ""
        locations[dungeon_name]["dungeon_length"] -= 1

    locations[dungeon_name]["area_type"] = "Dungeon"
    locations[dungeon_name]["climate"] = None
    locations[dungeon_name]["movement_type"] = None
    locations[dungeon_name]["exit"] = exit
    locations[dungeon_name]["climate"] = None
    locations[dungeon_name]["monsters"] = []
    locations[dungeon_name]["monster_population"] = 3
    locations[dungeon_name]["ground"] = []
    locations[dungeon_name]["constructions"] = {}
    locations[dungeon_name]["east"] = str(dungeon_name)
    locations[dungeon_name]["west"] = str(dungeon_name)
    locations[dungeon_name]["south"] = str(dungeon_name)
    locations[dungeon_name]["north"] = str(dungeon_name)
    locations[dungeon_name]["up"] = str(dungeon_name)
    locations[dungeon_name]["down"] = str(dungeon_name)
    locations[dungeon_name]["description"] = "You are inside " + str(dungeon_type)
    locations[dungeon_name]["visible_object"] = []
    locations[dungeon_name]["name"] = str(dungeon_type)
    locations[dungeon_name]["explore"] = False

    save_location_db(locations)


async def explore_dungeon(player_name, stats, location):  # this is an object
    with open('./library/dungeons.json', 'r') as file:
        dungeons = json.load(file)
        file.close()
    players = open_player_db()
    locations = open_locations_db()
    explore = locations[str(location.id)].get("explore")
    combatlog = None
    monster_name = None
    if explore != True:
        # monster controller
        number_min = dungeons[str(location.name)]["monsters"]["number_min"]
        number_max = dungeons[str(location.name)]["monsters"]["number_max"]
        monster_number = random.randint(number_min, number_max)
        monster_pool = dungeons[str(location.name)]["monsters"]["type"]
        boss = None
        if type(locations[str(location.id)].get("boss")) == list:
            if len(locations[str(location.id)].get("boss")) > 0:
                boss = random.choice(locations[str(location.id)]["boss"])
        locations[str(location.id)]["visible_object"] = []
        for i in range(monster_number):
            monster = random.choice(monster_pool)
            locations[str(location.id)]["visible_object"].append(monster)
        if boss != None:
            locations[str(location.id)]["visible_object"].append(boss)
            locations[str(location.id)]["boss"].remove(boss)

        # ground item controller
        item_pool = dungeons[str(location.name)].get("ground")
        if type(item_pool) == list and len(item_pool) > 0:
            item = random.choice(item_pool)
            if item != "None":
                locations[str(location.id)]["ground"].append(item)

        # constructions controller
        number_min = dungeons[str(location.name)]["constructions"]["number_min"]
        number_max = dungeons[str(location.name)]["constructions"]["number_max"]
        construction_number = random.randint(number_min, number_max)
        construction_pool = dungeons[str(location.name)]["constructions"].get("type")
        if type(construction_pool) == dict:
            construction_pool = list(dungeons[str(location.name)]["constructions"]["type"].keys())
            for i in range(construction_number):
                if len(construction_pool) > 0:
                    construction = random.choice(construction_pool)
                    locations[str(location.id)]["constructions"][construction] = \
                        dungeons[str(location.name)]["constructions"]["type"].get(construction)
                    construction_pool.remove(construction)

        # event handle
        events = list(dungeons[str(location.name)]["events"].keys())
        event = random.choice(events)
        ability_check = random.choice(dungeons[str(location.name)]["events"][event].get("ability check"))
        difficulty = dungeons[str(location.name)]["events"][event].get("difficulty")
        event_type = dungeons[str(location.name)]["events"][event].get("type")
        success_message = dungeons[str(location.name)]["events"][event].get("success_message")
        success = False
        if ability_check == "str":
            dice = random.randint(1, int(stats.str))
            if dice >= difficulty:
                success = True
        elif ability_check == "con":
            dice = random.randint(1, int(stats.con))
            if dice >= difficulty:
                success = True
        elif ability_check == "dex":
            dice = random.randint(1, int(stats.dex))
            if dice >= difficulty:
                success = True
        elif ability_check == "int":
            dice = random.randint(1, int(stats.int))
            if dice >= difficulty:
                success = True
        elif ability_check == "wis":
            dice = random.randint(1, int(stats.wis))
            if dice >= difficulty:
                success = True
        elif ability_check == "cha":
            dice = random.randint(1, int(stats.cha))
            if dice >= difficulty:
                success = True
        elif ability_check == "luc":
            dice = random.randint(1, int(stats.luc))
            if dice >= difficulty:
                success = True
        event_log = "❗" + event
        if success == True:
            event_log += " " + success_message
            event_log += "\n" + "🎲" + ability_check + " = " + str(dice) + ", target = " + str(difficulty)
            event_log += " Success! "
        else:
            event_log += " "
            event_log += "\n" + "🎲" + ability_check + " = " + str(dice) + ", target = " + str(difficulty)
            event_log += " Failed! "

            # negative impacts
            if event_type == "encounter_monster":
                encounter_monsters = dungeons[str(location.name)]["events"][event].get("encounter")
                monster_name = random.choice(encounter_monsters)
                monster = encounter(monster_name)
                combatlog, won = fight(player_name, stats, monster)
                players = open_player_db()
        treasure_box = random.choice(dungeons[str(location.name)]["treasure_box"])

        # renew the room
        path = random.choice(dungeons[str(location.name)]["paths"])
        icon = random.choice(dungeons[str(location.name)]["icon"])
        explore_log = "🔎 You explored this location....."

        locations[str(location.id)]["exit"] = path
        locations[str(location.id)]["icon"] = icon
        locations[str(location.id)]["explore"] = True
        explore_log += "\n" + str(event_log)
        for i in locations[str(location.id)]["constructions"]:
            explore_log += "\n" + "👣 You found a path behind " + str(i)
        explore_log += "\n" + "👣 You found a hidden path behind " + str(path)
        save_location_db(locations)
        await save_player_db(players)
    else:
        explore_log = "You already explored this area....."
    return explore_log, combatlog, monster_name


def yaml(log):
    output = "\n" + "```yaml" + "\n" + log + "```"
    return output


def apache(log):
    output = "\n" + "```apache" + "\n" + log + "```"
    return output


def css(log):
    output = "\n" + "```css" + "\n" + log + "```"
    return output


async def setup(bot):
    await bot.add_cog(Dungeon(bot))
