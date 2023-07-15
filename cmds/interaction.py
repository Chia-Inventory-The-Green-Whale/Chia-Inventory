from discord.ext import commands
import discord
from library.mobile_object import *
from library.locations import *
from library.json_db import *
from library.character import *
from library.mongo import *
import os
import discord
import time
import datetime


class Interaction(commands.Cog, description='Interact with NPCs and items'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True,
                      brief='input !go direction(east, west, south, north) to move to different localities!',
                      description='go some where', aliases=["g", "enter", "ent"])
    async def go(self, ctx, *, direction):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()

        # let's go
        log, old_location, new_location = player.go(direction)

        # submit a system log
        now = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
        system_channel = self.bot.get_channel(int(1023204349196906638))
        await system_channel.send(yaml(f"{str(now)}: {player_name} walked to {new_location}"))

        # define guild function
        async def find_guild():
            for guild in self.bot.guilds:
                if guild.name == 'Chia Inventory':
                    return guild

        # submit message
        if old_location != new_location:
            leave_message = f"{player_name} leaved..."
            arrival_message = f"{player_name} shows up here!"
            guild = await find_guild()
            player_list = get_player_list()
            for someone in player_list:
                if someone != player_name:
                    message_status = get_player_message_status(someone)
                    if message_status:
                        location_name = get_player_location(someone)
                        if location_name == old_location:
                            try:
                                receiver = guild.get_member_named(someone)
                                await receiver.send(yaml(leave_message))
                            except:
                                print("Cannot contact " + str(someone))
                        elif location_name == new_location:
                            try:
                                receiver = guild.get_member_named(someone)
                                await receiver.send(yaml(arrival_message))
                            except:
                                print("Cannot contact " + str(someone))

        await ctx.reply(log)

        # look after move
        player.read_account()
        current_location = locate(player.location).name
        log, icon, portrait, target_name, constructions, exits, mobs, target_type, items = player.look(None)
        title = str(current_location)
        if target_type == "Location":
            title = "📍" + title
        if target_type == "Structure":
            title = "🏠" + title
        if target_type == "Item":
            title = "📦" + title
        if target_type == "Monster":
            title = "👿" + title
        if target_type == "NFT":
            title = "💎" + title
        embed = discord.Embed(
            title=title,
            description=log
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

    @commands.command(pass_context=True,
                      brief='input !get to obtain items on the ground.',
                      description='get an item')
    async def get(self, ctx, *, item_name=""):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        item_list = get_item_list()
        locations = open_locations_db()
        location = locate(player.location)
        ground = location.ground
        if item_name != "":
            if type(ground) == list:
                if item_name in ground:
                    if item_name in item_list:
                        item_data = query_item_data(item_name)
                        player.get_item(item_name, 1)
                        locations[str(location.id)]["ground"].remove(str(item_name))
                        save_location_db(locations)
                        icon = item_data.get("icon")
                        await ctx.reply("You pickup " + str(item_name) + str(icon) + "!")
                    else:
                        await ctx.reply("This item is not listed in database yet!")
                elif item_name == "all":
                    count = 0
                    for i in ground:
                        player.get_item(i, 1)
                        locations[str(location.id)]["ground"].remove(i)
                        count += 1
                    save_location_db(locations)
                    await ctx.reply("You pickup " + str(count) + " items.")
                else:
                    await ctx.reply("There is no such a thing!")
            else:
                await ctx.reply("There is no such a thing!")
        else:
            await ctx.reply("Pick what? Please input !get <item name>")

    @commands.command(pass_context=True, brief='input !sell item_name to sell an item.',
                      description='sell an item')
    async def sell(self, ctx, *, item_name):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        # add number arg
        number = 1
        args = item_name.split()
        item_name = ""
        for i in args:
            if i[:7] == "number:":
                number = i[7:]
                try:
                    number = int(number)
                    if number < 1:
                        number = 1
                except:
                    number = number
                if type(number) != int:
                    number = 1
                args.remove(i)
            else:
                conjunction_list = ["of", "on", "at", "the"]
                if i in conjunction_list:
                    item_name += str(i) + " "
                else:
                    i = i.capitalize()
                    item_name += str(i) + " "
        item_name = item_name.rstrip(item_name[-1])
        log = player.sell_item(item_name, number)
        await ctx.reply(log)

    @commands.command(pass_context=True, brief='input !feed pet_name to feed a pet in your house.',
                      description='feed a pet')
    async def feed(self, ctx, *, pet_name):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        location = locate(player.location)

        # make the command case-insensitive
        if pet_name != "":
            args = pet_name.split()
            pet_name = ""
            for i in args:
                pet_name += i.capitalize() + " "
            pet_name = pet_name.rstrip(pet_name[-1])

        if pet_name in location.visible_object:
            item_list = get_item_list()
            on_chain_items = player.nft_inventory
            NFTs = []
            for NFT in on_chain_items:
                NFTs.append(NFT[:8])
            inventory = player.inventory
            if pet_name in item_list:
                item_data = query_item_data(pet_name)
                item_type = item_data.get("item_type")
                if item_type == "pet":
                    feedstuff = item_data["in-game-attributes"]["1"].get("feed")
                    if feedstuff in inventory and inventory[feedstuff]["number"] > 0:
                        player.lost_item(feedstuff)
                        # get buff
                        for i in item_data["in-game-attributes"]:
                            if item_data["in-game-attributes"][i].get("buff_requirement") == "feed":
                                buff_name = "pet_buff_" + str(i)
                                buff_attributes = item_data["in-game-attributes"].get(i)
                                player.get_buff(buff_name, buff_attributes)
                        await ctx.reply(f"You gave {str(pet_name)} some {str(feedstuff)} and he/she looks happy!")

                    elif feedstuff in NFTs:
                        for i in item_data["in-game-attributes"]:
                            if item_data["in-game-attributes"][i].get("buff_requirement") == "feed":
                                buff_name = "pet_buff_" + str(i)
                                buff_attributes = item_data["in-game-attributes"].get(i)
                                player.get_buff(buff_name, buff_attributes)
                        await ctx.reply(f"You gave {str(pet_name)} some {str(feedstuff)} and he/she looks happy!")
                    else:
                        await ctx.reply("You don't have " + str(feedstuff) + " to feed " + str(pet_name))
                else:
                    await ctx.reply(str(pet_name) + " is not a pet.")
            elif pet_name in on_chain_items:
                type = on_chain_items[pet_name]["item_type"]
                pass_list = ["icon", "item_type", "nft_id", "portrait"]
                if type == "pet":
                    feedstuff = on_chain_items[pet_name]["0"].get("feed")
                    if feedstuff in inventory and inventory[feedstuff]["number"] > 0:
                        inventory[feedstuff]["number"] -= 1
                        for i in on_chain_items[pet_name]:
                            if i not in pass_list:
                                if on_chain_items[pet_name][i].get("buff_requirement") == "feed":
                                    buff_name = "pet_buff_" + str(i)
                                    buff_attributes = on_chain_items[pet_name]["in-game-attributes"].get(i)
                                    player.get_buff(buff_name, buff_attributes)

                        await ctx.reply(f"You gave {str(pet_name)} some {str(feedstuff)} and he/she looks happy!")

                    elif feedstuff in NFTs:
                        for i in on_chain_items[pet_name]:
                            if i not in pass_list:
                                if on_chain_items[pet_name][i].get("buff_requirement") == "feed":
                                    buff_name = "pet_buff_" + str(i)
                                    buff_attributes = on_chain_items[pet_name].get(i)
                                    player.get_buff(buff_name, buff_attributes)
                        await ctx.reply(f"You gave {str(pet_name)} some {str(feedstuff)} and he/she looks happy!")

                    else:
                        await ctx.reply(NFTs)
                        await ctx.reply("You don't have " + str(feedstuff) + " to feed " + str(pet_name))
            else:
                await ctx.reply(str(pet_name) + " is not a pet.")
        else:
            await ctx.reply(str(pet_name) + " is not here.")

    @commands.command(pass_context=True, brief='input !hire <farmer_name> to hire a farmer in your farm.',
                      description='hire a farmer')
    async def hire(self, ctx, *, farmer_name):
        timestamp = str(time.time())
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        locations = open_locations_db()
        mobile_objects = open_mobile_object_db()

        # 20220930 added check items in inventory
        in_game_items = player.inventory
        on_chain_items = player.nft_inventory
        all_items = {}
        for i in on_chain_items:
            all_items[i] = on_chain_items[i]
        for i in in_game_items:
            all_items[i] = in_game_items[i]

        if farmer_name in all_items:
            if farmer_name in in_game_items:
                farmer_attributes = in_game_items.get(farmer_name)
            else:
                farmer_attributes = on_chain_items.get(farmer_name)

            if farmer_attributes["item_type"] == "farmer":
                current_location = player.location
                is_manor = player.manor
                if is_manor != None:
                    lands = player.lands
                    if current_location in lands:
                        constructions_here = locations[current_location].get("constructions")
                        if len(constructions_here) > 0:
                            is_farm_here = False
                            for i in constructions_here:
                                if constructions_here[i].get("construction_type") == "farm":
                                    is_farm_here = True
                            if is_farm_here == True:
                                is_house_here = False
                                for i in constructions_here:
                                    if constructions_here[i].get("construction_type") == "accommodation":
                                        is_house_here = True
                                if is_house_here == True:
                                    if farmer_name in in_game_items:
                                        player.lost_item(farmer_name)

                                    if farmer_name in on_chain_items:
                                        nft_id = player.nft_inventory[farmer_name].get("nft_id")
                                        change_nft_owner(nft_id, player_name)

                                    if farmer_name not in mobile_objects:
                                        mobile_objects[str(farmer_name)] = {}
                                        mobile_objects[str(farmer_name)]["name"] = str(farmer_name)
                                        mobile_objects[str(farmer_name)]["type"] = "farmer"
                                        mobile_objects[str(farmer_name)]["health"] = 9999
                                        mobile_objects[str(farmer_name)]["attack"] = 999
                                        mobile_objects[str(farmer_name)]["attack_method"] = "attack"
                                        mobile_objects[str(farmer_name)]["skill"] = []
                                        mobile_objects[str(farmer_name)]["slash_defense"] = 99
                                        mobile_objects[str(farmer_name)]["bash_defense"] = 99
                                        mobile_objects[str(farmer_name)]["pierce_defense"] = 99
                                        mobile_objects[str(farmer_name)]["loot"] = []
                                        mobile_objects[str(farmer_name)]["description"] = "A Chiania farmer"
                                        mobile_objects[str(farmer_name)]["author"] = None
                                        mobile_objects[str(farmer_name)]["interaction"] = True
                                        mobile_objects[str(farmer_name)]["aggression"] = "passive"
                                        mobile_objects[str(farmer_name)]["category"] = "not_defined"
                                        mobile_objects[str(farmer_name)]["icon"] = "🧑‍🌾"
                                        mobile_objects[str(farmer_name)]["employer"] = str(player_name)
                                        save_mobile_object_db(mobile_objects)
                                        await ctx.reply(str(farmer_name) + " is summoned to Chiania.")

                                    else:
                                        # change employer
                                        mobile_objects[str(farmer_name)]["employer"] = str(player_name)
                                        # remove previous location
                                        for i in locations:
                                            if locations[i].get("farmer") != None:
                                                if str(farmer_name) in locations[i].get("farmer"):
                                                    locations[i]["farmer"].remove(str(farmer_name))
                                        save_location_db(locations)

                                    if str(farmer_name) not in locations[current_location]["farmer"]:
                                        place_farmer(current_location, str(farmer_name))
                                        await ctx.reply("You hired " + str(farmer_name) + " to work in this location.")
                                    else:
                                        await ctx.reply(str(farmer_name) + " is here.")
                                else:
                                    await ctx.reply("There are no houses here!")
                            else:
                                await ctx.reply("There are no farms here!")
                        else:
                            await ctx.reply("There are no farms and houses here!")
                    else:
                        await ctx.reply("You have to hire farmers in your lands!")
                else:
                    await ctx.reply("You have to own a manor first!")
            else:
                await ctx.reply("You can not hire " + str(farmer_name) + ", it is not a farmer!")
        else:
            await ctx.reply("You don't have " + str(farmer_name))

    @commands.command(pass_context=True, brief='input !adopt pet_name to adopt a pet in your house.',
                      description='adopt a pet')
    async def adopt(self, ctx, *, pet_name):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()

        # 20220930 added check items in inventory
        in_game_items = player.inventory
        on_chain_items = player.nft_inventory
        all_items = {}
        for i in on_chain_items:
            all_items[i] = on_chain_items[i]
        for i in in_game_items:
            all_items[i] = in_game_items[i]

        if pet_name in all_items:
            if pet_name in in_game_items:
                pet_attributes = in_game_items[pet_name]
            else:
                pet_attributes = on_chain_items[pet_name]

            if pet_attributes["item_type"] == "pet":
                home = player.home
                if player.location == home:
                    if home != "Tavern":
                        locations = open_locations_db()
                        mobile_objects = open_mobile_object_db()
                        npc_name = pet_name

                        if pet_name not in mobile_objects:
                            mobile_objects[str(npc_name)] = {}
                            mobile_objects[str(npc_name)]["name"] = str(npc_name)
                            mobile_objects[str(npc_name)]["type"] = "pet"
                            mobile_objects[str(npc_name)]["health"] = 9999
                            mobile_objects[str(npc_name)]["attack"] = 999
                            mobile_objects[str(npc_name)]["attack_method"] = "attack"
                            mobile_objects[str(npc_name)]["skill"] = []
                            mobile_objects[str(npc_name)]["slash_defense"] = 99
                            mobile_objects[str(npc_name)]["bash_defense"] = 99
                            mobile_objects[str(npc_name)]["pierce_defense"] = 99
                            mobile_objects[str(npc_name)]["loot"] = []
                            mobile_objects[str(npc_name)]["description"] = str(player_name) + "'s pet."
                            mobile_objects[str(npc_name)]["author"] = None
                            mobile_objects[str(npc_name)]["interaction"] = True
                            mobile_objects[str(npc_name)]["aggression"] = "passive"
                            mobile_objects[str(npc_name)]["category"] = "not_defined"
                            mobile_objects[str(npc_name)]["icon"] = "\uD83D\uDC15"
                            save_mobile_object_db(mobile_objects)
                            await ctx.reply("You adopted " + str(pet_name))

                        else:
                            if mobile_objects[str(npc_name)]["description"] == str(player_name) + "'s pet.":
                                await ctx.reply("You already adopted " + str(pet_name))
                            else:
                                await ctx.reply("You adopted " + str(pet_name))

                        if pet_name not in locations[home]["npc"]:
                            place_mob(home, pet_name)
                            await ctx.reply("You called " + str(pet_name) + " back to your home.")
                        else:
                            await ctx.reply(str(pet_name) + " is in your home.")

                        if pet_name in in_game_items:
                            player.lost_item(pet_name)
                    else:
                        await ctx.reply("You cannot adopt pets in Tavern!")
                else:
                    await ctx.reply("You are not in home!")
            else:
                await ctx.reply("You can not adopt " + str(pet_name) + ", it is not a pet!")
        else:
            await ctx.reply("You don't have " + str(pet_name))

    @commands.command(pass_context=True, brief='input !ask npc_name question_key to get information from NPC.',
                      description='ask a question')
    async def ask(self, ctx, npc_name, *keys):
        system_channel = self.bot.get_channel(int(1023204349196906638))
        now = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
        name = ctx.message.author
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        timestamp = int(time.time())
        time_pass = timestamp - player.latest_command
        if time_pass > 2:
            location = player.location
            await system_channel.send(yaml(str(now) + ": " + str(player_name) + " interacted with " + str(npc_name)))
            mobile_objects = get_mobile_object(str(location))

            # make the command case-insensitive
            npc_name = npc_name.capitalize()

            if npc_name in mobile_objects:
                head, message, outcome, hint, item_choose = player.ask_npc(npc_name, keys)
                embed = discord.Embed()
                embed.set_author(name=str(head))
                embed.add_field(name="Communication", value=yaml(message), inline=False)
                if outcome is not None:
                    embed.add_field(name="Outcome", value=yaml(outcome), inline=False)
                embed.add_field(name="Hint", value=yaml(hint), inline=False)
                if item_choose != "None":
                    await name.send(file=discord.File(item_choose))
                    await system_channel.send(yaml(str(now) + ": " + str(name) + " got a nft item."))
                    os.remove(item_choose)
                await ctx.reply(embed=embed)

            else:
                await ctx.reply("There is no such a person here...")
        else:
            await ctx.reply(f"You need to wait for {str(time_pass)} seconds!")

    @commands.command(pass_context=True, brief='input !use item_name to use an item in your inventory.',
                      description='use an item')
    async def use(self, ctx, *, item_name):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        player_inventory = player.inventory
        args = item_name.split()
        item_name = ""
        number = 1
        for i in args:
            if i[:7] == "number:":
                number = i[7:]
                try:
                    number = int(number)
                    if number < 1:
                        number = 1
                except:
                    number = number
                if type(number) != int:
                    number = 1
                args.remove(i)
            else:
                conjunction_list = ["of", "on", "at", "the"]
                if i in conjunction_list:
                    item_name += str(i) + " "
                else:
                    i = i.capitalize()
                    item_name += str(i) + " "
        item_name = item_name.rstrip(item_name[-1])

        # check whether item in inventory
        if item_name in player_inventory:
            log = player.use_item(item_name, number)
            embed = discord.Embed()
            embed.add_field(name="Outcome", value=apache(log), inline=False)
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("You don't have " + str(item_name))


def apache(log):
    output = "\n" + "```apache" + "\n" + log + "```"
    return output


def yaml(log):
    output = "\n" + "```yaml" + "\n" + log + "```"
    return output


def fast_scandir(dirname):
    subfolders = [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders


async def setup(bot):
    await bot.add_cog(Interaction(bot))
