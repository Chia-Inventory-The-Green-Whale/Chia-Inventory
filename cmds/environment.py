from discord.ext import commands
from library.character import *
from library.json_db import *
import discord
import time
import datetime


async def check_account(ctx):
    player_name = str(ctx.message.author)
    player = character(player_name)
    picture_display = ""
    output = player.read_account()
    return output


class Environment(commands.Cog, description='Understand the environment'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief='input !environment',
                      description='input !environment to turn or turn off the environmental message')
    async def environment(self, ctx):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        log = player.switch_environment_message()
        await ctx.reply(log)

    @commands.command(pass_context=True,
                      brief='input !look to understand the environment!',
                      description='look around', aliases=["l"])
    async def look(self, ctx, *, target=None):
        player_name = str(ctx.message.author)
        player = character(player_name)
        picture_display = ""
        output = player.look(target)
        if output["bool"] is True:
            title = str(output["target_name"])

            if 0 < len(output["icon"]) < 10:
                title = str(output["icon"]) + title
            else:
                if output["target_type"] == "Location":
                    title = "📍" + title
                if output["target_type"] == "Structure":
                    title = "🏠" + title
                if output["target_type"] == "Item":
                    title = "📦" + title
                if output["target_type"] == "Monster":
                    title = "👿" + title
                if output["target_type"] == "NFT":
                    title = "💎" + title
                if len(output["icon"]) > 10:
                    picture_display = output["icon"]

            if output["portrait"] is not None:
                if len(output["portrait"]) > 10:
                    picture_display = output["portrait"]

            embed = discord.Embed(
                title=title,
                description=output["log"]
            )
            embed.set_image(url=picture_display)

            if output["mobs"] != "":
                embed.add_field(name="Monsters & NPC", value=yaml(output["mobs"]), inline=False)
            if output["items"] != "":
                embed.add_field(name="Items", value=yaml(output["items"]), inline=True)
            if output["constructions"] != "":
                embed.add_field(name="Structures", value=yaml(output["constructions"]), inline=True)
            if output["exits"] != "":
                embed.add_field(name="Exits", value=yaml(output["exits"]), inline=True)
            hint = ""
            if output["target_type"] == "Location":
                hint += "Hint: Please input !go <direction> or !go <structure name> to move location, or input !k <monster name> for hunting."
                # hint += "請輸入 !go <方向> 或 !go <建築物名稱> 進行移動。輸入 !k <怪物名稱> 進行狩獵。"
            await ctx.reply(hint, embed=embed)
        else:
            await ctx.reply(output["log"])


    @commands.command(pass_context=True,
                      brief='input !who to know who is in this locality!',
                      description='who is here')
    async def who(self, ctx):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        location_name, player_here = player.who_is_here()
        log = "Adventurers in " + str(location_name)
        log += "\n" + "---------------------------------------"
        log += "\n"
        if len(player_here) > 0:
            for i in player_here:
                log += i + "  "
        else:
            log += "No other adventurers here."
        log += "\n" + "---------------------------------------"
        await ctx.reply(apache(log))

    @commands.command(pass_context=True,
                      brief='input !catches to check how many preys you got!',
                      description='check how many preys you got', aliases=["cat"])
    async def catches(self, ctx):
        system_channel = self.bot.get_channel(int(1023204349196906638))
        player_name = str(ctx.message.author)
        stats = character(player_name)
        stats.read_account()
        mobile_objects = open_mobile_object_db()
        preys = stats.catch
        monster_name = dict.keys(preys)
        embed1 = discord.Embed()
        log = "Level: " + str(stats.level) + ", Exp: " + str(stats.player_exp) + "/" + str(
            stats.next_exp) + ", Coin: " + str(
            stats.coin) + ' 🪙'
        embed1.add_field(name=player_name + "'s Status", value=css(log), inline=False)
        log = ""
        number = 1
        column = 1

        for i in monster_name:
            if i in mobile_objects:
                log += "\n" + str(i) + mobile_objects[str(i)].get("icon") + " (" + str(preys[i]) + ")  "
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
        await system_channel.send(yaml(str(now) + ": " + player_name + " is checking catches."))
        await ctx.reply(embed=embed1)

    @commands.command(pass_context=True,
                      brief='input !inventory to check what items are in your backpack!',
                      description='check your backpack', aliases=["inv"])
    async def inventory(self, ctx):
        player_name = str(ctx.message.author)
        system_channel = self.bot.get_channel(int(1023204349196906638))
        player = character(player_name)
        player.read_account()
        item_list = get_item_list()
        equipment = player.equipment
        equipment_list = []
        for i in equipment:
            if equipment[i] != "":
                equipment_list.append(equipment[i])
        items = player.inventory
        nfts = player.nft_inventory

        equipment_log = ""
        for i in items:
            if i in item_list and items[i]["number"] > 0:
                item_data = query_item_data(i)
                item_function = item_data.get("function")
                item_icon = item_data.get("icon")
                if item_function == "equipment":
                    equipment_log += "\n" + str(i) + item_icon + "(" + str(
                        items[i]["number"]) + ")  "
        if equipment_log == "":
            equipment_log = "Not available"

        consumable_log = ""
        for i in items:
            if i in item_list and items[i]["number"] > 0:
                item_data = query_item_data(i)
                item_function = item_data.get("function")
                item_icon = item_data.get("icon")
                if item_function == "food":
                    consumable_log += "\n" + str(i) + item_icon + "(" + str(
                        items[i]["number"]) + ")  "
        for i in items:
            if i in item_list and items[i]["number"] > 0:
                item_data = query_item_data(i)
                item_function = item_data.get("function")
                item_icon = item_data.get("icon")
                if item_function == "treasure box":
                    consumable_log += "\n" + str(i) + item_icon + "(" + str(
                        items[i]["number"]) + ")  "
        for i in items:
            if i in item_list and items[i]["number"] > 0:
                item_data = query_item_data(i)
                item_function = item_data.get("function")
                item_icon = item_data.get("icon")
                if item_function == "key":
                    consumable_log += "\n" + str(i) + item_icon + "(" + str(
                        items[i]["number"]) + ")  "
        if consumable_log == "":
            consumable_log = "Not available"

        material_log = ""
        for i in items:
            if i in item_list and items[i]["number"] > 0:
                item_data = query_item_data(i)
                item_function = item_data.get("function")
                item_icon = item_data.get("icon")
                if item_function == "craft":
                    material_log += "\n" + str(i) + item_icon + "(" + str(
                        items[i]["number"]) + ")  "
        if material_log == "":
            material_log = "Not available"

        quest_log = ""
        for i in items:
            if i in item_list and items[i]["number"] > 0:
                item_data = query_item_data(i)
                item_function = item_data.get("function")
                item_icon = item_data.get("icon")
                if item_function == "quest":
                    quest_log += "\n" + str(i) + item_icon + "(" + str(
                        items[i]["number"]) + ")  "
        if quest_log == "":
            quest_log = "Not available"

        other_log = ""
        for i in items:
            if i in item_list and items[i]["number"] > 0:
                item_data = query_item_data(i)
                item_function = item_data.get("function")
                item_icon = item_data.get("icon")
                if item_function == "pet":
                    other_log += "\n" + str(i) + item_icon + "(" + str(
                        items[i]["number"]) + ")  "

        for i in items:
            if i in item_list and items[i]["number"] > 0:
                item_data = query_item_data(i)
                item_function = item_data.get("function")
                item_icon = item_data.get("icon")
                if item_function == "crop":
                    other_log += "\n" + str(i) + item_icon + "(" + str(
                        items[i]["number"]) + ")  "

        for i in items:
            if i in item_list and items[i]["number"] > 0:
                item_data = query_item_data(i)
                item_function = item_data.get("function")
                item_icon = item_data.get("icon")
                if item_function == "junk":
                    other_log += "\n" + str(i) + item_icon + "(" + str(
                        items[i]["number"]) + ")  "

        for i in items:
            if i not in item_list:
                other_log += "\n" + str(i) + "❓" + "(" + str(items[i]["number"]) + ")  "
        if other_log == "":
            other_log = "Not available"

        embed1 = discord.Embed(
            title=player_name + "'s In-game Items"
        )
        embed1.add_field(name="Equipment", value=css(equipment_log), inline=True)
        embed1.add_field(name="Consumable", value=css(consumable_log), inline=True)
        embed1.add_field(name="Material", value=css(material_log), inline=True)
        embed1.add_field(name="Quest", value=css(quest_log), inline=True)
        embed1.add_field(name="Other", value=css(other_log), inline=True)
        await ctx.reply(embed=embed1)

        embed3 = discord.Embed(
            title=player_name + "'s On-chain Items"
        )
        log = ""
        number = 1
        column = 1
        pass_list = ["icon", "item_type", "nft_id", "portrait"]
        for i in nfts:
            if i in equipment_list:
                log += "\n" + str(i) + "(eq.)  "
            else:
                production = False
                for j in nfts[i]:
                    if j not in pass_list:
                        if nfts[i][j].get("type") == "produce_item":
                            production = True
                if production:
                    cd = player.production / 720
                    percentage = str(round(cd * 100)) + '%'
                    log += "\n" + str(i) + "(cd {})  ".format(percentage)
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
        await system_channel.send(yaml(str(now) + ": " + player_name + " is checking inventory."))
        await ctx.reply(embed=embed3)


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
    await bot.add_cog(Environment(bot))
