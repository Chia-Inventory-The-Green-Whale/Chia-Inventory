from discord.ext import commands
from library.json_db import *
import discord
import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()


class Dictionary(commands.Cog, description='Dictionary'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True,
                      brief='input !study_monster to understand the monster!',
                      description='study_monster')
    async def study_monster(self, ctx, *, monster_name):
        mobile_objects = open_mobile_object_db()
        in_game_items = open_in_game_items_db()
        if mobile_objects.get(str(monster_name)) == None:
            await ctx.send("There is no such a monster...")

        else:
            monster_name = str(mobile_objects[str(monster_name)]["name"])
            monster_type = str(mobile_objects[str(monster_name)]["type"])
            monster_description = mobile_objects[str(monster_name)]["description"]
            monster_author = mobile_objects[str(monster_name)]["author"]
            monster_aggression = mobile_objects[str(monster_name)]["aggression"]
            monster_category = mobile_objects[str(monster_name)]["category"]

            # monster health
            monster_health = int(mobile_objects[str(monster_name)]["health"])
            monster_health_max = int(mobile_objects[str(monster_name)]["health"] * 4 / 3)

            # monster atk
            monster_attack = int(mobile_objects[str(monster_name)]["attack"])
            monster_attack_max = int(mobile_objects[str(monster_name)]["attack"] * 4 / 3)

            # monster defense
            monster_DEFslash = mobile_objects[str(monster_name)]["slash_defense"]
            monster_DEFbash = mobile_objects[str(monster_name)]["bash_defense"]
            monster_DEFpierce = mobile_objects[str(monster_name)]["pierce_defense"]

            # loot
            loot = mobile_objects[str(monster_name)]["loot"]
            loot_pool = []
            monster_loot = ""
            if len(loot) > 0:
                for i in loot:
                    if i not in loot_pool:
                        loot_pool.append(i)
                for i in loot_pool:
                    if i != "None":
                        icon = in_game_items[i].get("icon")
                        monster_loot += str(i) + str(icon) + "  "

            # visual effects
            monster_icon = mobile_objects[str(monster_name)].get("icon")
            monster_portrait = mobile_objects[str(monster_name)].get("portrait")
            if monster_portrait == None:
                monster_portrait = ""

            # calculation of exp and coins
            monster_exp = int(monster_health / 7) + int(
                (monster_DEFslash + monster_DEFbash + monster_DEFpierce) / 3) + int(
                monster_attack / 6)
            monster_exp_max = int(monster_health_max / 7) + int(
                (monster_DEFslash + monster_DEFbash + monster_DEFpierce) / 3) + int(
                monster_attack_max / 6)

            monster_coin = int(monster_exp / 5)
            monster_coin_max = int(monster_exp_max / 5) + 2

            embed = discord.Embed()
            monster_name = str(monster_name) + str(monster_icon)
            embed.set_author(name=str(monster_name))
            log = ""
            log += "\n" + "Attack: " + str(monster_attack) + "-" + str(monster_attack_max)
            log += "\n" + "Health: " + str(monster_health) + "-" + str(monster_health_max)
            log += "\n" + "Slash Defense: " + str(monster_DEFslash)
            log += "\n" + "Bash Defense: " + str(monster_DEFbash)
            log += "\n" + "Pierce Defense: " + str(monster_DEFpierce)
            embed.add_field(name="Combat", value=yaml(log), inline=False)
            log = ""
            log += "\n" + "Type: " + str(monster_type)
            log += "\n" + "Aggression: " + str(monster_aggression)
            log += "\n" + "Description: " + str(monster_description)
            log += "\n" + "Author: " + str(monster_author)
            embed.add_field(name="Background", value=yaml(log), inline=False)
            log = ""
            log += "\n" + "Exp: " + str(monster_exp) + "-" + str(monster_exp_max)
            log += "\n" + "Coins: " + str(monster_coin) + "-" + str(monster_coin_max)
            log += "\n" + "Items: " + str(monster_loot)
            embed.add_field(name="Loot", value=yaml(log), inline=False)
            embed.set_image(url=monster_portrait)
            await ctx.send(embed=embed)

    @commands.command(pass_context=True,
                      brief='input !mob_list to see how many kinds of mobile objects occur in Chiania!',
                      description='list mobile objects', aliases=["mob"])
    async def mob_list(self, ctx, mob_type=""):
        mobile_objects = open_mobile_object_db()
        page = 1
        title = "List of mobile objects in Chiania"
        log = ""
        if str(mob_type) in ["monster", "npc", "pet"]:
            # before final page
            for i in mobile_objects:
                if mobile_objects[i].get("type") == str(mob_type):
                    log += "\n" + str(i) + mobile_objects[str(i)]["icon"] + "  Type: " + mobile_objects[str(i)]["type"]
                    if len(log) > 2000:
                        embed = discord.Embed(
                            title=str(title + " Page " + str(page)),
                            description=yaml(log)
                        )
                        page += 1
                        log = ""
                        await ctx.reply(embed=embed)
            # print final page
            if len(log) > 0:
                embed = discord.Embed(
                    title=str(title + " Page " + str(page)),
                    description=yaml(log)
                )
                await ctx.reply(embed=embed)
        else:
            await ctx.reply("Please specify a type of mobile object for search. e.g. !mob monster")

    @commands.command(pass_context=True,
                      brief='input !commands to list commands in Chiania!',
                      description='list commands')
    async def commands(self, ctx):
        embed = discord.Embed(
            title="List of Commands"
        )
        Knodledge = ""
        Knodledge += "\n" + "1. !study_attributes"
        Knodledge += "\n" + "2. !study_item"
        Knodledge += "\n" + "3. !study_monster <monster name>"
        Knodledge += "\n" + "4. !mob_list"
        Knodledge += "\n" + "5. !commands"
        embed.add_field(name="Knowledge", value=yaml(Knodledge), inline=True)

        Combat = ""
        Combat += "\n" + "1. !hunt"
        Combat += "\n" + "2. !attack <monster name>"
        Combat += "\n" + "3. !catches"
        Combat += "\n" + "4. !equip <equipment name>"
        Combat += "\n" + "5. !inventory"
        Combat += "\n" + "6. !enhance <equipment name>"
        embed.add_field(name="Combat", value=yaml(Combat), inline=True)

        Exploration = ""
        Exploration += "\n" + "1. !look <nothing> or <structure name> or <item name> or <monster name>"
        Exploration += "\n" + "2. !explore"
        Exploration += "\n" + "3. !go <a direction>"
        Exploration += "\n" + "4. !who"
        Exploration += "\n" + "5. !get <an item>"
        Exploration += "\n" + "6. !investigate <structure name>"
        Exploration += "\n" + "7. !home"
        Exploration += "\n" + "8. !leave_manor"
        Exploration += "\n" + "9. !reclaim <a direction>"
        Exploration += "\n" + "10. !construct <an construction item>"
        Exploration += "\n" + "11. !destruct <a structure name>"
        Exploration += "\n" + "12. !move_house"
        embed.add_field(name="Exploration", value=yaml(Exploration), inline=False)

        Chiania_Coin = ""
        Chiania_Coin += "\n" + "1. !xcc withdraw <coin number>"
        Chiania_Coin += "\n" + "2. !xcc deposit <coin number>"
        Chiania_Coin += "\n" + "3. !xcc deposit confirm"
        embed.add_field(name="Chiania Coin", value=yaml(Chiania_Coin), inline=True)

        Interaction = ""
        Interaction += "\n" + "1. !feed <pet name>"
        Interaction += "\n" + "2. !adopt <pet item or NFT>"
        Interaction += "\n" + "3. !ask <NPC name> <nothing or index 1> <nothing or index 2>"
        Interaction += "\n" + "4. !use <item name>"
        embed.add_field(name="Interaction", value=yaml(Interaction), inline=True)

        Game_Development = ""
        Game_Development += "\n" + "1. !excavate <direction>"
        Game_Development += "\n" + "2. !change_name <name>"
        Game_Development += "\n" + "3. !close_door is the command to close all directions"
        Game_Development += "\n" + "4. !change_type <area type> for determine area type"
        Game_Development += "\n" + "5. !add_monster <monster name>"
        Game_Development += "\n" + "6. !add_npc <npc name>"
        Game_Development += "\n" + "7. !change_population <number> to determine maximum monster population in the location"
        Game_Development += "\n" + "8. !add_door <target location name>"
        embed.add_field(name="Game Development", value=yaml(Game_Development), inline=False)

        await ctx.reply(embed=embed)


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


def yaml(log):
    output = "\n" + "```yaml" + "\n" + log + "```"
    return output


async def setup(bot):
    await bot.add_cog(Dictionary(bot))
