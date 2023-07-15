from discord.ext import commands
import discord
import random
from library.json_db import *
import urllib3
from bs4 import BeautifulSoup
import sys
import time
import datetime
from os import path
from subprocess import Popen, PIPE, list2cmdline
from sqlite3 import connect

sys.path.insert(0, path.join(path.dirname(__file__)))
sys.path.insert(0, path.join(path.dirname(__file__), 'chia_blockchain'))
from chia_blockchain.chia.util.bech32m import decode_puzzle_hash

db_path = "/home/chiainventory/.chia/mainnet/db/blockchain_v2_mainnet.sqlite"


class db_wrapper():
    def connect_to_db(self):
        self._conn = connect(db_path)
        self._dbcursor = self._conn.cursor()

    def get_coins_by_puzzlehash(self, puzzlehash):
        self._dbcursor.execute(
            "SELECT timestamp, amount, confirmed_index, spent_index, coin_parent FROM coin_record WHERE puzzle_hash=? ORDER BY timestamp DESC",
            (bytes.fromhex(puzzlehash),))
        return self._dbcursor.fetchall()


class Tools(commands.Cog, description='Tools'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, brief='input !dice to roll a D20', description='a D20 dice')
    async def dice(self, ctx):
        dices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                 '19', '20']
        value = "./dice/Dice{}.png".format(random.choice(dices))
        await ctx.send(file=discord.File(value))


    @commands.command(pass_context=True, brief='input !balance to check how much XCC you have',
                      description='check XCC balance')
    async def balance(self, ctx):
        await ctx.reply("This function is not available now.")

        # system_channel = self.bot.get_channel(int(1023204349196906638))
        # now = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
        # name = ctx.message.author
        # players = open_player_db()
        # address = players[str(name)].get("Reward Address")
        # if address != "":
        #    inner_puzzle_bytes = decode_puzzle_hash(address)
        #    inner_puzzle = inner_puzzle_bytes.hex()
        #    tail = "04e28f2f24e1a8ba8290b30293976cdee933d1683220014316da6f8ee7753920"
        #   wrapped_puzzle = get_wrapped_puzzle(inner_puzzle, tail)
        #    balance = get_records(wrapped_puzzle)
        #    await system_channel.send(yaml(str(now) + ": " + str(name) + " is checking wallet." ))
        #    await ctx.send("You have a total of " + str(balance) + " XCC in wallet!")
        # else:
        #    await ctx.send("You not yet setup an address...Please input !find_address.")

    @commands.command(pass_context=True, brief='input !xcc <argument 1> <argument 2> to deposit or withdraw XCC.',
                      description='please input deposit or withdraw in <argument 1>' + "\n" + " and input a number (e.g. 100) in <argument 2>")
    async def xcc(self, ctx, arg1="", arg2=""):
        name = ctx.message.author
        system_channel = self.bot.get_channel(int(1023204349196906638))
        now = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
        players = open_player_db()
        await update_transactions()
        if str(name) in players:
            if arg1 == "deposit":
                if str(arg2) == "confirm":
                    transactions = open_transaction_db()
                    in_use = False
                    for i in transactions:
                        if transactions[i].get("in_use") == str(name):
                            in_use = True
                            in_use_address = i
                    if in_use == True:
                        history = transactions[in_use_address].get("transactions")
                        index = str(len(history))
                        deposit_amount = transactions[in_use_address]["transactions"][index].get("amount")
                        latest_timestamp = transactions[in_use_address]["transactions"][index][
                            "latest_transaction"].get("timestamp")
                        latest_amount = transactions[in_use_address]["transactions"][index]["latest_transaction"].get(
                            "amount")
                        wrapped_puzzle = transactions[in_use_address].get("xcc_wrapped_puzzle_hash")
                        current_timestamp, current_amount = get_latest_transaction(wrapped_puzzle)
                        if int(current_timestamp) != latest_timestamp:
                            if current_amount == deposit_amount:
                                transactions[in_use_address]["transactions"][index]["latest_transaction"][
                                    "timestamp"] = int(current_timestamp)
                                transactions[in_use_address]["transactions"][index]["latest_transaction"][
                                    "amount"] = current_amount
                                transactions[in_use_address]["in_use"] = False
                                transactions[in_use_address]["transactions"][index]["confirmation"] = True
                                save_transaction_db(transactions)

                                players[str(name)]["Wallet"] += deposit_amount
                                await save_player_db(players)
                                await system_channel.send(
                                    yaml(str(now) + ": " + str(name) + " deposited " + str(deposit_amount) + "."))
                                await ctx.reply(
                                    "Your transaction is confirmed! " + str(deposit_amount) + " CC has been delivered.")
                            else:
                                await ctx.reply("Someone transferred wrong number of XCC to this address.")
                        else:
                            await ctx.reply("There is no new transaction in this address.")
                    else:
                        await ctx.reply("You not yet apply a deposition.")

                elif str(arg2) == "cancel":
                    transactions = open_transaction_db()
                    in_use = False
                    for i in transactions:
                        if transactions[i].get("in_use") == str(name):
                            in_use = True
                            in_use_address = i
                    if in_use == True:
                        transactions[in_use_address]["in_use"] = False
                        save_transaction_db(transactions)
                        await system_channel.send(
                            yaml(str(now) + ": " + str(name) + " cancelled a deposit request."))
                        await ctx.reply("You have canceled the request of deposition.")
                    else:
                        await ctx.reply("You not yet apply a deposition.")

                else:
                    try:
                        amount = int(arg2)
                        if amount > 0:
                            transactions = open_transaction_db()
                            in_use = False
                            for i in transactions:
                                if transactions[i].get("in_use") == str(name):
                                    in_use = True

                            if in_use == False:
                                address_list = []
                                for i in transactions:
                                    if transactions[i].get("in_use") == False:
                                        address_list.append(i)
                                if len(address_list) > 0:
                                    address = random.choice(address_list)
                                    wrapped_puzzle = transactions[address].get("xcc_wrapped_puzzle_hash")
                                    timestamp, coin = get_latest_transaction(wrapped_puzzle)
                                    history = transactions[address].get("transactions")
                                    transactions[address]["in_use"] = str(name)
                                    index = 1 + len(history)
                                    transactions[address]["transactions"][str(index)] = {
                                        "adventurer": str(name),
                                        "type": "deposit",
                                        "amount": amount,
                                        "timestamp": int(time.time()),
                                        "time": str(now),
                                        "confirmation": False,
                                        "latest_transaction": {
                                            "timestamp": int(timestamp),
                                            "amount": coin
                                        }
                                    }
                                    save_transaction_db(transactions)
                                    await system_channel.send(
                                        yaml(str(now) + ": " + str(name) + " submitted a deposit request of " + str(
                                            amount) + "."))
                                    await ctx.reply(
                                        "A deposition address is assigned. Please send XCC to: " + str(address))
                                else:
                                    await ctx.reply("Currently there is no address available for deposit XCC.")
                            else:
                                await ctx.reply("You already assigned an address to deposit XCC.")
                        else:
                            await ctx.reply("Please input correct amount of XCC.")
                    except:
                        await ctx.reply("Please input correct amount of XCC.")

            elif arg1 == "withdraw":
                try:
                    amount = int(arg2)
                    wallet = players[str(name)].get("Wallet")
                    if wallet >= amount:
                        reputation = players[str(name)].get("Reputation")
                        if reputation == None:
                            reputation = 0
                            players[str(name)]["Reputation"] = 0
                        if reputation >= amount:
                            address = players[str(name)].get("Reward Address")
                            if address == None:
                                address = ""
                            if address != "":
                                latest_withdraw = players[str(name)].get("Latest Withdraw")
                                if latest_withdraw == None:
                                    latest_withdraw = 0
                                current_time = int(time.time())
                                time_pass = current_time - latest_withdraw
                                if time_pass > 3600:
                                    if amount > 0:
                                        players[str(name)]["Latest Withdraw"] = current_time
                                        players[str(name)]["Reputation"] -= amount
                                        players[str(name)]["Wallet"] -= amount
                                        await save_player_db(players)
                                        await send(address, amount)
                                        await system_channel.send(
                                            yaml(str(now) + ": " + str(name) + " withdrew " + str(
                                                amount) + " XCC."))
                                        await ctx.reply("You successfully withdraw " + str(amount) + " XCC.")
                                    else:
                                        await ctx.reply("There is no need to withdraw " + str(amount) + " XCC.")
                                else:
                                    time_left = 3600 - time_pass
                                    minute = time_left // 60
                                    second = time_left % 60
                                    await system_channel.send(
                                        yaml(str(now) + ": " + str(name) + " failed to withdraw CC."))
                                    await ctx.reply(
                                        "You need to wait for " + str(minute) + " minutes and " + str(
                                            second) + " seconds for next request.")
                            else:
                                await ctx.reply("Please input !find_address to apply a address for receiving XCC")
                        else:
                            await ctx.reply("You don't have enough reputation to withdraw.")
                    else:
                        await ctx.reply("You don't have enough CC to withdraw.")
                except:
                    await ctx.reply("Please input correct amount of XCC.")
            else:
                await ctx.reply("Please input !xcc deposit <amount> or !xcc withdraw <amount> as argument.")
        else:
            await ctx.reply("You are not adventurer, this command is not available for you!")


def get_wrapped_puzzle(inner_puzzle, tail):
    out = Popen(["cdv",
                 "clsp",
                 "cat_puzzle_hash",
                 inner_puzzle,
                 "-t",
                 tail], stdin=PIPE, text=True, stdout=PIPE)
    print("the commandline is {}".format(list2cmdline(out.args)))
    out = out.communicate()
    out = list(out)
    print("the wrapped puzzle hash is " + str(out[0]))

    return out[0]


def get_records(wrapped_puzzle):
    out = Popen(["cdv",
                 "rpc",
                 "coinrecords",
                 "--by",
                 "puzzlehash",
                 wrapped_puzzle], stdin=PIPE, text=True, stdout=PIPE)
    out = out.communicate()
    out = str(out)
    balance = 0
    if out != "('[]\\n', None)":
        out = out[53:]
        out = out.split('"amount": ')
        if len(out) > 0:
            for i in out:
                i = i.split(",")
                i = i[0]
                print(i)
                i = int(i)
                balance += i
    balance = balance / 1000

    return balance


def get_latest_transaction(wrapped_puzzle):
    db_read = db_wrapper()
    db_read.connect_to_db()
    rows = db_read.get_coins_by_puzzlehash(puzzlehash=wrapped_puzzle)
    if len(rows) > 0:
        timestamp, amount, confirmed_index, spent_index, coin_parent = rows[0]
        coin = int.from_bytes(amount, 'big') / 1000
    else:
        timestamp = 0
        coin = 0
    return int(timestamp), coin


async def send(xch_address, amount):
    out = Popen(["chia",
                 "wallet",
                 "send",
                 "-f", "2990254927",
                 "-i", "2",
                 "-m", "0.00000001",  # 10000 mojo
                 "-a", str(amount),
                 "-t", str(xch_address)  # receive address
                 ], stdin=PIPE, text=True, stdout=PIPE, shell=False)

    out.communicate("y\ny")
    out = out.communicate()
    print(str(xch_address) + " withdraw " + str(amount))
    print(str(out))


async def update_transactions():
    transactions = open_transaction_db()
    for i in transactions:
        if transactions[i].get("in_use") != False:
            history = transactions[i].get("transactions")
            index = str(len(history))
            latest_request_time = int(transactions[i]["transactions"][index].get("timestamp"))
            current_time = int(time.time())
            time_pass = current_time - latest_request_time
            if time_pass > 3600:
                transactions[i]["in_use"] = False
    save_transaction_db(transactions)


def yaml(log):
    output = "\n" + "```yaml" + "\n" + log + "```"
    return output


async def setup(bot):
    await bot.add_cog(Tools(bot))
