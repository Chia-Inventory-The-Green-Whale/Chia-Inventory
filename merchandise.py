from discord.ext import commands
import discord
import os
import ujson as json
import random


class Merchant(commands.Cog, description='Merchant'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True,
                      brief='input !merchandise to check what items are on sale!',
                      description='check what items are on sale')
    async def merchandise(self, ctx):
        merchantlog = "Merchandise List"
        merchantlog += ("\n" + '---------------------------------------')
        merchantlog += ("\n" +
                        'Serial No.   Item Name              Price(Items in Stock)')
        item_dict, log = items()

        merchantlog += log

        merchantlog += ("\n" +
                        '---------------------------------------')
        merchantlog += ("\n" +
                        'Type !buy Serial No. to buy an equipment!')

        await ctx.send(apache(merchantlog))

    @commands.command(pass_context=True, brief='input !buy Serial Number to buy an equipment',
                      description='buy an equipment')
    async def buy(self, ctx, serial_number):
        name = ctx.message.author
        item_dict, log = items()

        with open('./Players.json', 'r') as file:
            players = json.load(file)
            file.close()

        if item_dict.get(serial_number) == None:
            await ctx.send("There is no such a thing!")

        elif item_dict[serial_number]['number'] < 1:
            await ctx.send("This item is sold out!")

        else:
            item_name = item_dict[serial_number]['name']
            price = item_dict[serial_number]['price']
            path = item_dict[serial_number]["item_path"]
            wallet = players[str(name)]["Wallet"]
            check = players[str(name)].get(item_name)

            if check == None:
                players[str(name)][item_name] = 0

            limit = players[str(name)][item_name]

            if int(limit) >= 3:
                await ctx.send("You can't buy more!")

            elif int(wallet) < int(price):
                await ctx.send("You can't afford it!")

            else:
                players[str(name)]["Wallet"] -= int(price)
                players[str(name)][item_name] += 1
                with open('./Players.json', 'w') as file:
                    json.dump(players, file)

                await ctx.send("You bought " + item_name + ", " + str(
                    price) + " 🪙➜ 👟👟 (Please enable direct message from bot, or you won't get the offer...)")
                await name.send("Here is your offer...")
                list = os.listdir(path)
                item_choose = path + "/" + random.choice(list)
                await name.send(file=discord.File(item_choose))
                os.remove(item_choose)


def items():
    item_list = fast_scandir("./merchant/")
    item_dict = {}
    log = ""
    for i in range(0, len(item_list)):
        item_dict[str(i)] = {}
        item_dict[str(i)]["item_path"] = item_list[i]

        list = os.listdir(item_dict[str(i)]["item_path"])
        item_dict[str(i)]["number"] = len(list)
        number = str(item_dict[str(i)]["number"])

        item_list[i] = item_list[i][11:]
        item = item_list[i].split('_price_')

        item_dict[str(i)]["name"] = item[0]
        item_dict[str(i)]["price"] = item[1]
        distance1 = 4 - len(str(i))
        distance2 = 23 - len(item_dict[str(i)]["name"])
        price = str(item_dict[str(i)]["price"])
        log += "\n" + str(i) + "    " * distance1 + item_dict[str(i)][
            "name"] + " " * distance2 + price + " (" + number + ")"
    return item_dict, log


def fast_scandir(dirname):
    subfolders = [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders


def setup(bot):
    bot.add_cog(Merchant(bot))


def apache(log):
    output = "\n" + "```apache" + "\n" + log + "```"
    return output
