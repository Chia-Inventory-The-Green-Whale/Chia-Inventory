from discord.ext import commands
import discord
from library.character import *


class World_magic(commands.Cog, description='World_magic'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief='cast the spell !happy_new_year to obtain a special NFT!',
                      description='Happy New Year!')
    async def happy_new_year(self, ctx):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        magic_choose, log = player.cast_world_magic("2022")
        await ctx.reply(log)

    @commands.command(pass_context=True, brief='cast the spell !goblinization to transform into a goblin',
                      description='goblinization')
    async def goblinization(self, ctx):
        player_name = str(ctx.message.author)
        receiver = ctx.message.author
        player = character(player_name)
        player.read_account()
        magic_choose, log = player.cast_world_magic("goblinization")
        await ctx.reply(log)
        if magic_choose != "":
            await receiver.send(file=discord.File(magic_choose))
        os.remove(magic_choose)


async def setup(bot):
    await bot.add_cog(World_magic(bot))
