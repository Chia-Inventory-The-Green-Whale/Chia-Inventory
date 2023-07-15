from discord.ext import commands
import random
from library.json_db import *
import discord


class Developer(commands.Cog, description='These are developer tools for Chia Inventory.'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief='input !give <player name> <item name> to send an item',
                      description='send an item')
    async def give(self, ctx, player_name, *, item_name):
        name = ctx.message.author
        if str(name) == "Chia Inventory#9520":
            players = open_player_db()
            if str(player_name) in players:
                in_game_items = open_in_game_items_db()
                if str(item_name) in in_game_items:
                    item_to_send = in_game_items.get(str(item_name))
                    if str(item_name) not in players[str(player_name)]['Inventory']:
                        players[str(player_name)]['Inventory'][str(item_name)] = item_to_send
                    players[str(player_name)]['Inventory'][str(item_name)]["number"] += 1
                    await save_player_db(players)
                    await ctx.send("You sent " + str(item_name) + " to " + str(player_name))
                else:
                    await ctx.send("There is no such an item...")
            else:
                await ctx.send("There is not such a person...")
        else:
            await ctx.send("You don't know this spell...")

    @commands.command(pass_context=True, brief='input !change_description description to modify a room',
                      description='modify a room description')
    async def change_description(self, ctx, *, description):
        name = ctx.message.author
        if str(name) == "Chia Inventory#9520" or str(name) == "Da8erRul85#2286" or str(name) == "OddLogic#2415":
            locations = open_locations_db()
            players = open_player_db()
            location_name = players[str(name)]['Location']
            locations[location_name]["description"] = description
            save_location_db(locations)
            await ctx.send("You changed the description of " + str(location_name) + " into: " + str(description))

        else:
            await ctx.send("You don't know this spell...")

    @commands.command(pass_context=True, brief='input !excavate direction to create a room',
                      description='create a room')
    async def excavate(self, ctx, direction):
        name = ctx.message.author
        roles = ctx.author.roles
        Architect = discord.utils.get(ctx.guild.roles, name="Architect")
        if Architect in roles:
            if str(direction) in ["east", "west", "south", "north", "e", "w", "s", "n"]:
                new_room = str(random.getrandbits(32))
                await add_room(new_room)
                players = open_player_db()
                locations = open_locations_db()
                here = players[str(name)].get("Location")
                if direction in ["east", "e"]:
                    locations[here]["east"] = new_room
                    locations[new_room]["west"] = here
                if direction in ["west", "w"]:
                    locations[here]["west"] = new_room
                    locations[new_room]["east"] = here
                if direction in ["south", "s"]:
                    locations[here]["south"] = new_room
                    locations[new_room]["north"] = here
                if direction in ["north", "n"]:
                    locations[here]["north"] = new_room
                    locations[new_room]["south"] = here
                save_location_db(locations)
                await ctx.send("You excavated " + str(new_room) + " to the direction " + str(direction))
            else:
                await ctx.send("Please input direction correctly...")
        else:
            await ctx.send("You don't have permission to cast this spell...")

    @commands.command(pass_context=True, brief='input !change_name room_name to modify a room',
                      description='modify a room name')
    async def change_name(self, ctx, *, room_name):
        name = ctx.message.author
        roles = ctx.author.roles
        Architect = discord.utils.get(ctx.guild.roles, name="Architect")
        if Architect in roles:
            locations = open_locations_db()
            players = open_player_db()
            location_name = players[str(name)].get('Location')
            locations[location_name]["name"] = room_name
            save_location_db(locations)
            await ctx.send("You changed the name of " + str(location_name) + " into: " + str(room_name))

        else:
            await ctx.send("You don't have permission to cast this spell...")

    @commands.command(pass_context=True, brief='input !close_door to close doors',
                      description='close door')
    async def close_door(self, ctx):
        name = ctx.message.author
        roles = ctx.author.roles
        Architect = discord.utils.get(ctx.guild.roles, name="Architect")
        if Architect in roles:
            locations = open_locations_db()
            players = open_player_db()
            location_name = players[str(name)]['Location']
            locations[location_name]["east"] = location_name
            locations[location_name]["west"] = location_name
            locations[location_name]["south"] = location_name
            locations[location_name]["north"] = location_name
            save_location_db(locations)
            await ctx.send("You closed unused openings of this room...")
        else:
            await ctx.send("You don't have permission to cast this spell...")

    @commands.command(pass_context=True, brief='input !change_type area_type to modify a room',
                      description='modify a room name')
    async def change_type(self, ctx, *, area_type):
        name = ctx.message.author
        roles = ctx.author.roles
        Architect = discord.utils.get(ctx.guild.roles, name="Architect")
        if Architect in roles:
            locations = open_locations_db()
            players = open_player_db()
            location_name = players[str(name)]['Location']
            locations[location_name]["area_type"] = area_type
            save_location_db(locations)
            await ctx.send("You changed the area type of " + str(location_name) + " into: " + str(area_type))

        else:
            await ctx.send("You don't have permission to cast this spell...")

    @commands.command(pass_context=True, brief='input !add_monster monster_name to modify a room',
                      description='add monster')
    async def add_monster(self, ctx, *, monster_name):
        name = ctx.message.author
        roles = ctx.author.roles
        Architect = discord.utils.get(ctx.guild.roles, name="Architect")
        if Architect in roles:
            locations = open_locations_db()
            players = open_player_db()
            mobile_objects = open_mobile_object_db()
            location_name = players[str(name)]['Location']
            if str(monster_name) in mobile_objects:
                type = mobile_objects[str(monster_name)].get("type")
                if type == "monster":
                    locations[location_name]["monsters"].append(str(monster_name))
                    save_location_db(locations)
                    await ctx.send("You summon " + str(monster_name) + " to " + str(location_name))
                else:
                    await ctx.send(str(monster_name) + " is not monster.")
            else:
                await ctx.send("There is no such a mob in Chiania.")

        else:
            await ctx.send("You don't have permission to cast this spell...")

    @commands.command(pass_context=True, brief='input !add_npc npc_name to modify a room',
                      description='add npc')
    async def add_npc(self, ctx, *, npc_name):
        name = ctx.message.author
        roles = ctx.author.roles
        Architect = discord.utils.get(ctx.guild.roles, name="Architect")
        if Architect in roles:
            locations = open_locations_db()
            players = open_player_db()
            mobile_objects = open_mobile_object_db()
            location_name = players[str(name)].get('Location')
            if str(npc_name) in mobile_objects:
                type = mobile_objects[str(npc_name)].get("type")
                if type == "npc":
                    locations[location_name]["npc"].append(str(npc_name))
                    save_location_db(locations)
                    await ctx.send("You summon " + str(npc_name) + " to " + str(location_name))
                else:
                    await ctx.send(str(npc_name) + " is not NPC.")
            else:
                await ctx.send("There is no such a mob in Chiania.")
        else:
            await ctx.send("You don't have permission to cast this spell...")

    @commands.command(pass_context=True, brief='input !change_population number to modify a room',
                      description='change monster population')
    async def change_population(self, ctx, number):
        name = ctx.message.author
        roles = ctx.author.roles
        Architect = discord.utils.get(ctx.guild.roles, name="Architect")
        if Architect in roles:
            locations = open_locations_db()
            players = open_player_db()
            location_name = players[str(name)]['Location']
            locations[location_name]["monster_population"] = int(number)
            save_location_db(locations)
            await ctx.send("You increase the monster population of " + str(location_name) + " to " + str(number))
        else:
            await ctx.send("You don't have permission to cast this spell...")

    @commands.command(pass_context=True,
                      brief='input !add_door <room name> to create a door in current location, and link it to a room. If the room does not exist, it would be created as well.',
                      description='add a door in current location and link it to another location.')
    async def add_door(self, ctx, *, target):
        name = ctx.message.author
        roles = ctx.author.roles
        Architect = discord.utils.get(ctx.guild.roles, name="Architect")
        if Architect in roles:
            players = open_player_db()
            location_name = players[str(name)].get('Location')
            add_door(location_name, target)
            await ctx.send("You constructed a door to " + str(target))
        else:
            await ctx.send("You don't have permission to cast this spell...")

    @commands.command(pass_context=True,
                      brief='input !create_monster <monster name> to create a monster in Chiania.',
                      description='create a monster.')
    async def create_monster(self, ctx, *, monster_name):
        name = ctx.message.author
        roles = ctx.author.roles
        Architect = discord.utils.get(ctx.guild.roles, name="Architect")
        if Architect in roles:
            log = await add_monster(str(name), str(monster_name))
            await ctx.send("You try to create " + str(monster_name) + " in Chiania! " + log)
        else:
            await ctx.send("You don't have permission to cast this spell...")

    @commands.command(pass_context=True,
                      brief='input !modify_monster <args> to modify a monster in Chiania.',
                      description='modify a monster.')
    async def modify_monster(self, ctx, *, args=""):
        name = ctx.message.author
        roles = ctx.author.roles
        Architect = discord.utils.get(ctx.guild.roles, name="Architect")
        if Architect in roles:
            if args != "":
                monster_name = ""
                health = ""
                attack = ""
                description = ""
                icon = ""
                portrait = ""
                args = args.split(",")
                for i in args:
                    divide = i.split(":")
                    if divide[0] == "name":
                        monster_name = str(divide[1])
                    if divide[0] == "health":
                        health = int(divide[1])
                    if divide[0] == "attack":
                        attack = int(divide[1])
                    if divide[0] == "description":
                        description = str(divide[1])
                    if divide[0] == "icon":
                        icon = str(divide[1])
                    if divide[0] == "portrait":
                        portrait = str(divide[1])
                mobile_objects = open_mobile_object_db()
                if monster_name in mobile_objects:
                    if health != "":
                        mobile_objects[monster_name]["health"] = health
                    if attack != "":
                        mobile_objects[monster_name]["attack"] = attack
                    if description != "":
                        mobile_objects[monster_name]["description"] = description
                    if icon != "":
                        mobile_objects[monster_name]["icon"] = icon
                    if portrait != "":
                        mobile_objects[monster_name]["portrait"] = "https://" + portrait

                    save_mobile_object_db(mobile_objects)
                    await ctx.send(str(monster_name) + "'s attributes have been modified.")

                else:
                    await ctx.send("There is no such a monster...")
            else:
                await ctx.send(
                    "Please input !modify_monster name:<monster name>,health:<int>,attack:<int>,description:<description>")
        else:
            await ctx.send("You don't have permission to cast this spell...")


async def add_monster(author_name, monster_name):
    mobile_objects = open_mobile_object_db()
    if monster_name not in mobile_objects:
        mobile_objects[monster_name] = {
            "name": monster_name,
            "type": "monster",
            "health": 1,
            "attack": 1,
            "attack_method": None,
            "skill": [],
            "slash_defense": 1,
            "bash_defense": 1,
            "pierce_defense": 1,
            "loot": [],
            "description": None,
            "author": author_name,
            "interaction": False,
            "interaction_link": False,
            "aggression": "passive",
            "category": "not_defined",
            "icon": "❓",
            "portrait": ""
        }
        save_mobile_object_db(mobile_objects)
        log = monster_name + " is created!"
    else:
        log = monster_name + " already exist!"

    return log


async def add_room(room_name):
    locations = open_locations_db()
    locations[room_name] = {}
    locations[room_name]["area_type"] = None
    locations[room_name]["climate"] = None
    locations[room_name]["east"] = str(room_name)
    locations[room_name]["west"] = str(room_name)
    locations[room_name]["south"] = str(room_name)
    locations[room_name]["north"] = str(room_name)
    locations[room_name]["up"] = str(room_name)
    locations[room_name]["down"] = str(room_name)
    locations[room_name]["movement_type"] = None
    locations[room_name]["monsters"] = []
    locations[room_name]["monster_population"] = 3
    locations[room_name]["description"] = None
    locations[room_name]["visible_object"] = []
    locations[room_name]["icon"] = ""
    locations[room_name]["npc"] = []
    locations[room_name]["constructions"] = {}
    locations[room_name]["name"] = str(room_name)
    save_location_db(locations)


async def add_door(current_location, target_room_name):
    locations = open_locations_db()

    # confirm or create a new room
    target_room_id = ""
    for i in locations:
        if locations[i].get("name") == target_room_name:
            target_room_id = i

    if target_room_id == "":
        room_name = str(random.getrandbits(32))
        target_room_id = room_name
        locations[room_name] = {}
        locations[room_name]["area_type"] = None
        locations[room_name]["climate"] = None
        locations[room_name]["east"] = str(room_name)
        locations[room_name]["west"] = str(room_name)
        locations[room_name]["south"] = str(room_name)
        locations[room_name]["north"] = str(room_name)
        locations[room_name]["up"] = str(room_name)
        locations[room_name]["down"] = str(room_name)
        locations[room_name]["movement_type"] = None
        locations[room_name]["monsters"] = []
        locations[room_name]["monster_population"] = 3
        locations[room_name]["description"] = None
        locations[room_name]["visible_object"] = []
        locations[room_name]["icon"] = ""
        locations[room_name]["npc"] = []
        locations[room_name]["constructions"] = {}
        locations[room_name]["name"] = str(target_room_name)

    # create a door to the new room
    constructions = locations[current_location].get("constructions")
    if constructions == None:
        locations[current_location]["constructions"] = {}
    structure_name = "door to " + str(target_room_name)
    locations[current_location]["constructions"][structure_name] = {
        "name": structure_name,
        "construction_type": "door",
        "teleport": target_room_id,
        "enter": True,
        "description": structure_name,
        "icon": ""
    }

    # create a door in new location to the current room
    current_room_name = locations[current_location].get("name")
    constructions = locations[target_room_id].get("constructions")
    if constructions == None:
        locations[target_room_id]["constructions"] = {}
    structure_name = "door to " + str(current_room_name)
    locations[target_room_id]["constructions"][structure_name] = {
        "name": structure_name,
        "construction_type": "door",
        "teleport": current_location,
        "enter": True,
        "description": structure_name,
        "icon": ""
    }
    save_location_db(locations)


async def setup(bot):
    print("Setup Developer commands...")
    await bot.add_cog(Developer(bot))
