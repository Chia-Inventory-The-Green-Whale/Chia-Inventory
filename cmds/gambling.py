from discord.ext import commands
import discord
from library.character import *


class Gambling(commands.Cog, description='Play games with Mimic and players'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief='input !dice to roll a D20', description='a D20 dice')
    async def dice(self, ctx):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        if player.coin >= 10:
            dices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                     '19', '20']
            dice = random.choice(dices)
            value = "./dice/Dice{}.png".format(dice)
            win_list, reward = what_is_current_dice()
            if dice in win_list:
                player.earn_coin(reward)
                await ctx.reply(
                    f"You place a bet and throw a dice, it's {dice}, YOU WIN! Mimic has sent you {reward} coins.",
                    file=discord.File(value))
            else:
                player.earn_coin(-10)
                await ctx.reply(
                    f"You place a bet and throw a dice, it's {dice}, FAILED! Mimic has taken 10 coins from you...",
                    file=discord.File(value))
        else:
            await ctx.reply(f"You need at least 10 CC in wallet...")


def yaml(log):
    output = "\n" + "```yaml" + "\n" + log + "```"
    return output


async def setup(bot):
    await bot.add_cog(Gambling(bot))
