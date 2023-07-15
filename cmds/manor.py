from discord.ext import commands
from library.locations import *
from library.stamina_setting import *
import time
import datetime
from library.json_db import *
from library.room_creator import *
from cmds.hunt import fight
from library.character import *
import discord
import urllib3
from bs4 import BeautifulSoup
from library.mobile_object import encounter
from library.mongo import *

http = urllib3.PoolManager()


class Manor(commands.Cog, description='Commands related to manor management'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief='input !tavern to teleport yourself',
                      description='teleport to Tavern')
    async def tavern(self, ctx):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        log = player.teleport("Tavern")
        await ctx.reply(log)

    @commands.command(pass_context=True,
                      brief='input !home to teleport to go home!',
                      description='go home', aliases=["manor"])
    async def home(self, ctx):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        log = player.teleport_to_home()
        await ctx.reply(log)

    @commands.command(pass_context=True,
                      brief='input !leave_manor to leave your manor!',
                      description='leave manor', aliases=["leave_home"])
    async def leave_manor(self, ctx):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        log = player.leave_manor()
        await ctx.reply(log)

    @commands.command(pass_context=True,
                      brief='input !reclaim <direction> to reclaim a new land',
                      description='reclaim a new land')
    async def reclaim(self, ctx, direction):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        direction = direction.lower()
        log = player.reclaim_the_land(direction)
        await ctx.reply(log)

    @commands.command(pass_context=True,
                      brief='input !construct <structure name> to place a structure in current location.',
                      description='construct a structure')
    async def construct(self, ctx, *, structure_name=""):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        log = player.construct(structure_name)
        await ctx.reply(log)

    @commands.command(pass_context=True,
                      brief='input !destruct <structure name> to remove a structure in current location.',
                      description='destruct a structure')
    async def destruct(self, ctx, *, structure_name):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        locations = open_locations_db()
        current_location = player.location
        current_structures = locations[current_location].get("constructions")
        if type(current_structures) != dict:
            locations[current_location]["constructions"] = {}
        if structure_name in current_structures:
            constructions = player.constructions
            owned_construction_list = list(constructions.keys())
            if structure_name in owned_construction_list:
                locations[current_location]["constructions"].pop(structure_name)
                player.remove_a_construction(structure_name)
                save_location_db(locations)
                await ctx.reply("You removed " + str(structure_name) + " from this location.")
            else:
                await ctx.reply("You don't own this structure.")
        else:
            await ctx.reply("There is no such a thing here.")

    @commands.command(pass_context=True,
                      brief='input !move_house to select current (a house belongs to you) as your home!',
                      description='move house', aliases=["set_home"])
    async def move_house(self, ctx):
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        current_location = player.location
        on_chain_items = player.nft_inventory
        if current_location in on_chain_items:
            if on_chain_items[current_location]["item_type"] == "house":
                if player.home != str(current_location):
                    player.change_home(str(current_location))
                    await ctx.reply("You selected " + str(current_location) + " as your home.")
                else:
                    await ctx.reply(str(current_location) + " is already your home.")
            else:
                await ctx.reply(str(current_location) + " is not a house.")
        else:
            await ctx.reply("You don't own the house, " + str(current_location))


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
    await bot.add_cog(Manor(bot))
