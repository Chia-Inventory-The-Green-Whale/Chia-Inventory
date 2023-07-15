import os
from os import path
import sys
import datetime
import discord
from library.locations import *
from library.stamina_setting import *
from discord.ext import commands, tasks
from pretty_help import DefaultMenu, PrettyHelp
import psutil
from library.mongo import *

sys.path.insert(0, path.join(path.dirname(__file__)))
sys.path.insert(0, path.join(path.dirname(__file__), 'chia_blockchain'))

TOKEN = ''
GUILD = 'Chia Inventory'

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=['!', "/", '*', "."], case_insensitive=True, intents=intents)
menu = DefaultMenu('🌱')  # You can copy-paste any icons you want.
bot.help_command = PrettyHelp(navigation=menu, color=discord.Colour.green())
st = time.time()
db_backup_path = "./backupDB/"


def yaml(log):
    output = "\n" + "```yaml" + "\n" + log + "```"
    return output


async def load_extensions():
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            extension = f'cmds.{filename[:-3]}'
            print("Load extension: " + str(extension))
            await bot.load_extension(extension)


async def find_guild():
    for guild in bot.guilds:
        if guild.name == GUILD:
            return guild


async def load_guilds():
    for guild in bot.guilds:
        if guild.name == GUILD:
            print(
                f'{bot.user} is connected to the following guild: '
                f'{guild.name}(id: {guild.id})'
            )
            NO = 1
            log = ""
            for channel in guild.channels:
                log += "NO." + str(NO) + ": " + str(channel) + "; "
                NO += 1
            print(log)


@bot.event
async def on_ready():
    await load_extensions()
    await load_guilds()
    await timer.start()


@bot.event
async def on_member_join(member):
    Stranger = discord.utils.get(member.guild.roles, name="Stranger")
    log = f"Please type verify yourself in the verification channel. The Captcha Bot would send you a private message, please enable PM, follow the link, and complete the process."
    embed = discord.Embed(
        title=str(f"About Verification"),
        description=log
    )
    embed.set_image(url="https://pbs.twimg.com/profile_images/1545244231249559552/48N7fsvJ_400x400.png")
    await member.add_roles(Stranger)
    await member.send(f"Stranger! welcome to Chia Inventory {member.mention}!", embed=embed)


@bot.event
async def on_member_update(before, after):
    registration_channel = bot.get_channel(int(1000344248312397854))
    if len(before.roles) < len(after.roles):
        newRole = next(role for role in after.roles if role not in before.roles)
        if newRole.name == "Resident":
            log = "Please type /register your_did in this channel for account registration. If you don't know what is DID, take a look on the following guide:"
            embed = discord.Embed(
                title=str(f"About Chia DID"),
                description=log
            )
            imageurl = "https://cdn.discordapp.com/attachments/995478713561001984/1008195184523219014/MakeDID.jpg"
            embed.set_image(url=imageurl)
            await registration_channel.send(
                f"Congratulations! You are now a Resident of Chia Inventory {after.mention}! Please type /register your_did in this channel for registerion as Adventurer.",
                embed=embed)
            log = f"Chia Inventory provides a free NFT for all new players, take a look on the following guide to get it:"
            embed = discord.Embed(
                title=str(f"About Free NFT"),
                description=log
            )
            imageurl = "https://cdn.discordapp.com/attachments/995478713561001984/1008575793493983273/GetGoblin.jpg"
            embed.set_image(url=imageurl)
            await registration_channel.send(embed=embed)


@tasks.loop(seconds=1)
async def timer():
    et = time.time()
    time_pass = round(et - st) - 1
    await charge(et, time_pass)


async def charge(et, time_pass):
    if time_pass % 60 == 0:
        # system information
        timestamp = int(time.time())
        load1, load5, load15 = psutil.getloadavg()
        cpu_usage = int((load15 / os.cpu_count()) * 100)
        memory_usage = psutil.virtual_memory()[2]
        work_hours = int(100 * time_pass / 3600) / 100
        system_channel = bot.get_channel(int(1023204349196906638))
        now = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
        print("Time to scan server status: " + time.ctime(et))

        # prepare message for location
        guild = await find_guild()
        message_for_locations = await monster_spawn()
        active_player = 0
        drunk_player = 0
        player_list = get_player_list()
        for i in player_list:
            # get player data
            player = get_player_data(i)
            # check when the player login
            latest_command = player["Status"].get("Latest Command")
            if latest_command is not None:
                how_long = int(timestamp) - int(latest_command)
                if how_long < 86400:
                    active_player += 1
                    if player["Status"]['Drunk'] > 0:
                        drunk_player += 1

                    # send environmental message
                    environment = player["Status"].get("Message")
                    if environment == True:
                        here = player["Status"].get("Location")
                        if here in message_for_locations:
                            message = message_for_locations.get(here)
                            if message != "":
                                try:
                                    receiver = guild.get_member_named(i)
                                    await receiver.send(yaml(message))
                                except:
                                    print("Cannot contact " + str(i))
            else:
                modify_player_data(str(i), "Status.Latest Command", 0)

        log = f"{str(now)}: Server Status: CPU Usage: {str(cpu_usage)} %; Memory Usage: {str(memory_usage)} %; Working Time: {str(work_hours)}  Hours; Active Players: {str(active_player)}; Drunk Players: {str(drunk_player)}"

        # through a dice
        result = throw_a_dice()
        log += result
        try:
            await system_channel.send(yaml(log))
        except:
            print("Cannot connect Discord server.....")


bot.run(TOKEN)
