from discord.ext import commands
from library.attribute_assign import *
from library.stamina_setting import *
from library.locations import *
from library.json_db import *
from library.character import *
from library.mongo import *
import discord
import time
import datetime
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

class Registration(commands.Cog, description='Registration'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True,
                      brief='input !license xch_address did_address to mint a license to your xch address.',
                      description='register an adventurer license')
    async def license(self, ctx, xch_address, DID_address):
        log = f"You {str(ctx.message.author)} requested to mint an adventurer license to the address {xch_address} \n"
        log += f"Please assign the adventurer license to your DID: {DID_address}"
        print(len(xch_address))
        print(len(DID_address))
        # get avatar
        url = str(ctx.message.author.avatar)
        response = requests.get(url)
        avatar = Image.open(BytesIO(response.content))
        card = Image.open('al.png')
        license_name = f"{str(ctx.message.author)}.png"
        card.paste(avatar, (32, 32))
        card_write = ImageDraw.Draw(card)
        myFont = ImageFont.truetype('comic.ttf', 13)
        bdFont = ImageFont.truetype('comicbd.ttf', 13)
        card_write.text((280, 38), f"Adventurer", font=bdFont, fill=(255, 255, 255))
        card_write.text((280, 58), f"{str(ctx.message.author)}", font=myFont, fill=(255, 255, 255))
        card_write.text((280, 98), f"XCH address", font=bdFont, fill=(255, 255, 255))
        card_write.text((280, 118), f"{str(xch_address[:31])}", font=myFont, fill=(255, 255, 255))
        card_write.text((280, 138), f"{str(xch_address[31:])}", font=myFont, fill=(255, 255, 255))
        card_write.text((280, 178), f"DID", font=bdFont, fill=(255, 255, 255))
        card_write.text((280, 198), f"{str(DID_address[:31])}", font=myFont, fill=(255, 255, 255))
        card_write.text((280, 218), f"{str(DID_address[31:62])}", font=myFont, fill=(255, 255, 255))
        card_write.text((280, 238), f"{str(DID_address[62:])}", font=myFont, fill=(255, 255, 255))
        card.save(license_name, format="PNG")

        # create metadata
        metadata = {
            "format": "CHIP-0007",
            "name": f"Adventurer License of {str(ctx.message.author)}",
            "description": f"Adventurer License of {str(ctx.message.author)}",
            "minting_tool": "Chia Inventory Minting Tool",
            "sensitive_content": False,
            "series_number": 1,
            "series_total": 99999999999,
            "attributes": [
                {"trait_type": "adventurer",
                 "value": str(ctx.message.author)},
                {"trait_type": "xch_address",
                 "value": str(xch_address)},
                {"trait_type": "did",
                 "value": str(DID_address)}
            ],
            "collection": {
                "name": "Chia Inventory",
                "id": "4bd1103d-28e0-4a60-9f66-e63d7cc6bf0a",
                "attributes": [
                    {"type": "icon",
                     "value": f"https://community.chivescoin.org/uploadnftplatformchia/20220705130616_b0953505abd5078a57e827f1c61d3881_406639.png"
                     },
                    {"type": "banner",
                     "value": f"https://community.chivescoin.org/uploadnftplatformchia/20220711001518_b0953505abd5078a57e827f1c61d3881_359817.gif"
                     },
                    {"type": "description",
                     "value": f"Collectable equipments, potions, and items for your adventures in Chia metaverse.\nMe, The Green Whale, I am playing as a storyteller and blacksmith in an endless RPG game. People who grab my equipments are able to join fights and events, and win more NFTs for free. They can also sell them to allow newbies to join the game. This is my concept, a RPG style endless NFT set."
                     },
                    {"type": "twitter",
                     "value": "https://twitter.com/mrcic3"
                    }
                ]
            }
        }

        await ctx.reply(log)
        await ctx.reply("this is your adventurer license", file=discord.File(license_name))


    @commands.command(pass_context=True, brief='input !find_address to search for a reward address of XCH',
                      description='find a reward address')
    async def find_address(self, ctx):
        system_channel = self.bot.get_channel(int(1023204349196906638))
        now = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
        player_name = str(ctx.message.author)
        await system_channel.send(yaml(str(now) + ": " + str(player_name) + " is trying to apply a wallet address."))
        player = character(player_name)
        player.read_account()
        log = player.find_address()
        await ctx.reply(log)

    @commands.command(pass_context=True,
                      brief='input !register chia digital id (DID) for registration. Please assume this DID as your "character", mimic cont only one weapon, shield, species card, classes suit, body armor, helmet, glove, and boot. Please send only the item you want to equip to this DID!',
                      description='register DID')
    async def register(self, ctx, DID):
        name = ctx.message.author
        player_name = str(ctx.message.author)
        player_list = get_player_list()
        if DID[0:10] == "did<:chia:":
            DID = 'did:chia:' + str(DID[29:])
            await ctx.reply(f'Mimic detected you are using an emoji in the DID address. He corrected you address as {DID}')

        if player_name not in player_list:
            # check if it is DID
            if len(DID) != 62:
                if len(DID) == 68:
                    if DID[0:9] == 'did:chia:':
                        await ctx.reply('I detected you are using a formal DID address.')
                        # record player address, generate exp and wallet
                        did_list = get_did_list()
                        if str(DID) not in did_list:
                            await ctx.reply('I never seen this DID, try to memorize it...')
                            client = pymongo.MongoClient()
                            db = client["Chiania"]
                            collection = db["players"]
                            players_v2 = {
                                "Name": player_name,
                                "Address": {
                                    "DID": str(DID),
                                    "Reward Address": None
                                },
                                "Status": {
                                    "Exp": 0,
                                    "Life": 1,
                                    "Stamina": 600,
                                    "Mount Stamina": 0,
                                    "Drunk": 0,
                                    "Life_count": 0,
                                    "Location": "Tavern",
                                    "Channel": 1001435613641318462,
                                    "Cool Down": {
                                        "Latest Withdraw": 0,
                                        "Latest Hunt": 0
                                    },
                                    "Production": 0,
                                    "Home": "Tavern",
                                    "Buff": {},
                                    "Home Stay": 0,
                                    "Reforge Penalty": {},
                                    "Equipment": {},
                                    "Message": False
                                },
                                "Class": {
                                    "Basic": {
                                        "Name": None,
                                        "Level": 0
                                    },
                                    "Advance": {
                                        "Name": None,
                                        "Level": 0
                                    }
                                },
                                "Skills": {

                                },
                                'Assets': {
                                    "Wallet": 0,
                                    "Reputation": 0,
                                    "Manor": {},
                                    "Inventory": {
                                        "Items": {},
                                        "NFTs": {}
                                    },
                                    "Catch": {}
                                },
                                "Achievements": {},
                                "Quests": {}
                            }
                            collection.insert_one(players_v2)
                            Adventurer = discord.utils.get(name.guild.roles, name="Adventurer")
                            await name.add_roles(Adventurer)
                            await ctx.reply('...I have memorized your name (' + str(name) + ') and your DID (' + DID[
                                                                                                                 0:15] + '...). Be aware of the other mimics in the dungeon, Boo!')
                            newbie_guide = "Welcome to join Chia Inventory!"
                            newbie_guide += "\n" + "Chia Inventory is a MUD (multi-user dungeon), which is the origin of MMORPG (massively multiplayer online role-playing game)."
                            newbie_guide += "\n" + "Different to traditional MUD, Chia Inventory is built in Discord server, implemented NFTs on Chia blockchain as equipments and graphic elements."
                            newbie_guide += "\n"
                            newbie_guide += "\n" + "Here are basic steps to play Chia Inventory:"
                            newbie_guide += "\n" + "1."
                            newbie_guide += "\n" + "Input !inventory to check your inventory. You would find a Knife in your inventory."
                            newbie_guide += "\n"
                            newbie_guide += "\n" + "2."
                            newbie_guide += "\n" + "Input !equip Knife to equip the Knife. If you don't input item name after the command !equip, it would just display what you wear."
                            newbie_guide += "\n"
                            newbie_guide += "\n" + "3."
                            newbie_guide += "\n" + "Input !profile to check your attributes and status. It's hard to determine the strength of a character in Chia Inventory, but..., it's sure that new players should fight with Cockroach and Mouse for leveling."
                            newbie_guide += "\n"
                            newbie_guide += "\n" + "4."
                            newbie_guide += "\n" + "Input !look to see what monsters are around you. If you see Cockroach, you can input !attack Cockroach to start hunting."
                            newbie_guide += "\n"
                            newbie_guide += "\n" + "5."
                            newbie_guide += "\n" + "Feel boring about this place? Input !go east to move to East Kingdom Street. You can go anywhere by inputing !go directions(west, east, south, north)"

                            embed = discord.Embed(
                                title="Guide for New Players",
                                description=newbie_guide
                            )
                            await ctx.reply(embed=embed)

                        else:
                            await ctx.reply("DID is duplicated! Don't steal someone's DID...")
                    else:
                        await ctx.reply(f'DID address should begin with "did:chia:". This is not a DID!')
                else:
                    await ctx.reply(f'DID address should have a length of 68. This is not a DID!')
            else:
                await ctx.reply(
                'Length wrong, this is more likely an XCH address, not DID address. Please follow the guide to mint a DID address.')
        else:
            await ctx.reply("You already registered.")

    @commands.command(pass_context=True,
                      brief='input !profile to generate a player profile and check your equipments and status',
                      description='generate player profile and status', aliases=["pro"])
    async def profile(self, ctx, *, display_type=" "):
        name = ctx.message.author
        player_name = str(ctx.message.author)
        system_channel = self.bot.get_channel(int(1023204349196906638))
        now = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
        await system_channel.send(yaml(str(now) + ": " + str(name) + " is checking adventurer profile..."))
        stats = character(player_name)
        stats.read_account()
        profilelog = ("\n" + 'Level: ' + str(stats.level) + ', Exp: ' + str(stats.player_exp) + "/" + str(
            stats.next_exp))
        profilelog += ("\n" + 'DID: ' + stats.address)
        profilelog += ("\n" + 'Reward address: ' + stats.reward_address)
        stats.check_equipment()
        embed = discord.Embed()
        embed.add_field(name="Information", value=yaml(profilelog), inline=False)

        # status
        location = locate(str(stats.location))
        profilelog = ""
        profilelog += ("\n" + 'Life: ' + str(stats.life))
        profilelog += (', Stamina: ' + str(stats.stamina))
        profilelog += (", Mount Stamina: " + str(round(stats.mount_stamina, 1)))
        profilelog += ("\n" + 'Drunk: ' + str(round(stats.drunk, 1)) + ' minutes (+0.2 sta./min.)')
        profilelog += ("\n" + 'Stay Home: ' + str(stats.home_stay) + ' minutes')
        if len(stats.buff) > 0:
            profilelog += ("\n" + 'Buff: ')
            for i in stats.buff:
                profilelog += str(stats.buff[i]["type"]) + "(" + str(stats.buff[i]["factor"]) + ")" + "=" + str(
                    stats.buff[i]["value"]) + " (" + str(stats.buff[i]["buff_duration"]) + " min.)"
        profilelog += ("\n" + 'Location: ' + str(location.name))
        embed.add_field(name="Status", value=yaml(profilelog), inline=False)

        profilelog = ""
        eq_list = ["Weapon", "Shield", "Hat",
                   "Necklace", "Shoulder", "Armor",
                   "Armbands", "Gloves", "Pants",
                   "Shoes", "Belt", "Cloak",
                   "Ring", "Mount", "Herb",
                   "Familiar", "Portrait", "Spirit"]

        for i in eq_list:
            eq_name = str(stats.equipment.get(i))
            if eq_name != "":
                profilelog += "\n" + str(i) + ": " + eq_name
                if eq_name in stats.nft_inventory:
                    profilelog += " +" + str(stats.nft_inventory[eq_name]["enhancement"]["value"])
                if eq_name in stats.inventory:
                    enhancement = stats.inventory[eq_name]["in-game-attributes"].get("enhancement")
                    if enhancement is None:
                        enhancement_level = 0
                    else:
                        enhancement_level = stats.inventory[eq_name]["in-game-attributes"]["enhancement"].get("value")
                        if enhancement_level is None:
                            enhancement_level = 0
                    profilelog += " +" + str(enhancement_level)

        portrait = ""
        if stats.portrait != "":
            if str(stats.portrait) in stats.nft_inventory:
                portrait = stats.nft_inventory[str(stats.portrait)].get("portrait")

        embed.add_field(name="Equipment", value=yaml(profilelog), inline=False)

        # assign attributes
        stats.assign_attribute()
        profilelog = ""
        profilelog += ("\n" + 'Slash: ' + str(round(stats.slash, 1)))
        profilelog += ("\n" + 'Bash: ' + str(round(stats.bash, 1)))
        profilelog += ("\n" + 'Pierce: ' + str(round(stats.pierce, 1)))
        profilelog += ("\n" + 'Magic: ' + str(round(stats.magic, 1)))
        profilelog += ("\n" + 'Defense: ' + str(round(stats.defense, 1)))
        profilelog += ("\n" + 'HP: ' + str(round(stats.health, 1)))
        embed.add_field(name="Combat", value=yaml(profilelog), inline=True)

        profilelog = ""
        profilelog += ("\n" + 'Str: ' + str(round(stats.str, 1)))
        profilelog += ("\n" + 'Dex: ' + str(round(stats.dex, 1)))
        profilelog += ("\n" + 'Con: ' + str(round(stats.con, 1)))
        profilelog += ("\n" + 'Int: ' + str(round(stats.int, 1)))
        profilelog += ("\n" + 'Wis: ' + str(round(stats.wis, 1)))
        profilelog += ("\n" + 'Cha: ' + str(round(stats.cha, 1)))
        profilelog += ("\n" + 'Luc: ' + str(round(stats.luc, 1)))
        embed.add_field(name="Attributes", value=yaml(profilelog), inline=True)

        # asset
        profilelog = ""
        profilelog += ("\n" + 'Coin: ' + str(stats.coin) + ' 🪙')
        profilelog += ("\n" + 'Repu.: ' + str(stats.reputation))
        profilelog += ("\n" + 'Lands: ' + str(len(stats.lands)))
        profilelog += ("\n" + 'Build.: ' + str(len(stats.constructions)))
        embed.add_field(name="Assets", value=yaml(profilelog), inline=True)

        if display_type == " ":
            if portrait is not None:
                imageurl = str(portrait)
            else:
                imageurl = ""
        elif display_type == "t":
            imageurl = ""
        embed.set_thumbnail(url=imageurl)
        embed.set_author(name=str(stats.name), icon_url=imageurl)
        await ctx.reply(embed=embed)

    @commands.command(pass_context=True,
                      brief='input !nft_sync to update your NFT inventory',
                      description='update NFT inventory')
    async def nft_sync(self, ctx):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        log = player.nft_sync()
        await ctx.reply(log)

    @commands.command(pass_context=True,
                      brief='input !rank to show leaderboard of players',
                      description='generate player leaderboard')
    async def rank(self, ctx):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        players = get_all_players()
        log = "Adventure Ranking"
        log += "\n" + "---------------------------------------"
        rank_list = {}
        rank = 1
        for player in players:
            rank_list[player["Name"]] = player["Status"]["Exp"]

        rank_list = dict(reversed(sorted(rank_list.items(), key=lambda item: item[1])))

        for player_name in rank_list:
            player_level, player_exp, next_exp = level(rank_list[player_name])
            log += "\n" + str(rank) + "  " + str(player_name) + " Lv: " + str(player_level)
            rank += 1
            if rank == 51:
                log += "\n" + '---------------------------------------'
                await ctx.send(apache(log))


def yaml(log):
    output = "\n" + "```yaml" + "\n" + log + "```"
    return output


def apache(log):
    output = "\n" + "```apache" + "\n" + log + "```"
    return output


async def setup(bot):
    await bot.add_cog(Registration(bot))
