from discord.ext import commands
import discord
from library.character import *


class Dictionary(commands.Cog, description='Dictionary'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True,
                      brief='input !study_attributes to understand how attributes work!',
                      description='study_attributes')
    async def study_attributes(self, ctx):
        log = "Basic attributes:"
        log += "\n" + "1. Str: 10-15 + level/10"
        log += "\n" + "2. Dex: 10-15 + level/10"
        log += "\n" + "3. Con: 10-15 + level/10"
        log += "\n" + "4. Int: 10-15 + level/10"
        log += "\n" + "5. Wis: 10-15 + level/10"
        log += "\n" + "6. Cha: 10-15 + level/10"
        log += "\n" + "7. Luc: 10-15 + level/10"
        log += "\n"
        log += "\n" + "Attributes modification:"
        log += "\n" + "1. Slash: += Slash * Str / 10"
        log += "\n" + "2. Bash: += Bash * Str / 10"
        log += "\n" + "3. Pierce: += Pierce * (Str + Dex) / 20"
        log += "\n" + "4. Defense: += Con / 10"
        log += "\n" + "5. Health: += Con / 3"
        log += "\n"
        log += "\n" + "Impacts of enhancements:"
        log += "\n" + "1. Constant: Attr. = value + enhancement * 0.1"
        log += "\n" + "2. Random: Attr. = randint((1 + enhancement * 0.2), value)"
        log += "\n" + "3. Level Scale: Attr. = level / (value - enhancement * 0.1)"
        log += "\n" + "4. Probability: Chance = Probability (%) + enhancement"
        log += "\n"
        log += "\n" + "Attribute limitations:"
        log += "\n" + "1. Slash, Bash, and Pierce <= level + 1 + confidence/3"
        log += "\n" + "2. Defense <= level + confidence/3"
        log += "\n" + "3. Str, Dex, Con, Int, Wis, Cha and Luc <= level*1.5 + 5 + confidence/2"
        log += "\n"
        log += "\n" + "Attributes in Combat:"
        log += "\n" + "1. Player's Damage = the highest Damage Type to against monster's Defense (e.g. High Pierce against Monster's low Pierce Defense)"
        log += "\n" + "2. Maximum Damage of Monster = Monster Damage * 2 - Luc/10 - Defense - Random(1 - Con/5)"
        log += "\n" + "3. Maximum Damage of Player = Player Damage * 2 + Luc/10"
        log += "\n" + "4. Wise affect the probability to trigger 🧠⚔️"
        log += "\n" + "5. Int affect the probability to trigger 🪄️"
        log += "\n" + "6. Dex affect the probability to trigger ⚔️⚔ and the probability of  👟👟"
        log += "\n" + "7. Cha affect the probability to trigger ❓⚔"
        log += "\n"
        log += "\n" + "About confidence:"
        log += "\n" + "Confidence = number of items equipped. (Adventurers feel more confident when they have more equipment...)"

        embed = discord.Embed(
            title=str("About Attributes"),
            description=yaml(log)
        )
        await ctx.reply(embed=embed)

    @commands.command(pass_context=True,
                      brief='input !study_item to understand attributes of an item!',
                      description='study_item')
    async def study_item(self, ctx, *, item_name):
        in_game_items = get_item_list()
        on_chain_items = get_nft_name_list()
        item_icon = ""
        # check whether it is in-game item
        if str(item_name) in in_game_items:
            item_data = query_item_data(item_name)
            item_type = item_data["item_type"]
            item_icon = item_data["icon"]
            item_function = item_data["function"]
            log = "\n" + "Item type: " + str(item_type)
            log += "\n" + "Item function: " + str(item_function)
            if item_function == "equipment":
                log += "\n" + "Attributes:"
                item_attributes = item_data["in-game-attributes"]
                count = 0
                for i in item_attributes:
                    count += 1
                    log += "\n" + str(count) + ": " + str(item_attributes[i]["type"]) + "(" + str(
                        item_attributes[i]["factor"]) + ") = " + str(item_attributes[i]["value"])
            embed = discord.Embed(
                title=str(item_name) + str(item_icon),
                description=yaml(log)
            )
            imageurl = ""
            embed.set_image(url=imageurl)

        else:
            nft_id = find_nft_id(str(item_name))
            if nft_id is not None:
                item_data = query_nft_data(nft_id)
                item_type = item_data.get("item_type")
                item_icon = item_data.get("icon")
                item_portrait = item_data.get("portrait")
                item_owner = item_data.get("in-game owner")
                item_attributes = item_data.get("in-game-attributes")
                item_enhancement = item_data["in-game-attributes"]["enhancement"]["value"]
                ownership_fee = item_enhancement * (item_enhancement + 21) / 2
                log = "\n" + "Item type: " + str(item_type)
                log += "\n" + "Current owner: " + str(item_owner)
                log += "\n" + "Fee for change ownership: " + str(ownership_fee)
                log += "\n" + "Attributes:"
                count = 0
                for j in item_attributes:
                    count += 1
                    log += "\n" + str(count) + ": " + str(item_attributes[j]["type"]) + "(" + str(
                        item_attributes[j].get("factor")) + ") = " + str(item_attributes[j]["value"])

            else:
                log = "There is no such a thing!"

            embed = discord.Embed(
                title=str(item_name),
                description=yaml(log)
            )
            embed.set_image(url=str(item_portrait))
        await ctx.reply(embed=embed)


def yaml(log):
    output = "\n" + "```yaml" + "\n" + log + "```"
    return output


async def setup(bot):
    await bot.add_cog(Dictionary(bot))
