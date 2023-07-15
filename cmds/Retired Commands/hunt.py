from library.library import *
from library.mobile_object import *
from library.locations import *
from library.stamina_setting import *
from library.character import *
from library.json_db import *
import discord
import time
import datetime

http = urllib3.PoolManager()


class Combat(commands.Cog, description='Combat'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True,
                      brief='input !enhance to enhance your equipment, you also need to prepare Refining Stone.',
                      description='enhance an NFT', aliases=["en"])
    async def enhance(self, ctx, *, equipment_name=" "):
        system_channel = self.bot.get_channel(int(1023204349196906638))
        name = ctx.message.author
        players = open_player_db()
        in_game_items = players[str(name)]["Inventory"]
        on_chain_items = players[str(name)]["NFT Inventory"]

        # added 20221007 not yet done
        args = equipment_name.split()
        new_item_name = ""
        for i in args:
            if i[:7] == "number:":
                number = i[7:]
                try:
                    number = int(number)
                except:
                    number = number
                if type(number) != int:
                    number = 1
                args.remove(i)
            else:
                new_item_name += str(i) + " "
        new_item_name = new_item_name.rstrip(new_item_name[-1])
        if equipment_name in on_chain_items:
            equipment_name = equipment_name
            number = 1

        if "Refining Stone" in in_game_items:
            if in_game_items["Refining Stone"]["number"] > 0:
                if equipment_name in on_chain_items:
                    players[str(name)]["Inventory"]["Refining Stone"]["number"] -= 1
                    save_player_db(players)
                    nft_id = await find_nft_id(str(equipment_name))
                    nfts = open_on_chain_items_db()
                    current_enhancement = nfts[nft_id]["in-game-attributes"]["enhancement"]["value"]
                    current_owner = nfts[nft_id].get("in-game owner")
                    if current_owner == str(name):
                        chance = (0.95 ** current_enhancement) * 100
                        success = random.choices([True, False], weights=(chance, 100 - chance), k=1)[0]
                        if success == True:
                            nfts[nft_id]["in-game-attributes"]["enhancement"]["value"] += 1
                            save_nft_db(nfts)
                            log = "You successfully enhanced " + str(equipment_name)
                        else:
                            log = "You failed to enhance " + str(equipment_name)

                    elif current_owner == None:
                        nfts[nft_id]["in-game owner"] = str(name)
                        players[str(name)]["Inventory"]["Refining Stone"]["number"] += 1
                        save_nft_db(nfts)
                        save_player_db(players)
                        log = "You become the owner of " + str(equipment_name)

                    else:
                        transfer_price = current_enhancement*(current_enhancement+21)/2
                        wallet = players[str(name)].get("Wallet")
                        if wallet >= transfer_price:
                            nfts[nft_id]["in-game owner"] = str(name)
                            players[str(name)]["Wallet"] -= transfer_price
                            players[str(name)]["Inventory"]["Refining Stone"]["number"] += 1
                            for j in players:
                                equipment = players[j]["Equipment"]
                                for k in equipment:
                                    if equipment[k] == str(equipment_name):
                                        equipment[k] = ""
                            save_nft_db(nfts)
                            save_player_db(players)
                            log = "You paid " + str(transfer_price) + " CC to change the ownership of " + str(equipment_name)
                        else:
                            log = str(equipment_name) + "is not belong to you!"
                            log += "you need " + str(transfer_price) + " CC to change the ownership."

                else:
                    log = "You don't have " + str(equipment_name)
            else:
                log = "You don't have Refining Stone!"
        else:
            log = "You don't have Refining Stone!"
        now = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
        await system_channel.send(yaml(str(now) + ": " + str(name) + " enhanced " + str(equipment_name) + "."))
        await ctx.reply(yaml(log))

    @commands.command(pass_context=True,
                      brief='input !equip to add an NFT into equipment list.',
                      description='equip an NFT', aliases=["eq"])
    async def equip(self, ctx, *, equipment_name=" "):
        name = ctx.message.author
        system_channel = self.bot.get_channel(int(1023204349196906638))
        players = open_player_db()

        # search items in inventory
        on_chain_items = players[str(name)]["NFT Inventory"]
        in_game_items = players[str(name)]["Inventory"]
        all_items = {}
        for i in on_chain_items:
            all_items[i] = on_chain_items[i]
        for i in in_game_items:
            all_items[i] = in_game_items[i]

        # update player's equipment db list before equip
        eq_list = ["Weapon", "Shield", "Hat",
                   "Necklace", "Shoulder", "Armor",
                   "Armbands", "Gloves", "Pants",
                   "Shoes", "Belt", "Cloak",
                   "Ring", "Mount", "Herb",
                   "Familiar", "Portrait", "Spirit"]

        for i in eq_list:
            if i not in players[str(name)]["Equipment"]:
                players[str(name)]["Equipment"][i] = ""

        for i in players[str(name)]["Equipment"].copy():
            if i not in eq_list:
                players[str(name)]["Equipment"].pop(i)
            if players[str(name)]["Equipment"].get(str(i)) not in all_items:
                players[str(name)]["Equipment"][i] = ""

        # equip something
        if str(equipment_name) != " ":
            if len(all_items) > 0:
                if str(equipment_name) == "all":
                    await ctx.reply("You randomly equipped NFTs into blank slots.")
                    current_eq = players[str(name)].get("Equipment")
                    for i in current_eq:
                        if current_eq.get(i) != "":
                            eq_list.remove(i)

                    for i in all_items:
                        # determine item type
                        item_type = all_items[i]["item_type"]
                        # equip
                        if str(item_type.capitalize()) in eq_list:
                            if i in on_chain_items:
                                nft_id = await find_nft_id(str(i))
                                nfts = open_on_chain_items_db()
                                current_owner = nfts[nft_id].get("in-game owner")
                                if current_owner == None:
                                    nfts[nft_id]["in-game owner"] = str(name)
                                    if players[str(name)]["Equipment"].get(str(item_type.capitalize())) == "":
                                        players[str(name)]["Equipment"][str(item_type.capitalize())] = str(i)
                                        save_nft_db(nfts)
                                        save_player_db(players)

                                elif current_owner == str(name):
                                    if players[str(name)]["Equipment"].get(str(item_type.capitalize())) == "":
                                        players[str(name)]["Equipment"][str(item_type.capitalize())] = str(i)
                                        save_player_db(players)

                                else:
                                    await ctx.reply(str(i) + " is not owned by you! Please equip it independently.")
                            else:
                                if players[str(name)]["Equipment"].get(str(item_type.capitalize())) == "":
                                    players[str(name)]["Equipment"][str(item_type.capitalize())] = str(i)
                                    save_player_db(players)

                else:
                    if str(equipment_name) in all_items:
                        # determine item type
                        item_type = all_items[str(equipment_name)]["item_type"]
                        # equip
                        if str(item_type.capitalize()) in eq_list:
                            if str(equipment_name) in on_chain_items:
                                nft_id = await find_nft_id(str(equipment_name))
                                nfts = open_on_chain_items_db()
                                current_enhancement = nfts[nft_id]["in-game-attributes"]["enhancement"]["value"]
                                current_owner = nfts[nft_id].get("in-game owner")
                                if current_owner == None:
                                    nfts[nft_id]["in-game owner"] = str(name)
                                    players[str(name)]["Equipment"][str(item_type.capitalize())] = str(equipment_name)
                                    save_player_db(players)
                                    save_nft_db(nfts)

                                elif current_owner == str(name):
                                    players[str(name)]["Equipment"][str(item_type.capitalize())] = str(equipment_name)
                                    save_player_db(players)

                                else:
                                    transfer_price = current_enhancement*(current_enhancement+21)/2
                                    wallet = players[str(name)].get("Wallet")
                                    if wallet >= transfer_price:
                                        players[str(name)]["Wallet"] -= transfer_price
                                        nfts[nft_id]["in-game owner"] = str(name)
                                        players[str(name)]["Equipment"][str(item_type.capitalize())] = str(
                                            equipment_name)
                                        save_player_db(players)
                                        save_nft_db(nfts)
                                        await ctx.reply("You paid " + str(
                                            transfer_price) + " to change the ownership and equip " + str(
                                            equipment_name))
                                    else:
                                        await ctx.reply(
                                            str(equipment_name) + " is not owned by you and you have no money to pay for ownership!")
                            else:
                                players[str(name)]["Equipment"][str(item_type.capitalize())] = str(equipment_name)
                                save_player_db(players)
                                await ctx.reply("You equipped " + str(equipment_name))
                        else:
                            await ctx.reply(str(equipment_name) + " is not an equipment.")
                    else:
                        await ctx.reply("You don't have this NFT in inventory.")
            else:
                await ctx.reply("You have nothing in inventory.")
        else:
            await ctx.reply("If you want to equip NFT, find the nft_name in !inventory, then type !equip nft_name. ")

        log = ""
        for i in players[str(name)]["Equipment"]:
            log += "\n" + str(i) + ": "
            log += players[str(name)]["Equipment"][str(i)]

        embed = discord.Embed(
            title=str(name) + "'s Equipment",
            description=yaml(log)
        )
        now = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
        await system_channel.send(yaml(str(now) + ": " + str(name) + " is checking equipment."))
        await ctx.reply(embed=embed)

    @commands.command(pass_context=True,
                      brief='input !catches to check how many preys you got!',
                      description='check how many preys you got', aliases=["cat"])
    async def catches(self, ctx):
        system_channel = self.bot.get_channel(int(1023204349196906638))
        name = ctx.message.author
        stats = character(name)
        stats.check_account()
        check, message = stats.check_account()

        if check == False:
            await ctx.reply(message)
        else:
            stats.read_account()
            players = open_player_db()
            mobile_objects = open_mobile_object_db()

            if players[str(name)].get("Hunts") == None:
                players[str(name)]["Hunts"] = {}

            preys = players[str(name)]['Hunts']
            monster_name = dict.keys(preys)

            embed1 = discord.Embed()
            log = "Level: " + str(stats.level) + ", Exp: " + str(stats.player_exp) + "/" + str(
                stats.next_exp) + ", Coin: " + str(
                stats.coin) + ' 🪙'
            embed1.add_field(name=str(name) + "'s Status", value=css(log), inline=False)
            log = ""
            number = 1
            column = 1
            for i in monster_name:
                if i in mobile_objects:
                    log += "\n" + str(i) + mobile_objects[str(i)]["icon"] + " (" + str(preys[i]) + ")  "
                else:
                    log += "\n" + str(i) + "❓" + " (" + str(preys[i]) + ")  "
                number += 1
                if number == 20:
                    embed1.add_field(name="Page " + str(column), value=css(log), inline=True)
                    number = 0
                    column += 1
                    log = ""
            if number > 0:
                embed1.add_field(name="Page " + str(column), value=css(log), inline=True)
            now = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
            await system_channel.send(yaml(str(now) + ": " + str(name) + " is checking catches."))
            await ctx.reply(embed=embed1)

    @commands.command(pass_context=True,
                      brief='input !inventory to check what items are in your backpack!',
                      description='check your backpack', aliases=["inv"])
    async def inventory(self, ctx):
        name = ctx.message.author
        system_channel = self.bot.get_channel(int(1023204349196906638))
        players = open_player_db()
        if players[str(name)].get("Inventory") == None:
            players[str(name)]["Inventory"] = {}
        in_game_items = open_in_game_items_db().copy()
        equipment = players[str(name)]["Equipment"]
        equipment_list = []
        for i in equipment:
            if equipment[i] != "":
                equipment_list.append(equipment[i])
        items = players[str(name)]["Inventory"]
        on_chain_items = players[str(name)]["NFT Inventory"]

        equipment_log = ""
        for i in items:
            if i in in_game_items and items[i]["number"] > 0:
                if in_game_items[str(i)].get("function") == "equipment":
                    equipment_log += "\n" + str(i) + in_game_items[str(i)].get("icon") + "(" + str(
                        items[i]["number"]) + ")  "
        if equipment_log == "":
            equipment_log = "Not available"

        consumable_log = ""
        for i in items:
            if i in in_game_items and items[i]["number"] > 0:
                if in_game_items[str(i)].get("function") == "food":
                    consumable_log += "\n" + str(i) + in_game_items[str(i)].get("icon") + "(" + str(
                        items[i]["number"]) + ")  "
        for i in items:
            if i in in_game_items and items[i]["number"] > 0:
                if in_game_items[str(i)].get("function") == "treasure box":
                    consumable_log += "\n" + str(i) + in_game_items[str(i)].get("icon") + "(" + str(
                        items[i]["number"]) + ")  "
        for i in items:
            if i in in_game_items and items[i]["number"] > 0:
                if in_game_items[str(i)].get("function") == "key":
                    consumable_log += "\n" + str(i) + in_game_items[str(i)].get("icon") + "(" + str(
                        items[i]["number"]) + ")  "
        if consumable_log == "":
            consumable_log = "Not available"

        material_log = ""
        for i in items:
            if i in in_game_items and items[i]["number"] > 0:
                if in_game_items[str(i)].get("function") == "craft":
                    material_log += "\n" + str(i) + in_game_items[str(i)].get("icon") + "(" + str(
                        items[i]["number"]) + ")  "
        if material_log == "":
            material_log = "Not available"

        quest_log = ""
        for i in items:
            if i in in_game_items and items[i]["number"] > 0:
                if in_game_items[str(i)].get("function") == "quest":
                    quest_log += "\n" + str(i) + in_game_items[str(i)].get("icon") + "(" + str(
                        items[i]["number"]) + ")  "
        if quest_log == "":
            quest_log = "Not available"

        other_log = ""
        for i in items:
            if i in in_game_items and items[i]["number"] > 0:
                if in_game_items[str(i)].get("function") == "pet":
                    other_log += "\n" + str(i) + in_game_items[str(i)].get("icon") + "(" + str(
                        items[i]["number"]) + ")  "
        for i in items:
            if i not in in_game_items:
                other_log += "\n" + str(i) + "❓" + "(" + str(items[i]["number"]) + ")  "
        if other_log == "":
            other_log = "Not available"

        embed1 = discord.Embed(
            title=str(name) + "'s In-game Items"
        )
        embed1.add_field(name="Equipment", value=css(equipment_log), inline=True)
        embed1.add_field(name="Consumable", value=css(consumable_log), inline=True)
        embed1.add_field(name="Material", value=css(material_log), inline=True)
        embed1.add_field(name="Quest", value=css(quest_log), inline=True)
        embed1.add_field(name="Other", value=css(other_log), inline=True)
        await ctx.reply(embed=embed1)

        embed3 = discord.Embed(
            title=str(name) + "'s On-chain Items"
        )
        log = ""
        number = 1
        column = 1
        for i in on_chain_items:
            if i in equipment_list:
                log += "\n" + str(i) + "(eq.)  "
            else:
                production = False
                for j in on_chain_items[i]:
                    if j != "item_type" and j != "icon":
                        if on_chain_items[i][j].get("type") == "produce_item":
                            production = True
                if production == True:
                    CD = players[str(name)]["Production"] / 720
                    percentage = str(round(CD * 100)) + '%'
                    log += "\n" + str(i) + "(CD {})  ".format(percentage)
                else:
                    log += "\n" + str(i) + "  "
            number += 1
            if number == 20:
                embed3.add_field(name="Page " + str(column), value=css(log), inline=True)
                number = 0
                column += 1
                log = ""
        if number > 0:
            embed3.add_field(name="Page " + str(column), value=css(log), inline=True)

        now = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
        await system_channel.send(yaml(str(now) + ": " + str(name) + " is checking inventory."))
        await ctx.reply(embed=embed3)

    @commands.command(pass_context=True,
                      brief='input !hunt to search for a monster and fight!',
                      description='search a monster and fight', aliases=["hun"])
    async def hunt(self, ctx):
        channel = ctx.channel
        roles = ctx.author.roles
        Adventurer = discord.utils.get(ctx.guild.roles, name="Adventurer")
        if Adventurer in roles:
            name = ctx.message.author
            timestamp = int(time.time())
            players = open_player_db()
            system_channel = self.bot.get_channel(int(1023204349196906638))
            # channel selector
            if players[str(name)].get("Channel") == None:
                channel_to_send = self.bot.get_channel(int(1001435613641318462))
            else:
                channel_to_send = self.bot.get_channel(int(players[str(name)]["Channel"]))

            # check tick
            latest_hunt = players[str(name)].get("Latest Hunt")
            if latest_hunt == None:
                players[str(name)]["Latest Hunt"] = 0
                latest_hunt = 0

            time_pass = timestamp - latest_hunt
            if time_pass <= 3:
                await ctx.reply("You need to wait for " + str(time_pass) + " seconds for next hunting!")
            else:
                players[str(name)]["Latest Hunt"] = timestamp
                save_player_db(players)

                # load and check account
                stats = character(name)
                remind = "Combat log shows up in hunting-ground channel by default! You can enter your favored channel and type !set_channel to setup where to output the combat log."
                stats.read_account()

                # search a monster
                location = players[str(name)]['Location']
                location = locate(str(location))
                mobile_objects = open_mobile_object_db()

                if len(location.monsters) == 0:
                    monster = encounter("Cockroach")
                else:
                    monster = encounter(random.choice(location.monsters))
                if mobile_objects[str(monster.name)].get("portrait") != None:
                    icon = mobile_objects[str(monster.name)].get("portrait")
                else:
                    icon = ""

                log = "You search for monsters....., then you found a " + add_red(str(monster.name)) + "!"

                # fight

                combatlog, won = fight(name, stats, monster)
                log += combatlog
                embed = discord.Embed(
                    title=str(name) + "'s Combat Log",
                    description=remind + css(log)
                )
                embed.set_image(url=icon)
                now = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
                await system_channel.send(yaml(str(now) + ": " + str(name) + " challenged " + str(monster.name)))
                await channel_to_send.send(f"{ctx.message.author.mention}, your combat log is here.", embed=embed)
        else:
            await ctx.reply("You are not yet a Adventurer!")

    @commands.command(pass_context=True,
                      brief='input !attack to challenge a monster in current locality!',
                      description='attack a monster', aliases=["atk", "k"])
    async def attack(self, ctx, *, monster_name):
        roles = ctx.author.roles
        timestamp = int(time.time())
        # make the command case-insensitive
        args = monster_name.split()
        monster_name = ""
        for i in args:
            if i != "of" and i != "on" and i != "at" and i != "the":
                monster_name += i.capitalize() + " "
            else:
                monster_name += i + " "
        monster_name = monster_name.rstrip(monster_name[-1])

        Adventurer = discord.utils.get(ctx.guild.roles, name="Adventurer")
        if Adventurer in roles:
            name = ctx.message.author
            players = open_player_db()
            system_channel = self.bot.get_channel(int(1023204349196906638))
            # channel selector
            if players[str(name)].get("Channel") == None:
                channel_to_send = self.bot.get_channel(int(1001435613641318462))
            else:
                channel_to_send = self.bot.get_channel(int(players[str(name)]["Channel"]))

            # check tick
            latest_hunt = players[str(name)].get("Latest Hunt")
            if latest_hunt == None:
                players[str(name)]["Latest Hunt"] = 0
                latest_hunt = 0

            time_pass = timestamp - latest_hunt
            if time_pass <= 3:
                await ctx.reply("You need to wait for " + str(time_pass) + " seconds for next hunting!")
            else:
                players[str(name)]["Latest Hunt"] = timestamp
                save_player_db(players)


                # load and check account
                stats = character(name)
                stats.read_account()
                remind = "Combat log shows up in hunting-ground channel by default! You can enter your favored channel and type !set_channel to setup where to output the combat log."

                # search a monster
                location = players[str(name)]['Location']
                location = locate(str(location))
                mobile_objects = open_mobile_object_db()

                if monster_name not in location.visible_object:
                    await ctx.reply("There is no such a mobile object here...")
                else:
                    log = "You prepare to fight with " + add_red(str(monster_name)) + "!"
                    monster = encounter(monster_name)
                    if mobile_objects[str(monster.name)].get("portrait") != None:
                        icon = mobile_objects[str(monster.name)].get("portrait")
                    else:
                        icon = ""

                    # fight
                    combatlog, won = fight(name, stats, monster)
                    log += combatlog

                    embed = discord.Embed(
                        title=str(name) + "'s Combat Log",
                        description=remind + css(log)
                    )
                    embed.set_image(url=icon)
                    if won == True:
                        kill_monster(players[str(name)]['Location'], str(monster_name))

                    now = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
                    await system_channel.send(yaml(str(now) + ": " + str(name) + " challenged " + str(monster.name)))
                    await channel_to_send.send(f"{ctx.message.author.mention}, your combat log is here.", embed=embed)

        else:
            await ctx.reply("You are not yet a Adventurer!")

    @commands.command(pass_context=True,
                      brief='input !duel to challenge a player in current locality!',
                      description='challenge a player', aliases=["du"])
    async def duel(self, ctx, *, opponent_name):
        name = ctx.message.author
        players = open_player_db()

        # channel selector
        if players[str(name)].get("Channel") == None:
            channel_to_send = self.bot.get_channel(int(1001435613641318462))
        else:
            channel_to_send = self.bot.get_channel(int(players[str(name)]["Channel"]))

        # check tick
        if players[str(name)].get("Tick") == None:
            players[str(name)]["Tick"] = 0

        if players[str(name)]["Tick"] == 1:
            await ctx.reply("Too many commands in one tick!")
        else:
            players[str(name)]["Tick"] += 1
            with open('./Players.json', 'w', encoding="utf-8") as file:
                json.dump(players, file)

            # check account
            stats = character(name)
            stats.read_account()
            remind = "Hunting log shows up in hunting-ground channel by default! You can !set_channel to modify it."
            await ctx.reply(
                "Hunting log shows up in hunting-ground channel by default! You can !set_channel to modify it.")

            # search a monster
            location1 = players[str(name)]['Location']
            location2 = players[str(opponent_name)]['Location']
            if location1 != location2:
                await ctx.reply("There is no such a person here...")
            else:
                log = "You prepare to fight with " + add_red(str(opponent_name)) + "!"

                # fight
                combatlog, won = duel(name, opponent_name)
                log += combatlog
                await channel_to_send.send(css(log))


def fight(name, stats, monster):
    combatlog = ""
    stamina_cost = 0
    won = False
    players = open_player_db()
    # assign attributes
    stats.check_equipment()
    stats.assign_attribute()

    assist_attack = False
    assist_probability = 0
    assist_dd = 0

    if stats.familiar != "":
        if str(stats.familiar) in players[str(name)]["NFT Inventory"]:
            for i in players[str(name)]["NFT Inventory"][str(stats.familiar)]:
                if type(players[str(name)]["NFT Inventory"][str(stats.familiar)][i]) != str:
                    if players[str(name)]["NFT Inventory"][str(stats.familiar)][i].get("type") == "assist_attack":
                        assist_attack = True
                        assist_probability = players[str(name)]["NFT Inventory"][str(stats.familiar)][i].get(
                            "probability")
                        assist_dd = players[str(name)]["NFT Inventory"][str(stats.familiar)][i].get("value")

        if str(stats.familiar) in players[str(name)]["Inventory"]:
            for i in players[str(name)]["Inventory"][str(stats.familiar)]["in-game-attributes"]:
                if type(players[str(name)]["Inventory"][str(stats.familiar)]["in-game-attributes"][i]) != str:
                    if players[str(name)]["Inventory"][str(stats.familiar)]["in-game-attributes"][i].get(
                            "type") == "assist_attack":
                        assist_attack = True
                        assist_probability = players[str(name)]["Inventory"][str(stats.familiar)]["in-game-attributes"][
                            i].get("probability")
                        assist_dd = players[str(name)]["Inventory"][str(stats.familiar)]["in-game-attributes"][i].get(
                            "value")

    # start combat

    # check the requirement to attack monster
    if players[str(name)]['Life'] > 0:
        if players[str(name)]['Stamina'] >= 200:
            stamina_remain = players[str(name)]['Stamina']
            while True:
                if stamina_remain >= attack_cost:
                    # Player's turn
                    # calculate best attack mode with luck factor
                    bestDD = [max(stats.slash - monster.DEFslash, 0), max(stats.bash - monster.DEFbash, 0),
                              max(stats.pierce - monster.DEFpierce, 0)]
                    luck_adjust = random.randint(int(max(bestDD)), int(max(bestDD)) * 2 + int(stats.luc / 10))
                    damage = luck_adjust + random.randint(1, max(1, int(stats.str / 5)))

                    # calculate attribute impacts
                    quick = random.choices([True, False], weights=(int(stats.dex), 70), k=1)[0]
                    smart = random.choices([True, False], weights=(int(stats.int), 70), k=1)[0]
                    wise = random.choices([True, False], weights=(int(stats.dex), 70), k=1)[0]
                    assist = random.choices([True, False], weights=(
                        int(assist_probability * 100), 100 - int(assist_probability * 100)), k=1)[0]

                    if assist == True:
                        combatlog += ("\n" +
                                      str(stats.familiar) + "  ⚔ ➜ " +
                                      str(monster.name) + " HP: " + str(round(monster.health, 1)) + " ➜" + str(
                                    round(monster.health - assist_dd, 1)))

                        monster.health = monster.health - assist_dd

                    # int effect
                    if smart == True:
                        magic_damage = random.randint(stats.magic + 1, stats.magic * 2 + 2)
                        combatlog += ("\n" +
                                      str(stats.name) + "  🪄️ ➜ " +
                                      str(monster.name) + " HP: " + str(round(monster.health, 1)) + " ➜" + str(
                                    round(monster.health - magic_damage, 1)))

                        monster.health = monster.health - magic_damage

                    # dex effect
                    if quick == True:
                        combatlog += ("\n" +
                                      str(stats.name) + "  ⚔️⚔️ ➜ " +
                                      str(monster.name) + " HP: " + str(round(monster.health, 1)) + " ➜" + str(
                                    round(monster.health - (damage * 2), 1)))
                        monster.health = monster.health - damage - damage
                        stamina_cost += attack_cost

                    else:
                        # wis effect
                        if wise == True:
                            bestDD = stats.slash + stats.bash + stats.pierce
                            luck_adjust = random.randint(max(1, int(bestDD)),
                                                         max(1, int(bestDD * 2 + int(stats.luc / 10))))
                            damage = luck_adjust + random.randint(1, max(1, int(stats.str / 5)))
                            combatlog += ("\n" +
                                          str(stats.name) + " 🧠⚔️ ➜ " +
                                          str(monster.name) + " HP: " + str(round(monster.health, 1)) + " ➜" + str(
                                        round(monster.health - damage, 1)))
                            monster.health = monster.health - damage
                            stamina_cost += attack_cost
                        else:
                            combatlog += ("\n" +
                                          str(stats.name) + "  ⚔️ ➜ " +
                                          str(monster.name) + " HP: " + str(round(monster.health, 1)) + " ➜" + str(
                                        round(monster.health - damage, 1)))
                            monster.health = monster.health - damage
                            stamina_cost += attack_cost

                    if monster.health <= 0:
                        combatlog += ("\n" +
                                      str(monster.name) + " ➜ 💀")
                        # distribute coins and exp
                        stats.coin += monster.coin
                        players = open_player_db()
                        players[str(name)]['Wallet'] += monster.coin
                        players[str(name)]['Exp'] += monster.exp
                        loot = "nothing"
                        loot_type = ""
                        if len(monster.loot) > 0:
                            loot_select = random.choice(monster.loot)
                            in_game_items = open_in_game_items_db().copy()
                            if loot_select != "None":
                                loot = loot_select
                                if players[str(name)]['Inventory'].get(loot) == None:
                                    players[str(name)]['Inventory'][loot] = in_game_items[loot].copy()
                                players[str(name)]['Inventory'][loot]["number"] += 1
                                loot_type = in_game_items[str(loot)]["icon"]
                        if players[str(name)].get("Hunts") == None:
                            players[str(name)]["Hunts"] = {}
                        if players[str(name)]["Hunts"].get(monster.name) == None:
                            players[str(name)]["Hunts"][monster.name] = 0
                        players[str(name)]["Hunts"][monster.name] += 1
                        players[str(name)]['Stamina'] -= round(stamina_cost)
                        players[str(name)]['Stamina'] = round(players[str(name)]['Stamina'], 1)
                        combatlog += ("\n" + str(stats.name) + " lost " + str(
                            stamina_cost) + " stamina. (" + str(
                            players[str(name)]['Stamina']) + " stamina left)")
                        save_player_db(players)

                        combatlog += ("\n" + str(monster.coin) + " 🪙➜ " +
                                      str(stats.name))
                        combatlog += ("\n" + str(monster.exp) + " Exp➜ " +
                                      str(stats.name))
                        combatlog += ("\n" + "You found " + str(loot) + str(loot_type) + " from the corpse.")

                        won = True
                        print(str(stats.name) + " killed " + str(monster.name) + " lost " + str(
                            stamina_cost) + " stamina. (" + str(players[str(name)]['Stamina']) + " stamina left)")
                        return combatlog, won
                else:
                    combatlog += ("\n" + str(stats.name) + " requires additional 20 stamina to perform attack...")

                # Monster's turn
                # dex effect
                quick = random.choices([True, False], weights=(int(stats.dex), 70), k=1)[0]
                charming = random.choices([True, False], weights=(int(stats.cha), 70), k=1)[0]

                if quick == True:
                    combatlog += ("\n" +
                                  str(monster.name) + "  ⚔️ ➜ " + str(stats.name) + " 👟")
                    stamina_cost += evasion_cost
                else:
                    counter = max(1, random.randint(monster.attack,
                                                    max(1, int(monster.attack * 2 - int(
                                                        stats.luc / 10)))) - stats.defense - random.randint(
                        1, max(1, int(stats.con / 5))))
                    # cha effect
                    if charming == True:
                        combatlog += ("\n" +
                                      str(monster.name) + " ❓⚔️ ➜ " +
                                      str(monster.name) + " HP: " + str(round(monster.health, 1)) + " ➜" + str(
                                    round(monster.health - counter, 1))
                                      )
                        monster.health = monster.health - counter
                        stamina_cost += evasion_cost
                        if monster.health <= 0:
                            combatlog += ("\n" +
                                          str(monster.name) + " ➜ 💀")
                            # distribute coins and exp
                            stats.coin += monster.coin
                            players = open_player_db()
                            players[str(name)]['Wallet'] += monster.coin
                            players[str(name)]['Exp'] += monster.exp
                            loot = "nothing"
                            loot_type = ""
                            if len(monster.loot) > 0:
                                loot_select = random.choice(monster.loot)
                                in_game_items = open_in_game_items_db().copy()
                                if loot_select != "None":
                                    loot = loot_select
                                    if players[str(name)]['Inventory'].get(loot) == None:
                                        players[str(name)]['Inventory'][loot] = in_game_items[loot].copy()
                                    players[str(name)]['Inventory'][loot]["number"] += 1
                                    loot_type = in_game_items[str(loot)]["icon"]
                            if players[str(name)].get("Hunts") == None:
                                players[str(name)]["Hunts"] = {}
                            if players[str(name)]["Hunts"].get(monster.name) == None:
                                players[str(name)]["Hunts"][monster.name] = 0
                            players[str(name)]["Hunts"][monster.name] += 1
                            players[str(name)]['Stamina'] -= round(stamina_cost)
                            players[str(name)]['Stamina'] = round(players[str(name)]['Stamina'], 1)
                            combatlog += ("\n" + str(stats.name) + " lost " + str(
                                stamina_cost) + " stamina. (" + str(
                                players[str(name)]['Stamina']) + " stamina left)")
                            save_player_db(players)

                            combatlog += ("\n" + str(monster.coin) + " 🪙➜ " +
                                          str(stats.name))
                            combatlog += ("\n" + str(monster.exp) + " Exp➜ " +
                                          str(stats.name))
                            combatlog += ("\n" + "You found " + str(loot) + str(loot_type) + " from the corpse.")

                            won = True
                            print(str(stats.name) + " killed " + str(monster.name) + " lost " + str(
                                stamina_cost) + " stamina. (" + str(players[str(name)]['Stamina']) + " stamina left)")
                            return combatlog, won
                    else:
                        combatlog += ("\n" +
                                      str(monster.name) + "  ⚔️ ➜ " +
                                      str(stats.name) + " HP: " + str(round(stats.health, 1)) + " ➜" + str(
                                    round(stats.health - counter, 1))
                                      )
                        stats.health = stats.health - counter
                        stamina_cost += hit_cost

                        # response after hit by monster
                        if stats.health <= 0:
                            if stamina_remain >= (escape_cost + stamina_cost):
                                combatlog += ("\n" + str(stats.name) + " ➜ 👟👟")
                                stamina_cost += escape_cost
                                break

                            else:
                                players[str(name)]['Life'] -= 1
                                players[str(name)]['Life_count'] = 0
                                combatlog += ("\n" + str(stats.name) + " ➜ 💀")
                                print(str(stats.name) + " is killed by " + str(monster.name) + " and lost " + str(
                                    stamina_cost) + " stamina.")
                                break

            players[str(name)]['Stamina'] -= stamina_cost
            players[str(name)]['Stamina'] = round(players[str(name)]['Stamina'], 1)
            if players[str(name)]['Stamina'] < 0:
                players[str(name)]['Stamina'] = 0

            save_player_db(players)

            combatlog += ("\n" + str(stats.name) + " lost " + str(
                stamina_cost) + " stamina. (" + str(players[str(name)]['Stamina']) + " stamina left)")

            return combatlog, won

        else:
            combatlog = "\n" + "For your safety, you need to keep at least 200 stamina for hunting..."
            return combatlog, won

    else:
        life_count = 180 - players[str(name)]['Life_count']
        combatlog = "\n" + "You lay on the ground and dreamed about your adventure... hopefully the goddess of Chiania can revive you. You start to pray, [you hear a voice]: " + str(
            life_count) + ' minutes left...'
        return combatlog, won


def duel(player1, player2):
    stats1 = character(player1)
    stats1.read_account()
    stats1.check_equipment()
    stats2 = character(player2)
    stats2.read_account()
    stats2.check_equipment()
    combatlog = ""
    stamina_cost = 0
    won = False
    players = open_player_db()
    # assign attributes
    stats1.assign_attribute()
    stats2.assign_attribute()

    # start combat
    combatlog += ("\n" + "Combat Log between " + str(stats1.name) + " and " + str(stats2.name))

    print(str(stats1.name) + " challenged " + str(stats2.name))

    # check the requirement to attack monster
    if players[str(stats1.name)]['Life'] > 0 and players[str(stats2.name)]['Life'] > 0:
        if players[str(stats1.name)]['Stamina'] >= 200 and players[str(stats2.name)]['Stamina'] >= 200:
            stamina1_remain = players[str(stats1.name)]['Stamina']
            stamina2_remain = players[str(stats2.name)]['Stamina']
            while True:
                if stamina1_remain >= attack_cost:
                    # Player1's turn
                    # calculate best attack mode with luck factor
                    bestDD = max(stats1.slash, stats1.bash, stats1.pierce, 0)
                    luck_adjust = random.randint(bestDD, bestDD * 2 + int(stats1.luc / 10))
                    damage = luck_adjust + random.randint(1, int(stats1.str / 5))

                    # calculate attribute impacts (attacker)
                    quick = random.choices([True, False], weights=(int(stats1.dex), 70), k=1)[0]
                    smart = random.choices([True, False], weights=(int(stats1.int), 70), k=1)[0]
                    wise = random.choices([True, False], weights=(int(stats1.dex), 70), k=1)[0]

                    # defender
                    evasion = random.choices([True, False], weights=(int(stats2.dex), 70), k=1)[0]
                    charming = random.choices([True, False], weights=(int(stats2.cha), 70), k=1)[0]

                    if evasion == True:
                        combatlog += ("\n" +
                                      str(stats1.name) + "  ⚔️ ➜ " + str(stats2.name) + " 👟")
                        stamina_cost += evasion_cost
                    else:
                        if charming == True:
                            combatlog += ("\n" +
                                          str(stats1.name) + " ❓⚔️ ➜ " +
                                          str(stats1.name) + " HP: " + str(stats1.health) + " ➜" + str(
                                        stats1.health - damage)
                                          )
                            stats1.health = stats1.health - damage
                            stamina_cost += evasion_cost
                        else:
                            # int effect
                            if smart == True:
                                magic_damage = random.randint(stats1.magic + 1, stats1.magic * 2 + 2)
                                combatlog += ("\n" +
                                              str(stats1.name) + "  🪄️ ➜ " +
                                              str(stats2.name) + " HP: " + str(stats2.health) + " ➜" + str(
                                            stats2.health - magic_damage))

                                stats2.health = stats2.health - magic_damage

                            # dex effect
                            if quick == True:
                                # wis effect
                                if wise == True:
                                    combatlog += ("\n" +
                                                  str(stats1.name) + "  ⚔️ ➜ " +
                                                  str(stats2.name) + " HP: " + str(stats2.health) + " ➜" + str(
                                                stats2.health - damage))
                                    stats2.health = stats2.health - damage
                                    stamina_cost += attack_cost
                                else:
                                    bestDD = stats1.slash + stats1.bash + stats1.pierce
                                    luck_adjust = random.randint(bestDD, bestDD * 2 + int(stats1.luc / 10))
                                    damage = luck_adjust + random.randint(1, int(stats1.str / 5))
                                    combatlog += ("\n" +
                                                  str(stats1.name) + " 🧠⚔️ ➜ " +
                                                  str(stats2.name) + " HP: " + str(stats2.health) + " ➜" + str(
                                                stats2.health - damage))
                                    stats2.health = stats2.health - damage
                                    stamina_cost += attack_cost
                            else:
                                combatlog += ("\n" +
                                              str(stats1.name) + "  ⚔️⚔️ ➜ " +
                                              str(stats2.name) + " HP: " + str(stats2.health) + " ➜" + str(
                                            stats2.health - (damage * 2)))
                                stats2.health = stats2.health - damage - damage
                                stamina_cost += attack_cost

                            if stats2.health <= 0:
                                combatlog += ("\n" +
                                              str(stats2.name) + " ➜ 💀")
                                # distribute coins and exp
                                stats1.coin += 0
                                with open('./Players.json', 'r', encoding="utf-8") as file:
                                    players = json.load(file)
                                    file.close()
                                players[str(stats1.name)]['Wallet'] += 0
                                players[str(stats1.name)]['Exp'] += 0
                                players[str(stats1.name)]['Stamina'] -= 0
                                combatlog += ("\n" + str(stats1.name) + " lost " + "0" + " stamina. (" + str(
                                    players[str(stats1.name)]['Stamina']) + " stamina left)")

                                combatlog += ("\n" + "0" + " 🪙➜ " +
                                              str(stats1.name))
                                combatlog += ("\n" + "0" + " Exp➜ " +
                                              str(stats1.name))

                                won = True
                                print(str(stats1.name) + " killed " + str(
                                    stats2.name) + " lost " + "0" + " stamina. (" + str(
                                    players[str(stats1.name)]['Stamina']) + " stamina left)")
                                return combatlog, won

                else:
                    combatlog += ("\n" + str(stats1.name) + " requires additional 20 stamina to perform attack...")

                # Player2's turn
                if stamina2_remain >= attack_cost:
                    # Player1's turn
                    # calculate best attack mode with luck factor
                    bestDD = max(stats2.slash, stats2.bash, stats2.pierce, 0)
                    luck_adjust = random.randint(bestDD, bestDD * 2 + int(stats2.luc / 10))
                    damage = luck_adjust + random.randint(1, int(stats2.str / 5))

                    # calculate attribute impacts
                    quick = random.choices([True, False], weights=(int(stats2.dex), 70), k=1)[0]
                    smart = random.choices([True, False], weights=(int(stats2.int), 70), k=1)[0]
                    wise = random.choices([True, False], weights=(int(stats2.dex), 70), k=1)[0]

                    # defender
                    evasion = random.choices([True, False], weights=(int(stats1.dex), 70), k=1)[0]
                    charming = random.choices([True, False], weights=(int(stats1.cha), 70), k=1)[0]

                    if evasion == True:
                        combatlog += ("\n" +
                                      str(stats2.name) + "  ⚔️ ➜ " + str(stats1.name) + " 👟")
                        stamina_cost += evasion_cost
                    else:
                        if charming == True:
                            combatlog += ("\n" +
                                          str(stats2.name) + " ❓⚔️ ➜ " +
                                          str(stats2.name) + " HP: " + str(stats2.health) + " ➜" + str(
                                        stats2.health - damage)
                                          )
                            stats2.health = stats2.health - damage
                            stamina_cost += evasion_cost
                        else:
                            # int effect
                            if smart == True:
                                magic_damage = random.randint(stats2.magic + 1, stats2.magic * 2 + 2)
                                combatlog += ("\n" +
                                              str(stats2.name) + "  🪄️ ➜ " +
                                              str(stats1.name) + " HP: " + str(stats1.health) + " ➜" + str(
                                            stats1.health - magic_damage))

                                stats1.health = stats1.health - magic_damage

                            # dex effect
                            if quick == True:
                                # wis effect
                                if wise == True:
                                    combatlog += ("\n" +
                                                  str(stats2.name) + "  ⚔️ ➜ " +
                                                  str(stats1.name) + " HP: " + str(stats1.health) + " ➜" + str(
                                                stats1.health - damage))
                                    stats1.health = stats1.health - damage
                                    stamina_cost += attack_cost
                                else:
                                    bestDD = stats2.slash + stats2.bash + stats2.pierce
                                    luck_adjust = random.randint(bestDD, bestDD * 2 + int(stats2.luc / 10))
                                    damage = luck_adjust + random.randint(1, int(stats2.str / 5))
                                    combatlog += ("\n" +
                                                  str(stats2.name) + " 🧠⚔️ ➜ " +
                                                  str(stats1.name) + " HP: " + str(stats1.health) + " ➜" + str(
                                                stats1.health - damage))
                                    stats1.health = stats1.health - damage
                                    stamina_cost += attack_cost
                            else:
                                combatlog += ("\n" +
                                              str(stats2.name) + "  ⚔️⚔️ ➜ " +
                                              str(stats1.name) + " HP: " + str(stats1.health) + " ➜" + str(
                                            stats1.health - (damage * 2)))
                                stats1.health = stats1.health - damage - damage
                                stamina_cost += attack_cost

                            if stats1.health <= 0:
                                combatlog += ("\n" +
                                              str(stats1.name) + " ➜ 💀")
                                # distribute coins and exp
                                stats2.coin += 0
                                players = open_player_db()
                                players[str(stats2.name)]['Wallet'] += 0
                                players[str(stats2.name)]['Exp'] += 0
                                players[str(stats2.name)]['Stamina'] -= 0
                                combatlog += ("\n" + str(stats2.name) + " lost " + "0" + " stamina. (" + str(
                                    players[str(stats2.name)]['Stamina']) + " stamina left)")
                                # with open('./Players.json', 'w') as file:
                                #    json.dump(players, file)

                                combatlog += ("\n" + "0" + " 🪙➜ " +
                                              str(stats2.name))
                                combatlog += ("\n" + "0" + " Exp➜ " +
                                              str(stats2.name))

                                won = True
                                print(str(stats2.name) + " killed " + str(
                                    stats1.name) + " lost " + "0" + " stamina. (" + str(
                                    players[str(stats2.name)]['Stamina']) + " stamina left)")
                                return combatlog, won

                else:
                    combatlog += ("\n" + str(stats2.name) + " requires additional 20 stamina to perform attack...")

        else:
            combatlog = "\n" + "You are too tired to hunt..."
            return combatlog, won

    else:
        life_count1 = 180 - players[str(stats1.name)]['Life_count']
        life_count2 = 180 - players[str(stats2.name)]['Life_count']
        combatlog = "\n" + "You dreamed about your dual with " + str(stats2.name)
        return combatlog, won


def yaml(log):
    output = "\n" + "```yaml" + "\n" + log + "```"
    return output


def css(log):
    output = "\n" + "```css" + "\n" + log + "```"
    return output


def add_red(text):
    text = "[" + text + "]"
    return text


async def find_nft_id(item_name):
    nfts = open_on_chain_items_db()
    nft_id = None
    for i in nfts:
        if nfts[i]["item_name"] == str(item_name):
            if nfts[i].get("burned") == None:
                url = 'https://api.mintgarden.io/nfts/' + str(i)
                response = http.request('GET', url)
                nft = BeautifulSoup(response.data, features="html.parser")
                nft = json.loads(nft.text)
                owner = nft["owner_address"].get("encoded_id")
                if owner == "xch1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqm6ks6e8mvy" or owner == "xch1x0lmv0hv4cafhdanj49n0ugjm9crhuzte8m8r8cxus5haw64dhws6da2cf":
                    nfts[i]["burned"] = True
                else:
                    nfts[i]["burned"] = False
                save_nft_db(nfts)

            if nfts[i].get("burned") == False:
                nft_id = str(i)

    return nft_id


async def setup(bot):
    await bot.add_cog(Combat(bot))
