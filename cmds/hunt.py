from library.library import *
from library.mobile_object import *
from library.locations import *
from library.stamina_setting import *
from library.character import *
from library.mongo import *
import discord
import time
import datetime

http = urllib3.PoolManager()


class Combat(commands.Cog, description='Combat'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True,
                      brief='input !enhance to enhance your equipment, you also need to prepare Refining Stone.',
                      description='enhance an NFT', aliases=["en"])
    async def enhance(self, ctx, *, equipment_name=" "):
        system_channel = self.bot.get_channel(int(1023204349196906638))
        player_name = str(ctx.message.author)
        player = character(player_name)
        player.read_account()
        in_game_items = player.inventory
        on_chain_items = player.nft_inventory
        if equipment_name != "":
            args = equipment_name.split()
            equipment_name = ""
            for i in args:
                if i != "of" and i != "on" and i != "at" and i != "the" and i[:1] != "(":
                    equipment_name += i.capitalize() + " "
                elif i[:1] == "(":
                    equipment_name += "(" + i[1:].capitalize() + " "
                else:
                    equipment_name += i + " "
            equipment_name = equipment_name.rstrip(equipment_name[-1])
            print(f"{player_name} enhanced {equipment_name}!")
        if equipment_name in on_chain_items:
            equipment_name = equipment_name
            if "Refining Stone" in in_game_items:
                if in_game_items["Refining Stone"]["number"] > 0:
                    if equipment_name in on_chain_items:
                        nft_id = player.nft_inventory[equipment_name].get("nft_id")
                        nft_data = query_nft_data(nft_id)
                        current_enhancement = nft_data["in-game-attributes"]["enhancement"].get("value")
                        current_owner = nft_data.get("in-game owner")
                        if current_owner == str(player_name):
                            # update player db 20221118
                            player.get_item("Refining Stone", -1)
                            chance = (0.95 ** current_enhancement) * 100
                            success = random.choices([True, False], weights=(chance, 100 - chance), k=1)[0]
                            if success:
                                enhance_nft(nft_id)
                                log = "You successfully enhanced " + str(equipment_name)
                            else:
                                log = "You failed to enhance " + str(equipment_name)

                        elif current_owner is None:
                            change_nft_owner(nft_id, player_name)
                            log = "You become the owner of " + str(equipment_name)

                        else:
                            transfer_price = current_enhancement * (current_enhancement + 21) / 2
                            wallet = player.coin
                            if wallet >= transfer_price:
                                change_nft_owner(nft_id, player_name)
                                player.earn_coin(-transfer_price)
                                log = "You paid " + str(transfer_price) + " CC to change the ownership of " + str(
                                    equipment_name)
                            else:
                                log = str(equipment_name) + "is not belong to you!"
                                log += "you need " + str(transfer_price) + " CC to change the ownership."

                    else:
                        log = "You don't have " + str(equipment_name)
                else:
                    log = "You don't have Refining Stone!"
            else:
                log = "You don't have Refining Stone!"
        elif equipment_name in in_game_items:
            item_data = query_item_data(equipment_name)
            item_function = item_data.get("function")
            if item_function == "equipment":
                enhance_material = item_data.get("enhance-material")
                if enhance_material is not None:
                    check_material = True
                    log = f"You need following materials to enhance {equipment_name}:"
                    for material in enhance_material:
                        number_required = item_data["enhance-material"].get(material)
                        log += f"\n{material}: {str(number_required)}"
                        if material in player.inventory:
                            number_in_inventory = player.inventory[material].get("number")
                            if number_in_inventory < number_required:
                                check_material = False
                        else:
                            check_material = False
                    if check_material is True:
                        enhancement = player.inventory[equipment_name]["in-game-attributes"].get("enhancement")
                        if enhancement is None:
                            field = f"Assets.Inventory.Items.{equipment_name}.in-game-attributes.enhancement"
                            update = item_data["in-game-attributes"].get("enhancement")
                            modify_player_data(player_name, field, update)
                            enhancement_level = 0
                            enhancement_limit = item_data["in-game-attributes"]["enhancement"].get("limit")
                        else:
                            enhancement_level = enhancement.get("value")
                            enhancement_limit = enhancement.get("limit")
                        if enhancement_limit > enhancement_level:
                            for material in enhance_material:
                                number_required = item_data["enhance-material"].get(material)
                                player.get_item(material, -number_required)
                            update = enhancement_level + 1
                            field = f"Assets.Inventory.Items.{equipment_name}.in-game-attributes.enhancement.value"
                            modify_player_data(player_name, field, update)
                            log = f"You successfully enhanced {equipment_name} to level {str(update)}!"
                        else:
                            log = f"You cannot enhance {equipment_name} for over {str(enhancement_limit)} times!"
                    else:
                        log = log
                else:
                    log = "This equipment cannot be enhanced!"
            else:
                log = "This is not an equipment!"
        else:
            log = f"You don't have {equipment_name}!"
        now = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
        await system_channel.send(yaml(str(now) + ": " + str(player_name) + " enhanced " + str(equipment_name) + "."))
        await ctx.reply(yaml(log))

    @commands.command(pass_context=True,
                      brief='input !equip to add an NFT into equipment list.',
                      description='equip an NFT', aliases=["eq", "equipment"])
    async def equip(self, ctx, *, equipment_name=" "):
        player_name = str(ctx.message.author)
        system_channel = self.bot.get_channel(int(1023204349196906638))
        player = character(player_name)
        player.read_account()

        # search items in inventory
        in_game_items = player.inventory
        on_chain_items = player.nft_inventory

        all_items = {}
        for nft in on_chain_items:
            all_items[nft] = on_chain_items[nft]
        for item in in_game_items:
            all_items[item] = in_game_items[item]

        # update player's equipment db list before equip
        eq_list = ["Weapon", "Shield", "Hat",
                   "Necklace", "Shoulder", "Armor",
                   "Armbands", "Gloves", "Pants",
                   "Shoes", "Belt", "Cloak",
                   "Ring", "Mount", "Herb",
                   "Familiar", "Portrait", "Spirit"]

        # equip something
        if str(equipment_name) != " ":
            if len(all_items) > 0:
                if str(equipment_name) == "all":
                    await ctx.reply("You randomly equipped NFTs into blank slots.")
                    current_eq = player.equipment
                    for slot in current_eq:
                        if current_eq.get(slot) != "":
                            eq_list.remove(slot)

                    for i in all_items:
                        # determine item type
                        item_type = all_items[i].get("item_type")
                        item_type_cap = str(item_type.capitalize())
                        # equip
                        if str(item_type.capitalize()) in eq_list:
                            if i in on_chain_items:
                                nft_id = player.nft_inventory[equipment_name].get("nft_id")
                                nft_data = query_nft_data(nft_id)
                                current_owner = nft_data.get("in-game owner")
                                if current_owner is None:
                                    change_nft_owner(nft_id, player_name)
                                    if player["Status"]["Equipment"].get(item_type_cap) == "":
                                        modify_player_data(player_name, f"Status.Equipment.{item_type_cap}", str(i))
                                elif current_owner == str(player_name):
                                    if player["Status"]["Equipment"].get(item_type_cap) == "":
                                        modify_player_data(player_name, f"Status.Equipment.{item_type_cap}", str(i))
                                else:
                                    await ctx.reply(str(i) + " is not owned by you! Please equip it independently.")
                            else:
                                if player["Status"]["Equipment"].get(item_type_cap) == "":
                                    modify_player_data(player_name, f"Status.Equipment.{item_type_cap}", str(i))

                else:
                    if str(equipment_name) in all_items:
                        # determine item type
                        item_type = all_items[str(equipment_name)].get("item_type")
                        item_type_cap = str(item_type.capitalize())
                        print(item_type_cap)
                        # equip
                        if item_type_cap in eq_list:
                            if str(equipment_name) in on_chain_items:
                                nft_id = player.nft_inventory[equipment_name].get("nft_id")
                                nft_data = query_nft_data(nft_id)
                                current_enhancement = nft_data["in-game-attributes"]["enhancement"].get("value")
                                current_owner = nft_data.get("in-game owner")
                                if current_owner is None:
                                    change_nft_owner(nft_id, player_name)
                                    modify_player_data(player_name, f"Status.Equipment.{item_type_cap}",
                                                       str(equipment_name))

                                elif current_owner == str(player_name):
                                    print(f"Status.Equipment.{item_type_cap}")
                                    modify_player_data(player_name, f"Status.Equipment.{item_type_cap}",
                                                       str(equipment_name))

                                else:
                                    transfer_price = current_enhancement * (current_enhancement + 21) / 2
                                    wallet = player["Assets"].get("Wallet")
                                    if wallet >= transfer_price:
                                        change_nft_owner(nft_id, player_name)
                                        modify_player_data(player_name, "Status.Equipment.{item_type_cap}",
                                                           str(equipment_name))
                                        modify_player_wallet(player_name, -transfer_price)

                                        await ctx.reply("You paid " + str(
                                            transfer_price) + " to change the ownership and equip " + str(
                                            equipment_name))
                                    else:
                                        await ctx.reply(
                                            str(equipment_name) + " is not owned by you and you have no money to pay for ownership!")
                            else:
                                modify_player_data(player_name, f"Status.Equipment.{item_type_cap}",
                                                   str(equipment_name))
                                await ctx.reply("You equipped " + str(equipment_name))
                        else:
                            await ctx.reply(str(equipment_name) + " is not an equipment.")
                    else:
                        await ctx.reply("You don't have this NFT in inventory.")
            else:
                await ctx.reply("You have nothing in inventory.")
        else:
            await ctx.reply("If you want to equip NFT, find the nft_name in !inventory, then type !equip nft_name. ")

        log = ""
        player = get_player_data(player_name)
        for i in player["Status"]["Equipment"]:
            log += "\n" + str(i) + ": "
            log += player["Status"]["Equipment"][str(i)]

        embed = discord.Embed(
            title=str(player_name) + "'s Equipment",
            description=yaml(log)
        )
        now = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
        await system_channel.send(yaml(str(now) + ": " + player_name + " is checking equipment."))
        await ctx.reply(embed=embed)

    @commands.command(pass_context=True,
                      brief='input !attack to challenge a monster in current locality!',
                      description='attack a monster', aliases=["atk", "k", "hunt", "hun"])
    async def attack(self, ctx, *, monster_name=""):
        player_name = str(ctx.message.author)
        timestamp = int(time.time())
        now = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")

        # make the command case-insensitive
        if monster_name != "":
            args = monster_name.split()
            monster_name = ""
            for i in args:
                if i != "of" and i != "on" and i != "at" and i != "the":
                    monster_name += i.capitalize() + " "
                else:
                    monster_name += i + " "
            monster_name = monster_name.rstrip(monster_name[-1])

        # check adventurer role
        async def find_guild():
            for guild in self.bot.guilds:
                if guild.name == 'Chia Inventory':
                    return guild

        guild = await find_guild()
        roles = guild.get_member_named(player_name).roles
        adventurer = discord.utils.get(guild.roles, name="Adventurer")

        if adventurer in roles:
            player = get_player_data(player_name)

            # check tick
            latest_hunt = player["Status"]["Cool Down"].get("Latest Hunt")
            time_pass = timestamp - latest_hunt
            if time_pass > 2:
                modify_player_hunt_cd(player_name, timestamp)

                # load and check account
                stats = character(player_name)
                stats.read_account()
                remind = "Combat log shows up in hunting-ground channel by default! You can enter your favored channel and type !set_channel to setup where to output the combat log."

                # channel selector
                system_channel = self.bot.get_channel(int(1023204349196906638))
                inhibited_channels = []
                hunting_channels = ["⌨command-test", "🌳hunting-ground-1", "🐦hunting-ground-2", "🍌hunting-ground-3",
                                    "🍎hunting-ground-4",
                                    "🐇hunting-ground-5", "💀hunting-ground-6", "👿hunting-ground-7"]
                for channel in guild.channels:
                    if str(channel) not in hunting_channels:
                        inhibited_channels.append(str(channel))
                current_channel = str(ctx.channel)
                if current_channel not in inhibited_channels:
                    # search a monster
                    location = player["Status"].get('Location')
                    location = locate(str(location))
                    if len(location.enemies) != 0:
                        mobile_objects = open_mobile_object_db()
                        if monster_name == "":
                            monster = encounter(random.choice(location.enemies))
                            log = "You prepare to fight with " + add_red(str(monster.name)) + "!"

                        elif monster_name in location.enemies:
                            monster = encounter(monster_name)
                            log = "You prepare to fight with " + add_red(str(monster_name)) + "!"

                        if "monster" in locals():
                            # fight
                            combatlog, won = fight(player_name, stats, monster)
                            log += combatlog
                            if won:
                                here = get_player_location(player_name)
                                await kill_monster(here, str(monster.name))
                                message = player_name + " eliminated " + str(monster.name)
                            else:
                                message = str(monster.name) + " defeated " + player_name

                            if mobile_objects[str(monster.name)].get("portrait") is not None:
                                icon = mobile_objects[str(monster.name)].get("portrait")
                            else:
                                icon = ""
                            embed = discord.Embed(
                                title=player_name + "'s Combat Log",
                                description=remind + css(log)
                            )
                            embed.set_image(url=icon)
                            await system_channel.send(
                                yaml(str(now) + ": " + player_name + " challenged " + str(monster.name)))
                            await ctx.reply(
                                f"{ctx.message.author.mention}, your combat log is here.",
                                embed=embed)

                            # environmental message
                            player_list = get_player_list()
                            for player in player_list:
                                if player != player_name:
                                    location_name = get_player_location(player)
                                    if location_name == location.location:
                                        message_status = get_player_message_status(player)
                                        if message_status:
                                            try:
                                                receiver = guild.get_member_named(player)
                                                await receiver.send(yaml(message))
                                            except:
                                                print("Cannot contact " + str(player))
                        else:
                            await ctx.reply(f"{monster_name} is not here!")
                    else:
                        await ctx.reply("There is no monster in this location!")
                else:
                    await ctx.reply(
                        "You cannot hunt here..Please hunt in hunting ground channels or direct message with Mimic!")
            else:
                await ctx.reply("You need to wait for " + str(time_pass) + " seconds for next hunting!")
        else:
            await ctx.reply("You are not yet a adventurer!")


def fight(player_name, stats, monster):
    timestamp = str(time.time())
    combatlog = ""
    stamina_cost = 0
    won = False
    player = get_player_data(player_name)
    # assign attributes
    stats.check_equipment()
    stats.assign_attribute()

    assist_probability = 0
    assist_dd = 0

    if stats.familiar != "":
        if str(stats.familiar) in stats.nft_inventory:
            for i in stats.nft_inventory[str(stats.familiar)]:
                if type(stats.nft_inventory[str(stats.familiar)][i]) != str:
                    if stats.nft_inventory[str(stats.familiar)][i].get("type") == "assist_attack":
                        assist_probability = stats.nft_inventory[str(stats.familiar)][i].get(
                            "probability")
                        assist_dd = stats.nft_inventory[str(stats.familiar)][i].get("value")

        if str(stats.familiar) in stats.inventory:
            for i in stats.inventory[str(stats.familiar)]["in-game-attributes"]:
                if type(stats.inventory[str(stats.familiar)]["in-game-attributes"][i]) != str:
                    if stats.inventory[str(stats.familiar)]["in-game-attributes"][i].get(
                            "type") == "assist_attack":
                        assist_probability = stats.inventory[str(stats.familiar)]["in-game-attributes"][
                            i].get("probability")
                        assist_dd = stats.inventory[str(stats.familiar)]["in-game-attributes"][i].get(
                            "value")

    # start combat

    # check the requirement to attack monster
    if stats.life > 0:
        if stats.stamina >= 200:
            stamina_remain = stats.stamina
            while True:
                if stamina_remain >= attack_cost:
                    # Player's turn
                    # calculate best attack mode with luck factor
                    bestDD = [max(stats.slash - monster.DEFslash, 0), max(stats.bash - monster.DEFbash, 0),
                              max(stats.pierce - monster.DEFpierce, 0)]
                    luck_adjust = random.randint(int(max(bestDD)), int(max(bestDD)) * 2 + int(stats.luc / 10))
                    damage = luck_adjust + random.randint(1, max(1, int(stats.str / 5)))

                    # calculate attribute impacts
                    quick = random.choices([True, False], weights=(int(stats.dex), 70), k=1)[0]
                    smart = random.choices([True, False], weights=(int(stats.int), 70), k=1)[0]
                    wise = random.choices([True, False], weights=(int(stats.dex), 70), k=1)[0]
                    assist = random.choices([True, False], weights=(
                        int(assist_probability * 100), 100 - int(assist_probability * 100)), k=1)[0]

                    if assist:
                        combatlog += ("\n" +
                                      str(stats.familiar) + "  ⚔ ➜ " +
                                      str(monster.name) + " HP: " + str(round(monster.health, 1)) + " ➜" + str(
                                    round(monster.health - assist_dd, 1)))

                        monster.health = monster.health - assist_dd

                    # int effect
                    if smart:
                        magic_damage = random.randint(stats.magic + 1, stats.magic * 2 + 2)
                        combatlog += ("\n" +
                                      str(stats.name) + "  🪄️ ➜ " +
                                      str(monster.name) + " HP: " + str(round(monster.health, 1)) + " ➜" + str(
                                    round(monster.health - magic_damage, 1)))

                        monster.health = monster.health - magic_damage

                    # dex effect
                    if quick:
                        combatlog += ("\n" +
                                      str(stats.name) + "  ⚔️⚔️ ➜ " +
                                      str(monster.name) + " HP: " + str(round(monster.health, 1)) + " ➜" + str(
                                    round(monster.health - (damage * 2), 1)))
                        monster.health = monster.health - damage - damage
                        stamina_cost += attack_cost

                    else:
                        # wis effect
                        if wise:
                            bestDD = stats.slash + stats.bash + stats.pierce
                            luck_adjust = random.randint(max(1, int(bestDD)),
                                                         max(1, int(bestDD * 2 + int(stats.luc / 10))))
                            damage = luck_adjust + random.randint(1, max(1, int(stats.str / 5)))
                            combatlog += ("\n" +
                                          str(stats.name) + " 🧠⚔️ ➜ " +
                                          str(monster.name) + " HP: " + str(round(monster.health, 1)) + " ➜" + str(
                                        round(monster.health - damage, 1)))
                            monster.health = monster.health - damage
                            stamina_cost += attack_cost
                        else:
                            combatlog += ("\n" +
                                          str(stats.name) + "  ⚔️ ➜ " +
                                          str(monster.name) + " HP: " + str(round(monster.health, 1)) + " ➜" + str(
                                        round(monster.health - damage, 1)))
                            monster.health = monster.health - damage
                            stamina_cost += attack_cost

                    if monster.health <= 0:
                        combatlog += ("\n" +
                                      str(monster.name) + " ➜ 💀")
                        # distribute coins and exp
                        stats.coin += monster.coin
                        stats.earn_coin(monster.coin)
                        stats.earn_exp(monster.exp)
                        loot = "nothing"
                        loot_type = ""
                        if len(monster.loot) > 0:
                            loot_select = random.choice(monster.loot)
                            item_list = get_item_list()
                            if loot_select in item_list:
                                loot = loot_select
                                stats.get_item(loot, 1)
                                item_data = query_item_data(loot)
                                loot_type = item_data.get("icon")

                        stats.catch_monster(monster.name)
                        stamina_cost = round(stamina_cost)
                        stamina_left = stats.lost_stamina(stamina_cost)
                        combatlog += ("\n" + str(stats.name) + " lost " + str(
                            stamina_cost) + " stamina. (" + str(stamina_left) + " stamina left)")

                        combatlog += ("\n" + str(monster.coin) + " 🪙➜ " +
                                      str(stats.name))
                        combatlog += ("\n" + str(monster.exp) + " Exp➜ " +
                                      str(stats.name))
                        combatlog += ("\n" + "You found " + str(loot) + str(loot_type) + " from the corpse.")

                        won = True
                        print(str(stats.name) + " killed " + str(monster.name) + " lost " + str(
                            stamina_cost) + " stamina. (" + str(stamina_left) + " stamina left)")
                        return combatlog, won
                else:
                    combatlog += ("\n" + str(stats.name) + " requires additional 20 stamina to perform attack...")

                # Monster's turn
                # dex effect
                quick = random.choices([True, False], weights=(int(stats.dex), 70), k=1)[0]
                charming = random.choices([True, False], weights=(int(stats.cha), 70), k=1)[0]

                if quick:
                    combatlog += ("\n" +
                                  str(monster.name) + "  ⚔️ ➜ " + str(stats.name) + " 👟")
                    stamina_cost += evasion_cost
                else:
                    counter = max(1, random.randint(monster.attack,
                                                    max(1, int(monster.attack * 2 - int(
                                                        stats.luc / 10)))) - stats.defense - random.randint(
                        1, max(1, int(stats.con / 5))))
                    # cha effect
                    if charming:
                        combatlog += ("\n" +
                                      str(monster.name) + " ❓⚔️ ➜ " +
                                      str(monster.name) + " HP: " + str(round(monster.health, 1)) + " ➜" + str(
                                    round(monster.health - counter, 1))
                                      )
                        monster.health = monster.health - counter
                        stamina_cost += evasion_cost
                        if monster.health <= 0:
                            combatlog += ("\n" +
                                          str(monster.name) + " ➜ 💀")
                            # distribute coins and exp
                            stats.earn_coin(monster.coin)
                            stats.earn_exp(monster.exp)
                            loot = "nothing"
                            loot_type = ""
                            if len(monster.loot) > 0:
                                loot_select = random.choice(monster.loot)
                                item_list = get_item_list()
                                if loot_select in item_list:
                                    loot = loot_select
                                    stats.get_item(loot, 1)
                                    item_data = query_item_data(loot)
                                    loot_type = item_data.get("icon")

                            stats.catch_monster(monster.name)
                            stamina_cost = round(stamina_cost)
                            stamina_left = stats.lost_stamina(stamina_cost)
                            combatlog += ("\n" + str(stats.name) + " lost " + str(
                                stamina_cost) + " stamina. (" + str(
                                stamina_left) + " stamina left)")

                            combatlog += ("\n" + str(monster.coin) + " 🪙➜ " +
                                          str(stats.name))
                            combatlog += ("\n" + str(monster.exp) + " Exp➜ " +
                                          str(stats.name))
                            combatlog += ("\n" + "You found " + str(loot) + str(loot_type) + " from the corpse.")

                            won = True
                            print(str(stats.name) + " killed " + str(monster.name) + " lost " + str(
                                stamina_cost) + " stamina. (" + str(stamina_left) + " stamina left)")
                            return combatlog, won
                    else:
                        combatlog += ("\n" +
                                      str(monster.name) + "  ⚔️ ➜ " +
                                      str(stats.name) + " HP: " + str(round(stats.health, 1)) + " ➜" + str(
                                    round(stats.health - counter, 1))
                                      )
                        stats.health = stats.health - counter
                        stamina_cost += hit_cost

                        # response after hit by monster
                        if stats.health <= 0:
                            if stamina_remain >= (escape_cost + stamina_cost):
                                combatlog += ("\n" + str(stats.name) + " ➜ 👟👟")
                                stamina_cost += escape_cost
                                break

                            else:
                                stats.die()
                                combatlog += ("\n" + str(stats.name) + " ➜ 💀")
                                print(str(stats.name) + " is killed by " + str(monster.name) + " and lost " + str(
                                    stamina_cost) + " stamina.")
                                break

            stamina_cost = round(stamina_cost)
            stamina_left = stats.lost_stamina(stamina_cost)
            combatlog += ("\n" + str(stats.name) + " lost " + str(
                stamina_cost) + " stamina. (" + str(stamina_left) + " stamina left)")

            return combatlog, won

        else:
            combatlog = "\n" + "For your safety, you need to keep at least 200 stamina for hunting..."
            return combatlog, won

    else:
        life_count = 180 - stats.life_count
        combatlog = "\n" + "You lay on the ground and dreamed about your adventure... hopefully the goddess of Chiania can revive you. You start to pray, [you hear a voice]: " + str(
            life_count) + ' minutes left...'
        return combatlog, won


def yaml(log):
    output = "\n" + "```yaml" + "\n" + log + "```"
    return output


def css(log):
    output = "\n" + "```css" + "\n" + log + "```"
    return output


def add_red(text):
    text = "[" + text + "]"
    return text


async def setup(bot):
    await bot.add_cog(Combat(bot))
