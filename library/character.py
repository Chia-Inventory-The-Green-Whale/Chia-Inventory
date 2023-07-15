import os
import time
from library.mongo import *
from library.mobile_object import *
from library.locations import *
import urllib3
from bs4 import BeautifulSoup
from subprocess import Popen, PIPE, run, list2cmdline

http = urllib3.PoolManager()


class character:
    def __init__(self, name):
        self.name = name
        # address
        self.address = ""
        self.reward_address = ""
        # status
        self.exp = 0
        self.life = 1
        self.stamina = 0
        self.mount_stamina = 0
        self.drunk = 0
        self.life_count = 0
        self.location = ""
        self.channel = ""
        self.cool_down = {
            "latest_withdraw": 0,
            "latest_hunt": 0
        }
        self.production = 0
        self.home = ""
        self.buff = {}
        self.home_stay = 0
        self.reforge_penalty = {}
        self.equipment = {
            "Weapon": "",
            "Shield": "",
            "Hat": "",
            "Necklace": "",
            "Shoulder": "",
            "Armor": "",
            "Armbands": "",
            "Gloves": "",
            "Pants": "",
            "Shoes": "",
            "Belt": "",
            "Cloak": "",
            "Ring": "",
            "Mount": "",
            "Herb": "",
            "Familiar": "",
            "Portrait": "",
            "Spirit": ""
        }
        self.message = False
        # class

        # combat
        self.health = 20
        self.slash = 0
        self.bash = 0
        self.pierce = 0
        self.magic = 0
        self.defense = 0
        self.weapon = ""
        self.shield = ""
        self.armor = ""
        self.mount = ""
        self.ring = ""
        self.herb = ""
        self.familiar = ""
        self.portrait = ""
        self.spirit = ""
        # combat temporary
        self.player_exp = 0
        self.next_exp = 0
        self.level = 0
        self.str = 10 + random.randint(1, 5)
        self.dex = 10 + random.randint(1, 5)
        self.con = 10 + random.randint(1, 5)
        self.int = 10 + random.randint(1, 5)
        self.wis = 10 + random.randint(1, 5)
        self.cha = 10 + random.randint(1, 5)
        self.luc = 10 + random.randint(1, 5)

        # assets
        self.coin = 0
        self.reputation = 0
        self.lands = 0
        self.structures = 0
        self.inventory = {}
        self.nft_inventory = {}

    def read_account(self):
        # read db
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["players"]
        target = {"Name": str(self.name)}
        player_data = collection.find_one(target)
        if player_data is not None:
            # latest login
            timestamp = int(time.time())
            self.latest_command = player_data["Status"].get("Latest Command")
            time_pass = timestamp - self.latest_command
            print(f"player {self.name} has taken a rest for {time_pass} seconds")
            player_data["Status"]["Latest Command"] = timestamp

            # charge
            # produce items
            player_data["Status"]["Production"] += int(time_pass / 60)
            production = int(player_data["Status"]["Production"] / 720)
            left = player_data["Status"]["Production"] % 720
            player_data["Status"]["Production"] = left
            count = 0
            for key in player_data["Assets"]["Inventory"]["NFTs"]:
                if count <= 7:
                    if type(player_data["Assets"]["Inventory"]["NFTs"][key]) != str:
                        for attribute in player_data["Assets"]["Inventory"]["NFTs"][key]:
                            if type(player_data["Assets"]["Inventory"]["NFTs"][key][attribute]) != str:
                                if player_data["Assets"]["Inventory"]["NFTs"][key][attribute].get(
                                        "type") == "produce_item":
                                    number = player_data["Assets"]["Inventory"]["NFTs"][key][attribute].get(
                                        "value")
                                    item = player_data["Assets"]["Inventory"]["NFTs"][key][attribute].get(
                                        "factor")
                                    if player_data["Assets"]["Inventory"]["Items"].get(item) is None:
                                        player_data["Assets"]["Inventory"]["Items"][item] = query_item_data(item)
                                        player_data["Assets"]["Inventory"]["Items"][item]["number"] = 0
                                    player_data["Assets"]["Inventory"]["Items"][item]["number"] += number * production
                                    count += 1

            # 20221219 added home_stay features
            home = player_data["Status"].get("Home")
            if player_data["Status"].get("Location") == home:
                home_stay = player_data["Status"].get("Home Stay")
                player_data["Status"]["Home Stay"] += int(time_pass / 60)
                if home in player_data["Assets"]["Inventory"].get("NFTs"):
                    buff_requirement = player_data["Assets"]["Inventory"]["NFTs"][home]["0"].get("buff_requirement")
                    if buff_requirement == "home_stay":
                        home_stay_requirement = player_data["Assets"]["Inventory"]["NFTs"][home]["0"].get("home_stay")
                        if home_stay >= home_stay_requirement:
                            home_stay_buff = {}
                            for j in player_data["Assets"]["Inventory"]["NFTs"][home]["0"]:
                                home_stay_buff[j] = player_data["Assets"]["Inventory"]["NFTs"][home]["0"][j]
                                player_data["Status"]["Buff"]["home stay butt"] = home_stay_buff
            else:
                player_data["Status"]["Home Stay"] = 0

            # 20221219 added check buff cd
            if len(player_data["Status"]["Buff"]) > 0:
                for buff in player_data["Status"]["Buff"].copy():
                    player_data["Status"]["Buff"][buff]["buff_duration"] -= int(time_pass / 60)
                    if player_data["Status"]["Buff"][buff]["buff_duration"] < 1:
                        player_data["Status"]["Buff"].pop(buff)

            # city or wild
            locations = open_locations_db()
            if player_data["Status"]['Location'] not in locations:
                player_data["Status"]['Location'] = "Tavern"
                location = locate("Tavern")
            else:
                location = locate(player_data["Status"].get('Location'))
            area_type = location.area_type

            # drunk effect
            if location.name == "Tavern" or location.name == player_data["Status"].get("Home"):
                if int(time_pass / 60) >= player_data["Status"]['Drunk']:
                    drunk_duration = player_data["Status"]['Drunk']
                    player_data["Status"]['Drunk'] = 0
                else:
                    drunk_duration = int(time_pass / 60)
                    player_data["Status"]['Drunk'] -= int(time_pass / 60)
                player_data["Status"]['Stamina'] += 0.2 * drunk_duration
            if player_data["Status"]['Drunk'] > 1440:
                player_data["Status"]['Drunk'] = 1440

            # charge stamina
            if area_type == "Home" and player_data["Status"]['Stamina'] < home_max_stamina:
                player_data["Status"]['Stamina'] += city_charge * int(time_pass / 60)
                if player_data["Status"]['Stamina'] > home_max_stamina:
                    player_data["Status"]['Stamina'] = home_max_stamina
            if area_type == "City" and player_data["Status"]['Stamina'] < city_max_stamina:
                player_data["Status"]['Stamina'] += city_charge * int(time_pass / 60)
                if player_data["Status"]['Stamina'] > city_max_stamina:
                    player_data["Status"]['Stamina'] = city_max_stamina
            if area_type in ["Desert", "Rainforest", "Taiga", "Deciduous Forest", "Grassland", "Savanna",
                             "Tundra"]:
                area_type = "Wild"
            if area_type == "Wild" and player_data["Status"]['Stamina'] < wild_max_stamina:
                player_data["Status"]['Stamina'] += wild_charge * int(time_pass / 60)
                if player_data["Status"]['Stamina'] > wild_max_stamina:
                    player_data["Status"]['Stamina'] = wild_max_stamina
            if player_data["Status"]['Stamina'] < 0:
                player_data["Status"]['Stamina'] = 0
            player_data["Status"]['Stamina'] = round(player_data["Status"]['Stamina'], 1)

            # check mount
            if player_data["Status"].get("Equipment") is not None:
                mount = player_data["Status"]["Equipment"].get("Mount")
                if mount != "":
                    if player_data["Status"].get("Mount Stamina") is None:
                        player_data["Status"]["Mount Stamina"] = 0
                    else:
                        if player_data["Status"]["Mount Stamina"] < 100:
                            player_data["Status"]["Mount Stamina"] += int(time_pass / 60)
                            if player_data["Status"]["Mount Stamina"] > 100:
                                player_data["Status"]["Mount Stamina"] = 100

            # quest cd
            for j in player_data["Quests"]:
                if player_data["Quests"][j]["cd"] > 0:
                    player_data["Quests"][j]["cd"] -= int(time_pass / 60)
                    if player_data["Quests"][j]["cd"] < 0:
                        player_data["Quests"][j]["cd"] = 0

            # revive
            if player_data["Status"]['Life'] != 1:
                life_count = player_data["Status"].get('Life_count')
                if life_count < 180:
                    player_data["Status"]['Life_count'] += int(time_pass / 60)
                if player_data["Status"]['Life_count'] >= 180:
                    player_data["Status"]['Life_count'] = 0
                    player_data["Status"]['Life'] = 1

            # 2022/12/25 add world magic
            if player_data["Status"].get("World Magic") is None:
                player_data["Status"]["World Magic"] = {}
                player_data["Status"]["World Magic"]["goblinization"] = False
                player_data["Status"]["World Magic"]["2022"] = False

            # dump database
            save_player_db(self.name, player_data)

            # read address
            self.address = str(player_data["Address"].get("DID"))
            self.reward_address = str(player_data["Address"].get("Reward Address"))

            # read status
            self.exp = player_data["Status"].get("Exp")
            lv, player_exp, next_exp = level(self.exp)
            self.level = lv
            self.player_exp = player_exp
            self.next_exp = next_exp
            self.health += int(lv / 2)
            self.life = player_data["Status"].get("Life")
            self.stamina = player_data["Status"].get("Stamina")
            self.mount_stamina = player_data["Status"].get("Mount Stamina")
            self.drunk = player_data["Status"].get("Drunk")
            self.life_count = player_data["Status"].get("Life_count")
            self.location = player_data["Status"].get("Location")
            self.channel = player_data["Status"].get("Channel")
            self.cool_down = player_data["Status"].get("Cool Down")
            self.production = player_data["Status"].get("Production")
            self.home = player_data["Status"].get("Home")
            if self.home is None:
                self.home = "Tavern"
            self.buff = player_data["Status"].get("Buff")
            self.home_stay = player_data["Status"].get("Home Stay")
            self.reforge_penalty = player_data["Status"].get("Reforge Penalty")
            self.equipment = player_data["Status"].get("Equipment")
            self.weapon = player_data["Status"]["Equipment"].get("Weapon")
            self.shield = player_data["Status"]["Equipment"].get("Shield")
            self.hat = player_data["Status"]["Equipment"].get("Hat")
            self.necklace = player_data["Status"]["Equipment"].get("Necklace")
            self.shoulder = player_data["Status"]["Equipment"].get("Shoulder")
            self.armor = player_data["Status"]["Equipment"].get("Armor")
            self.armbands = player_data["Status"]["Equipment"].get("Armbands")
            self.gloves = player_data["Status"]["Equipment"].get("Gloves")
            self.pants = player_data["Status"]["Equipment"].get("Pants")
            self.shoes = player_data["Status"]["Equipment"].get("Shoes")
            self.belt = player_data["Status"]["Equipment"].get("Belt")
            self.cloak = player_data["Status"]["Equipment"].get("Cloak")
            self.mount = player_data["Status"]["Equipment"].get("Mount")
            self.ring = player_data["Status"]["Equipment"].get("Ring")
            self.herb = player_data["Status"]["Equipment"].get("Herb")
            self.familiar = player_data["Status"]["Equipment"].get("Familiar")
            self.portrait = player_data["Status"]["Equipment"].get("Portrait")
            self.spirit = player_data["Status"]["Equipment"].get("Spirit")
            self.message = player_data["Status"].get("Message")
            self.quests = player_data.get("Quests")
            self.latest_nft_update = player_data["Status"].get("Latest NFT Update")
            if self.latest_nft_update is None:
                modify_player_data(str(self.name), "Status.Latest NFT Update", timestamp)
                self.latest_nft_update = timestamp

            # read assets
            self.coin = player_data["Assets"].get("Wallet")
            self.reputation = player_data["Assets"].get('Reputation')
            self.manor = player_data["Assets"].get("Manor")
            if self.manor is not None:
                self.manor_center = self.manor.get("center")
                self.lands = player_data["Assets"]["Manor"].get("lands")

                if self.lands is not None:
                    self.lands_number = len(self.lands)
                else:
                    self.lands = []
                    self.lands_number = 0
                if player_data["Assets"]["Manor"].get("constructions") is not None:
                    self.constructions = list(player_data["Assets"]["Manor"].get("constructions").keys())
                    self.constructions_number = len(self.constructions)
                else:
                    self.constructions = []
                    self.constructions_number = 0
            else:
                self.manor_center = "Tavern"
                self.lands = []
                self.lands_number = 0
                self.constructions = []
                self.constructions_number = 0
            self.inventory = player_data["Assets"]["Inventory"].get("Items")
            self.nft_inventory = player_data["Assets"]["Inventory"].get("NFTs")
            self.catch = player_data["Assets"].get("Catch")

            # world magic
            self.goblinization = player_data["Status"]["World Magic"].get("goblinization")
            self._2022_ = player_data["Status"]["World Magic"].get("2022")

            return True
        else:
            return False

    def switch_environment_message(self):
        if self.message == False:
            modify_player_data(self.name, "Status.Message", True)
            log = "You turned on the enviornmental message!"
        else:
            modify_player_data(self.name, "Status.Message", False)
            log = "You turned off the enviornmental message!"
        return log

    def find_address(self):
        http = urllib3.PoolManager()
        url = f'https://api.mintgarden.io/profile/{self.address}/nfts?type=owned'
        response = http.request('GET', url)
        soup = BeautifulSoup(response.data, features="html.parser")
        inventory = json.loads(soup.text)
        address_list = []
        items = inventory.get("items")
        if inventory.get("items") != None:
            if len(items) > 0:
                for i in range(0, len(items)):
                    address_list.append(items[i]['owner_address_encoded_id'])
                reward_address = random.choice(address_list)
                field = "Address.Reward Address"
                modify_player_data(self.name, field, str(reward_address))
                log = "Found and applied a wallet address: " + str(reward_address)
            else:
                log = "You don't have any NFT in DID, no way to find an address..."
        else:
            log = "You don't have any NFT in DID, no way to find an address..."
        return log

    def cast_world_magic(self, magic_name):
        def magic_source(spell):
            magic_list = os.listdir("./magic/" + str(spell))
            charge = len(magic_list)
            return magic_list, charge

        def show_nft_nid(fingerprint, id):
            response = run(["chia", "wallet", "nft", "list", "-f {}".format(fingerprint), "-i {}".format(id)],
                           capture_output=True)
            response = str(response)
            response = response.split('Current NFT coin ID:       ')
            response = response[1:]
            for i in range(len(response)):
                response[i] = response[i][0:64]
            return response

        def send_nft(fingerprint, id, ni, ta):
            response = run(["chia",
                            "wallet",
                            "nft",
                            "transfer",
                            "-f", str(fingerprint),
                            "-i", str(id),
                            "-ni", str(ni),
                            "-ta", str(ta),
                            "-m", "0.0000001"],
                           capture_output=True)
            print("the commandline is {}".format(list2cmdline(response.args)))
            print(response)
            return response

        log = ""
        magic_choose = ""
        if magic_name == "goblinization":
            magic_list, charge = magic_source("goblinization")
            if charge > 0:
                if self.goblinization == False:
                    magic_choose = "./magic/goblinization/" + random.choice(magic_list)
                    modify_player_data(self.name, "Status.World Magic.goblinization", True)
                    log = "You have been GOBLINIZED!"
                else:
                    log = "You are already transformed to a goblin!"
            else:
                log = "No mana to cast this spell! Please ask the magician to charge."
        elif magic_name == "2022":
            magic_list = show_nft_nid(2990254927, 3)
            if len(magic_list) > 0:
                if self.reward_address is not None and self.reward_address != "":
                    if self._2022_ == False:
                        magic_choose = random.choice(magic_list)
                        modify_player_data(self.name, "Status.World Magic.2022", True)
                        send_nft(2990254927, 3, magic_choose, self.reward_address)
                        log = "A Chia Inventory 2022 NFT has been sent to your wallet!"
                    else:
                        log = "You already have a Chia Inventory 2022 NFT!"
                else:
                    log = "You need a reward address to receive this magic."
            else:
                log = "No mana to cast this spell! Please ask the magician to charge."

        return magic_choose, log

    def nft_sync(self):
        # latest nft db update
        timestamp = int(time.time())
        latest_nft_update = self.latest_nft_update
        time_pass = timestamp - latest_nft_update
        if time_pass > 300:
            modify_player_data(str(self.name), "Status.Latest NFT Update", timestamp)
            player_name = self.name
            print("Checking " + str(player_name) + "'s NFT")
            http = urllib3.PoolManager()
            address = self.address
            url = 'https://api.mintgarden.io/profile/' + address + '/nfts?type=owned&size=100'
            response = http.request('GET', url)
            soup = BeautifulSoup(response.data, features="html.parser")
            nft_inventory = json.loads(soup.text)
            update = {}
            before = self.nft_inventory
            if nft_inventory.get("items") is not None:
                print("got something from Mintgarden")
                for nft in range(0, len(nft_inventory["items"])):
                    nft_id = nft_inventory["items"][nft]["encoded_id"]
                    nft_list = get_nft_list()
                    if nft_id in nft_list:
                        nft_data = query_nft_data(nft_id)
                        item_name = nft_inventory["items"][nft]['name']
                        print(f"detect CI item: {str(nft_id)} = {item_name}")
                        update[item_name] = nft_data["in-game-attributes"]
                        update[item_name]["nft_id"] = nft_id
                        update[item_name]["item_type"] = nft_data["item_type"]
                        update[item_name]["icon"] = nft_data["icon"]
                        update[item_name]["portrait"] = nft_data["portrait"]
                    else:
                        print("non-CI item: " + str(nft_id))

            if before != update:
                log = "NFT inventory has been updated."
                modify_player_data(player_name, "Assets.Inventory.NFTs", update)
                print(str(player_name) + ": " + str(before) + " update as " + str(update))
            else:
                log = "NFT inventory has no change..."
        else:
            wait = 300 - time_pass
            log = f"You still need to wait for {wait} seconds to update NFT inventory..."

        return log

    def recover_stamina(self, amount):
        if amount is not None:
            client = pymongo.MongoClient()
            db = client["Chiania"]
            collection = db["players"]
            target = {"Name": str(self.name)}
            player_data = collection.find_one(target)
            player_data["Status"]["Stamina"] += amount
            update = player_data["Status"]["Stamina"]
            field = "Status.Stamina"
            collection.update_one(target, {"$set": {field: update}})

    def get_drunk(self, amount):
        if amount is not None:
            client = pymongo.MongoClient()
            db = client["Chiania"]
            collection = db["players"]
            target = {"Name": str(self.name)}
            player_data = collection.find_one(target)
            player_data["Status"]["Drunk"] += amount
            update = player_data["Status"]["Drunk"]
            field = "Status.Drunk"
            collection.update_one(target, {"$set": {field: update}})

    def earn_coin(self, amount):
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["players"]
        target = {"Name": str(self.name)}
        player_data = collection.find_one(target)
        player_data["Assets"]["Wallet"] += amount
        update = player_data["Assets"]["Wallet"]
        field = "Assets.Wallet"
        collection.update_one(target, {"$set": {field: update}})

    def earn_reputation(self, amount):
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["players"]
        target = {"Name": str(self.name)}
        player_data = collection.find_one(target)
        player_data["Assets"]["Reputation"] += amount
        update = player_data["Assets"]["Reputation"]
        field = "Assets.Reputation"
        collection.update_one(target, {"$set": {field: update}})

    def earn_exp(self, amount):
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["players"]
        target = {"Name": str(self.name)}
        player_data = collection.find_one(target)
        player_data["Status"]["Exp"] += amount
        update = player_data["Status"]["Exp"]
        field = "Status.Exp"
        collection.update_one(target, {"$set": {field: update}})

    def lost_stamina(self, amount):
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["players"]
        target = {"Name": str(self.name)}
        player_data = collection.find_one(target)
        player_data["Status"]["Stamina"] -= amount
        update = player_data["Status"]["Stamina"]
        field = "Status.Stamina"
        collection.update_one(target, {"$set": {field: update}})
        stamina_left = player_data["Status"]["Stamina"]
        return stamina_left

    def lost_mount_stamina(self, amount):
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["players"]
        target = {"Name": str(self.name)}
        player_data = collection.find_one(target)
        player_data["Status"]["Mount Stamina"] -= amount
        update = player_data["Status"]["Mount Stamina"]
        field = "Status.Mount Stamina"
        collection.update_one(target, {"$set": {field: update}})
        mount_stamina_left = player_data["Status"]["Mount Stamina"]
        return mount_stamina_left

    def die(self):
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["players"]
        target = {"Name": str(self.name)}
        field = "Status.Life"
        collection.update_one(target, {"$set": {field: 0}})
        field = "Status.Life_count"
        collection.update_one(target, {"$set": {field: 0}})

    def get_item(self, item_name, number):
        item_name = str(item_name)
        item_attributes = query_item_data(item_name)
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["players"]
        target = {"Name": str(self.name)}
        player_data = collection.find_one(target)
        field = f"Assets.Inventory.Items.{item_name}"
        if item_name not in player_data["Assets"]["Inventory"]["Items"]:
            collection.update_one(target, {"$set": {field: item_attributes}})
            field = f"Assets.Inventory.Items.{item_name}.number"
            collection.update_one(target, {"$set": {field: number}})
        else:
            update = player_data["Assets"]["Inventory"]["Items"][item_name]["number"] + number
            field = f"Assets.Inventory.Items.{item_name}.number"
            collection.update_one(target, {"$set": {field: update}})

    def lost_item(self, item_name):
        item_name = str(item_name)
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["players"]
        target = {"Name": str(self.name)}
        player_data = collection.find_one(target)
        if item_name in player_data["Assets"]["Inventory"]["Items"]:
            update = player_data["Assets"]["Inventory"]["Items"][item_name]["number"] - 1
            field = f"Assets.Inventory.Items.{item_name}.number"
            collection.update_one(target, {"$set": {field: update}})

    def get_buff(self, buff_name, buff_attributes):
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["players"]
        target = {"Name": str(self.name)}
        field = f"Status.Buff.{buff_name}"
        update = buff_attributes
        collection.update_one(target, {"$set": {field: update}})

    def catch_monster(self, monster_name):
        monster_name = str(monster_name)
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["players"]
        target = {"Name": str(self.name)}
        player_data = collection.find_one(target)
        field = f"Assets.Catch.{monster_name}"
        if monster_name not in player_data["Assets"]["Catch"]:
            collection.update_one(target, {"$set": {field: 1}})
        else:
            update = player_data["Assets"]["Catch"][monster_name] + 1
            field = f"Assets.Catch.{monster_name}"
            collection.update_one(target, {"$set": {field: update}})

    def get_reward_address(self):
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["players"]
        target = {"Name": str(self.name)}
        player_data = collection.find_one(target)
        self.address = player_data["Address"].get("DID")
        http = urllib3.PoolManager()
        url = 'https://api.mintgarden.io/profile/' + self.address + '/nfts?type=owned'
        response = http.request('GET', url)
        soup = BeautifulSoup(response.data, features="html.parser")
        try:
            inventory = json.loads(soup.text)
            address_list = []
            for i in range(0, len(inventory["items"])):
                address_list.append(inventory["items"][i]['owner_address_encoded_id'])
            reward_address = random.choice(address_list)
            self.reward_address = reward_address
            update = reward_address
        except:
            update = ""
        modify_player_data(str(self.name), "Address.Reward Address", update)

    def who_is_here(self):
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["players"]
        target = {"Status.Location": str(self.location)}
        players = collection.find(target)
        player_list = []
        for player in players:
            if player != self.name:
                player_list.append(player["Name"])
        return self.location, player_list

    def look(self, target):
        account = self.read_account()
        output = {}
        if account is True:
            locations = open_locations_db()
            mobile_objects = open_mobile_object_db()
            location = locate(self.location)
            log = ""
            # check drunk
            drunk_bonus = 0
            if self.drunk > 0:
                if self.location == "Tavern" or self.location == self.home:
                    drunk_bonus = 0.2
            area_type = location.area_type
            current_location, player_here = self.who_is_here()
            monster_list = location.visible_object
            icon = ""
            portrait = ""
            constructions = ""
            exits = ""
            mobs = ""
            items = ""
            if target is None:
                target_type = "Location"
                log += "\n" + "Area Type: " + str(area_type)
                if location.area_type in wild_list:
                    log += "\n" + "Current/Maximum Stamina: " + str(self.stamina) + "/" + str(
                        wild_max_stamina) + ", Stamina Restore: " + str(wild_charge) + "/min"
                if location.area_type == "City":
                    log += "\n" + "Current/Maximum Stamina: " + str(self.stamina) + "/" + str(
                        city_max_stamina) + ", Stamina Restore: " + str(city_charge + drunk_bonus) + "/min"
                if location.area_type == "Home":
                    log += "\n" + "Current/Maximum Stamina: " + str(self.stamina) + "/" + str(
                        home_max_stamina) + ", Stamina Restore: " + str(city_charge + drunk_bonus) + "/min"
                log += "\n" + "Mount Stamina: " + str(self.mount_stamina)
                if location.description != "":
                    log += "\n" + "Description: " + str(location.description)
                if len(player_here) > 0:
                    log += "\n" + "Adventurers: "
                    log += str(len(player_here)) + "  (type !who to see details)"
                if len(monster_list) > 0:
                    for i in monster_list:
                        mobs += i
                        if i in mobile_objects:
                            icon = mobile_objects[str(i)].get("icon")
                        else:
                            icon = ""
                        mobs += icon
                        mobs += " "
                if len(location.construction) > 0:
                    for i in location.construction:
                        constructions += "\n" + str(i) + " "

                if len(location.ground) > 0:
                    items_on_the_ground = {}
                    for i in location.ground:
                        if i not in items_on_the_ground:
                            items_on_the_ground[i] = 1
                        else:
                            items_on_the_ground[i] += 1
                    for i in items_on_the_ground:
                        items += f"{str(i)}({str(items_on_the_ground[i])})  "

                if len(location.exits) > 0:
                    exits += str(location.exits)

                else:
                    if location.explore != True:
                        structure_exits = list(location.construction.keys())
                        if len(structure_exits) == 0:
                            exits += "\n" + "Perception: There are no obvious exits in this location. You need to !explore and find out where to go!"

                    else:
                        exit = locations[str(location.id)].get("exit")
                        exits += "\n" + "Perception: You have explored this area, and it seems you can leave this place through the hidden path " + str(
                            exit)

                icon = location.icon
                portrait = location.portrait
                target_name = location.name

            elif str(target) in location.construction:
                target_type = "Structure"
                icon = location.construction[str(target)].get("icon")
                portrait = location.construction[str(target)].get("portrait")
                construction_type = location.construction[str(target)]["construction_type"]
                enter = location.construction[str(target)]["enter"]
                teleport = location.construction[str(target)]["teleport"]
                description = location.construction[str(target)]["description"]
                log = "Construction Type: " + str(construction_type)
                log += "\n" + "Enter: " + str(enter)
                log += "\n" + "You are looking at " + str(target)
                log += "\n" + description

                target_name = str(target)

            elif str(target) in monster_list:
                target_type = "Monster"
                monster_name = str(target)
                monster_name = str(mobile_objects[str(monster_name)]["name"])
                monster_type = str(mobile_objects[str(monster_name)]["type"])
                monster_health = mobile_objects[str(monster_name)]["health"]
                monster_attack = mobile_objects[str(monster_name)]["attack"]
                monster_DEFslash = mobile_objects[str(monster_name)]["slash_defense"]
                monster_DEFbash = mobile_objects[str(monster_name)]["bash_defense"]
                monster_DEFpierce = mobile_objects[str(monster_name)]["pierce_defense"]
                monster_loot = mobile_objects[str(monster_name)]["loot"]
                monster_description = mobile_objects[str(monster_name)]["description"]
                monster_author = mobile_objects[str(monster_name)]["author"]
                monster_aggression = mobile_objects[str(monster_name)]["aggression"]
                monster_category = mobile_objects[str(monster_name)]["category"]
                log += "\n" + "Attack: " + str(monster_attack) + "-" + str(int(monster_attack + monster_attack / 3))
                log += "\n" + "Health: " + str(monster_health) + "-" + str(int(monster_health + monster_health / 3))
                log += "\n" + "Slash Defense: " + str(monster_DEFslash)
                log += "\n" + "Bash Defense: " + str(monster_DEFbash)
                log += "\n" + "Pierce Defense: " + str(monster_DEFpierce)
                log += "\n" + "Category: " + str(monster_category)
                log += "\n" + "Aggression: " + str(monster_aggression)
                log += "\n" + "Description: " + str(monster_description)
                log += "\n" + "Author: " + str(monster_author)
                icon = mobile_objects[str(monster_name)].get("icon")
                portrait = mobile_objects[str(monster_name)].get("portrait")
                target_name = str(target)

            elif str(target) in self.inventory:
                target_type = "Item"
                item_name = str(target)
                item_data = self.inventory.get(item_name)
                item_type = item_data.get("item_type")
                icon = item_data.get("icon")
                portrait = item_data.get("portrait")
                item_function = item_data.get("function")
                log = "\n" + "Item type: " + str(item_type)
                log += "\n" + "Item function: " + str(item_function)
                if item_function == "equipment":
                    log += "\n" + "Attributes:"
                    item_attributes = item_data.get("in-game-attributes")
                    count = 0
                    for i in item_attributes:
                        count += 1
                        log += "\n" + str(count) + ": " + str(item_attributes[i].get("type")) + "(" + str(
                            item_attributes[i].get("factor")) + ") = " + str(item_attributes[i].get("value"))
                target_name = str(target)

            elif str(target) in self.nft_inventory:
                target_type = "NFT"
                item_name = str(target)
                nft_id = self.nft_inventory[item_name].get("nft_id")
                nft_data = query_nft_data(nft_id)
                item_type = nft_data.get("item_type")
                icon = nft_data.get("icon")
                portrait = nft_data.get("portrait")
                item_attributes = nft_data.get("in-game-attributes")
                log = "\n" + "Item type: " + str(item_type)
                log += "\n" + "Attributes:"
                count = 0
                for j in item_attributes:
                    count += 1
                    log += "\n" + str(count) + ": " + str(item_attributes[j]["type"]) + "(" + str(
                        item_attributes[j].get("factor")) + ") = " + str(item_attributes[j]["value"])

                target_name = item_name

            else:
                target_type = "None"
                icon = ""
                target_name = ""
                log = str(target) + " is not here."

            log = yaml(log)

            output["bool"] = True
            output["log"] = log
            output["icon"] = icon
            output["portrait"] = portrait
            output["target_name"] = target_name
            output["constructions"] = constructions
            output["exits"] = exits
            output["mobs"] = mobs
            output["target_type"] = target_type
            output["items"] = items
            return output
        else:
            output["bool"] = False
            output["log"] = "User name not exist!"
            return output

    # where am i ?
    def where(self):
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["players"]
        target = {"Name": str(self.name)}
        player_data = collection.find_one(target)
        here = player_data["Status"].get("Location")
        return here

    def change_home(self, new_home):
        modify_player_data(self.name, "Status.Home", new_home)

    # general command for movement
    def go(self, direction):
        direction = direction.lower()
        location = locate(self.location)
        old_location = new_location = location.name
        log = ""

        # construction name
        args = direction.split()
        construction_name = ""
        for i in args:
            if i != "of" and i != "on" and i != "at" and i != "the":
                construction_name += i.capitalize() + " "
            else:
                construction_name += i + " "
        construction_name = construction_name.rstrip(construction_name[-1])

        # instant move?
        instant = True
        if len(direction) == 1:
            instant = False
        for i in direction:
            if i not in ['e', 'w', 's', 'n']:
                instant = False

        # start from here
        if self.life > 0:
            if self.mount_stamina >= go_cost or self.stamina >= go_cost:
                locations = open_locations_db()
                if direction in ['east', 'west', 'south', 'north', 'e', 'w', 's', 'n']:
                    if direction == 'east' or direction == 'e':
                        if self.location == location.east:
                            log += "You can not go this direction!"
                        else:
                            modify_player_data(str(self.name), f"Status.Location", location.east)
                            new_location = locate(location.east).name
                            log += "You walk to " + new_location
                            if self.mount_stamina >= go_cost:
                                self.lost_mount_stamina(go_cost)
                            else:
                                self.lost_stamina(go_cost)
                    if direction == 'west' or direction == 'w':
                        if self.location == location.west:
                            log += "You can not go this direction!"
                        else:
                            modify_player_data(str(self.name), f"Status.Location", location.west)
                            new_location = locate(location.west).name
                            log += "You walk to " + new_location
                            if self.mount_stamina >= go_cost:
                                self.lost_mount_stamina(go_cost)
                            else:
                                self.lost_stamina(go_cost)
                    if direction == 'south' or direction == 's':
                        if self.location == location.south:
                            log += "You can not go this direction!"
                        else:
                            modify_player_data(str(self.name), f"Status.Location", location.south)
                            new_location = locate(location.south).name
                            log += "You walk to " + new_location
                            if self.mount_stamina >= go_cost:
                                self.lost_mount_stamina(go_cost)
                            else:
                                self.lost_stamina(go_cost)
                    if direction == 'north' or direction == 'n':
                        if self.location == location.north:
                            log += "You can not go this direction!"
                        else:
                            modify_player_data(str(self.name), f"Status.Location", location.north)
                            new_location = locate(location.north).name
                            log += "You walk to " + new_location
                            if self.mount_stamina >= go_cost:
                                self.lost_mount_stamina(go_cost)
                            else:
                                self.lost_stamina(go_cost)

                # instant move
                elif instant == True:
                    for i in direction:
                        here = self.where()
                        location = locate(here)
                        if i == 'e':
                            if here == location.east:
                                log += "\n" + "You can not go this direction!"
                            else:
                                modify_player_data(str(self.name), f"Status.Location", location.east)
                                location = locate(location.east)
                                new_location = location.name
                                log += "\n" + "You walk to " + new_location
                                if self.mount_stamina >= go_cost:
                                    self.mount_stamina -= go_cost
                                    self.lost_mount_stamina(go_cost)
                                else:
                                    self.lost_stamina(go_cost)
                        if i == 'w':
                            if here == location.west:
                                log += "\n" + "You can not go this direction!"
                            else:
                                modify_player_data(str(self.name), f"Status.Location", location.west)
                                location = locate(location.west)
                                new_location = location.name
                                log += "\n" + "You walk to " + new_location
                                if self.mount_stamina >= go_cost:
                                    self.mount_stamina -= go_cost
                                    self.lost_mount_stamina(go_cost)
                                else:
                                    self.lost_stamina(go_cost)
                        if i == 's':
                            if here == location.south:
                                log += "\n" + "You can not go this direction!"
                            else:
                                modify_player_data(str(self.name), f"Status.Location", location.south)
                                location = locate(location.south)
                                new_location = location.name
                                log += "\n" + "You walk to " + new_location
                                if self.mount_stamina >= go_cost:
                                    self.mount_stamina -= go_cost
                                    self.lost_mount_stamina(go_cost)
                                else:
                                    self.lost_stamina(go_cost)
                        if i == 'n':
                            if here == location.north:
                                log += "\n" + "You can not go this direction!"
                            else:
                                modify_player_data(str(self.name), f"Status.Location", location.north)
                                location = locate(location.north)
                                new_location = locate(location.north).name
                                log += "\n" + "You walk to " + new_location
                                if self.mount_stamina >= go_cost:
                                    self.mount_stamina -= go_cost
                                    self.lost_mount_stamina(go_cost)
                                else:
                                    self.lost_stamina(go_cost)

                # enter constructions
                elif construction_name in location.construction:
                    direction = construction_name
                    construction_type = location.construction[str(direction)].get("construction_type")
                    teleport = location.construction[str(direction)].get("teleport")

                    # if construction_type == "dungeon":
                    #    dungeon_type = teleport
                    #    new_dungeon = "Instance " + str(random.getrandbits(32))
                    #    create_dungeon(new_dungeon, dungeon_type)
                    #    modify_player_data(str(self.name), f"Status.Location", new_dungeon)
                    #    new_location = locate(new_dungeon).name
                    #    self.lost_stamina(go_cost)
                    #    log += f"You entered {new_location}"

                    # elif construction_type == "dungeon_door":
                    #    locations[str(location.id)]["dungeon_length"] -= 1
                    #    create_dungeon(str(location.id), str(location.name))
                    #    new_location = str(direction)
                    #    self.lost_stamina(go_cost)
                    #    log += "You moved to the next location through " + str(direction)

                    if construction_type == "accommodation":
                        modify_player_data(str(self.name), f"Status.Location", teleport)
                        new_location = str(direction)
                        log += "You entered " + str(direction)

                    elif construction_type == "door":
                        modify_player_data(str(self.name), f"Status.Location", teleport)
                        new_location = str(direction)
                        log += "You opened the door."

                    else:
                        log += "You cannot enter " + str(direction)
                else:
                    log += "You can not go this direction!"
            else:
                log += "You are too tired to walk..."
        else:
            life_count = 180 - self.life_count
            log += "You lay on the ground and dreamed about your adventure... hopefully the goddess of Chiania can revive you. You start to pray, [you hear a voice]: " + str(
                life_count) + ' minutes left...'

        return log, old_location, new_location

    # functions related to manor
    def teleport_to_home(self):
        locations = open_locations_db()
        if self.home not in locations:
            modify_player_data(str(self.name), f"Status.Home", "Tavern")
            log = "This house is not constructed yet, please !construct it in manor."
        else:
            if self.manor_center != "Tavern":
                if self.home in self.nft_inventory:
                    if self.home in self.constructions:
                        modify_player_data(str(self.name), f"Status.Location", self.home)
                        log = f"You teleported yourself to {self.home}."
                    else:
                        modify_player_data(str(self.name), f"Status.Location", self.manor_center)
                        log = "This house is not constructed yet, teleported to Manor."
                else:
                    modify_player_data(str(self.name), f"Status.Location", self.manor_center)
                    log = "You don't own the house, teleported to Manor."
            else:
                modify_player_data(str(self.name), f"Status.Location", "Tavern")
                log = "You don't have manor, teleported to Tavern."
        return log

        # functions related to manor

    def teleport(self, location):
        locations = open_locations_db()
        if location in locations:
            modify_player_data(str(self.name), f"Status.Location", location)
            log = f"You are teleported to {location}."
        else:
            log = f"There is no such a location."
        return log

    def leave_manor(self):
        if self.location in self.lands:
            modify_player_data(str(self.name), f"Status.Location", "Kingdom Street")
            log = "You leaved manor and walked to Kingdom Street."
        else:
            log = "You are not in manor."
        return log

    def reclaim_the_land(self, direction):
        locations = open_locations_db()
        if self.location in self.lands:
            if direction in ['east', 'west', 'south', 'north', 'e', 'w', 's', 'n']:
                barrier = True
                if direction in ["e", "east"]:
                    if locations[self.location]["east"] == self.location:
                        barrier = False
                elif direction in ["w", "west"]:
                    if locations[self.location]["west"] == self.location:
                        barrier = False
                elif direction in ["s", "south"]:
                    if locations[self.location]["south"] == self.location:
                        barrier = False
                elif direction in ["n", "north"]:
                    if locations[self.location]["north"] == self.location:
                        barrier = False

                if barrier == False:
                    reclaim_price = 200 * (1 + self.lands_number)
                    if self.coin > reclaim_price:
                        self.earn_coin(-reclaim_price)
                        new_room = str(random.getrandbits(32))
                        self.lands.append(new_room)
                        modify_player_data(str(self.name), f"Assets.Manor.lands", self.lands)
                        area_type = random.choice(
                            ["Desert", "Rainforest", "Taiga", "Deciduous Forest", "Grassland", "Savanna", "Tundra"])
                        style = str(random.randint(1, 4))
                        locations[new_room] = {}
                        locations[new_room]["area_type"] = area_type
                        locations[new_room]["climate"] = None
                        locations[new_room]["east"] = str(new_room)
                        locations[new_room]["west"] = str(new_room)
                        locations[new_room]["south"] = str(new_room)
                        locations[new_room]["north"] = str(new_room)
                        locations[new_room]["up"] = str(new_room)
                        locations[new_room]["down"] = str(new_room)
                        locations[new_room]["movement_type"] = None
                        locations[new_room]["monsters"] = []
                        locations[new_room]["monster_population"] = 0
                        locations[new_room]["constructions"] = {}
                        locations[new_room]["description"] = f"This is an undeveloped land of {self.name}"
                        locations[new_room]["visible_object"] = []
                        locations[new_room]["name"] = area_type
                        if area_type == "Deciduous Forest":
                            area_type = "Deciduous%20Forest"
                        locations[new_room][
                            "icon"] = "https://github.com/Chia-Inventory-The-Green-Whale/Chia-Inventory/blob/main/icons/" + area_type + style + ".jpg?raw=true"

                        if direction in ["e", "east"]:
                            locations[self.location]["east"] = new_room
                            locations[new_room]["west"] = self.location
                        if direction in ["w", "west"]:
                            locations[self.location]["west"] = new_room
                            locations[new_room]["east"] = self.location
                        if direction in ["s", "south"]:
                            locations[self.location]["south"] = new_room
                            locations[new_room]["north"] = self.location
                        if direction in ["n", "north"]:
                            locations[self.location]["north"] = new_room
                            locations[new_room]["south"] = self.location
                        save_location_db(locations)
                        log = f"You cost {str(reclaim_price)} to reclaim a new land."
                    else:
                        log = f"You need {str(reclaim_price)} coins to reclaim an additional land!"
                else:
                    log = "You can't reclaim a land in this direction!"
            else:
                log = "There is no such a direction."
        else:
            log = "You are not in manor."
        return log

    def construct(self, structure_name):
        home_list = []
        for construction in self.constructions:
            if construction[:12] == "Seasons Home":
                home_list.append(construction)
        home_number = len(home_list)

        if structure_name != "":
            if self.location in self.lands:
                if self.location != self.manor_center:
                    if structure_name in self.nft_inventory:
                        construction_type = self.nft_inventory[structure_name].get("item_type")
                        construction_list = ["house"]
                        if construction_type in construction_list:
                            locations = open_locations_db()
                            current_structures = locations[self.location].get("constructions")
                            if type(current_structures) != dict:
                                locations[self.location]["constructions"] = {}
                                current_structures = {}
                            if structure_name not in current_structures:
                                locations[self.location]["constructions"][structure_name] = {}
                                construction_price = 100 * (1 + home_number)
                                if self.coin > construction_price:
                                    self.earn_coin(-construction_price)

                                    # change ownership of nft
                                    nft_id = self.nft_inventory[structure_name].get("nft_id")
                                    nft_data = query_nft_data(nft_id)
                                    current_owner = nft_data.get("in-game owner")
                                    if current_owner == None:
                                        change_nft_owner(nft_id, self.name)
                                    else:
                                        current_owner_db = get_player_data(current_owner)
                                        check_current_owner = current_owner_db["Assets"]["Manor"]["constructions"].get(
                                            structure_name)
                                        if check_current_owner is not None:
                                            current_structure_location = \
                                                current_owner_db["Assets"]["Manor"]["constructions"][
                                                    structure_name].get(
                                                    "location")
                                            self.remove_a_construction(current_owner, structure_name)
                                            locations[current_structure_location]["constructions"].pop(structure_name)
                                            change_nft_owner(nft_id, self.name)

                                    # record and change ownership in player db
                                    if structure_name not in self.constructions:
                                        self.add_a_structure(structure_name, "house")

                                    else:
                                        exist_location = self.constructions[structure_name].get("location")
                                        self.move_a_construction(structure_name, self.location)
                                        locations[exist_location]["constructions"].pop(structure_name)

                                    # construct
                                    if construction_type == "house":
                                        locations[self.location]["constructions"][structure_name]["name"] = str(
                                            structure_name)
                                        locations[self.location]["constructions"][structure_name][
                                            "construction_type"] = "accommodation"
                                        locations[self.location]["constructions"][structure_name]["teleport"] = str(
                                            structure_name)
                                        locations[self.location]["constructions"][structure_name]["enter"] = True
                                        locations[self.location]["constructions"][structure_name][
                                            "description"] = str(self.name) + "'s house."
                                        locations[structure_name] = {}
                                        locations[structure_name]["area_type"] = "Home"
                                        locations[structure_name]["climate"] = None
                                        locations[structure_name]["east"] = str(structure_name)
                                        locations[structure_name]["west"] = str(structure_name)
                                        locations[structure_name]["south"] = str(structure_name)
                                        locations[structure_name]["north"] = str(structure_name)
                                        locations[structure_name]["up"] = str(structure_name)
                                        locations[structure_name]["down"] = str(structure_name)
                                        locations[structure_name]["movement_type"] = None
                                        locations[structure_name]["monsters"] = []
                                        locations[structure_name]["monster_population"] = 0
                                        locations[structure_name]["description"] = str(self.name) + "'s home."
                                        locations[structure_name]["visible_object"] = []
                                        locations[structure_name]["name"] = str(structure_name)
                                        locations[structure_name]["icon"] = "🏠"
                                        locations[structure_name]["portrait"] = self.nft_inventory[
                                            str(structure_name)].get("portrait")
                                        locations[structure_name]["constructions"] = {}
                                        locations[structure_name]["constructions"]["Door"] = {}
                                        locations[structure_name]["constructions"]["Door"]["name"] = "Door"
                                        locations[structure_name]["constructions"]["Door"]["construction_type"] = "door"
                                        locations[structure_name]["constructions"]["Door"]["teleport"] = str(
                                            self.location)
                                        locations[structure_name]["constructions"]["Door"]["enter"] = True
                                        locations[structure_name]["constructions"]["Door"][
                                            "description"] = "A door in " + str(self.name) + "'s house."
                                        locations[structure_name]["constructions"]["Door"]["icon"] = ""

                                        save_location_db(locations)
                                        log = f"You constructed {str(structure_name)} in this location."
                                    else:
                                        log = f"{str(structure_name)} is an unknown type of structure..."
                                else:
                                    log = "You need " + str(construction_price) + " to construct " + str(
                                        structure_name) + "."
                            else:
                                log = str(structure_name) + " is already in this location."
                        else:
                            log = str(structure_name) + " is not a structure."
                    else:
                        if structure_name == "farm":
                            if self.stamina >= 800:
                                locations = open_locations_db()
                                constructions = locations[self.location].get("constructions")
                                farm_is_here = False
                                if type(constructions) == dict:
                                    for i in constructions:
                                        if constructions[i].get("name") == "Farm":
                                            farm_is_here = True

                                if farm_is_here == False:
                                    farm_name = add_farm(self.location)
                                    self.lost_stamina(800)
                                    self.add_a_structure(farm_name, "farm")
                                    log = "You constructed a farm in this location!"
                                else:
                                    log = "You already have a farm in this location!"
                            else:
                                log = "You are too tired to construct a farm! (800 stamina is required)"
                        else:
                            log = f"You don't have a license to construct {str(structure_name)}"
                else:
                    log = "You can not construct in Center of Manor."
            else:
                log = "You can't construct in public lands."
        else:
            log = "Please input !construct <structure name>."
        return log

    def remove_a_construction(self, player_name, structure_name):
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["players"]
        target = {"Name": str(player_name)}
        player_data = collection.find_one(target)
        player_data["Assets"]["Manor"]["constructions"].pop(structure_name)
        update = player_data["Assets"]["Manor"]["constructions"]
        field = "Assets.Manor.constructions"
        collection.update_one(target, {"$set": {field: update}})

    def move_a_construction(self, structure_name, new_location):
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["players"]
        target = {"Name": str(self.name)}
        player_data = collection.find_one(target)
        player_data["Assets"]["Manor"]["constructions"][structure_name]["location"] = new_location
        update = player_data["Assets"]["Manor"]["constructions"][structure_name]["location"]
        field = f"Assets.Manor.constructions.{structure_name}.location"
        collection.update_one(target, {"$set": {field: update}})

    def add_a_structure(self, structure_name, type):
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["players"]
        target = {"Name": str(self.name)}
        player_data = collection.find_one(target)
        player_data["Assets"]["Manor"]["constructions"][structure_name] = {}
        player_data["Assets"]["Manor"]["constructions"][structure_name]["type"] = type
        player_data["Assets"]["Manor"]["constructions"][structure_name]["location"] = self.location
        update = player_data["Assets"]["Manor"]["constructions"]
        field = "Assets.Manor.constructions"
        collection.update_one(target, {"$set": {field: update}})

    # functions related to fight
    def check_equipment(self):
        # load nft and in-game item list
        on_chain_items = self.nft_inventory
        in_game_items = self.inventory
        all_items = {}
        for i in on_chain_items:
            all_items[i] = on_chain_items[i]
        for i in in_game_items:
            all_items[i] = in_game_items[i]

        # check whether your equipment exist in inventory
        for i in self.equipment:
            if self.equipment[i] not in all_items:
                modify_player_data(str(self.name), f"Status.Equipment.{i}", "")

    def accept_the_quest(self, quest_name):
        quest_exist = self.quests.get(str(quest_name))
        if quest_exist is None:
            quests = open_quest_db()
            update = quests.get(quest_name)
            modify_player_data(str(self.name), f"Quests.{quest_name}", update)
            quest_status_update = "You accept the quest: " + str(quest_name)
        else:
            quest_status_update = "You already have this quest!"
        return quest_status_update

    def finish_the_quest(self, quest_name):
        quests = open_quest_db()
        the_quest = self.quests.get(str(quest_name))
        if the_quest is not None:
            cd_now = the_quest.get("cd")
            cd_max = the_quest.get("cd_max")
            if cd_now == 0:
                if the_quest.get("type") == "hunt":
                    quest_target = quests[quest_name].get("target")
                    hunt_number = quests[quest_name].get("number")
                    catched_target = self.catch.get(str(quest_target))
                    if catched_target is not None:
                        if catched_target >= hunt_number:
                            quest_status_update = "You have killed " + str(catched_target) + " " + str(
                                quest_target) + ", and successfully finished the quest!"
                            update = catched_target - hunt_number
                            modify_player_data(str(self.name), f"Assets.Catch.{quest_target}", update)
                            exp_gain = quests[quest_name]["reward"].get("experience")
                            coin_gain = quests[quest_name]["reward"].get("coin")
                            reputation_gain = quests[quest_name]["reward"].get("reputation")
                            self.earn_exp(exp_gain)
                            self.earn_coin(coin_gain)
                            self.earn_reputation(reputation_gain)
                            modify_player_data(str(self.name), f"Quests.{quest_name}.cd", cd_max)
                            if len(quests[quest_name]["reward"]["loot"]) > 0:
                                loot_gain = random.choice(quests[quest_name]["reward"]["loot"])
                                self.get_item(loot_gain, 1)
                            else:
                                loot_gain = "nothing"
                            quest_status_update += "\n" + "You obtained: " + str(exp_gain) + " exp, " + str(
                                coin_gain) + " coins, " + str(reputation_gain) + " reputation, and " + str(loot_gain)

                        else:
                            quest_status_update = "You not yet finished the quest!"
                    else:
                        quest_status_update = "You not yet finished the quest!"

                if quests[quest_name]["type"] == "collect item":
                    summary = {}
                    quest_target = quests[quest_name]["target"]
                    temp_inventory = []
                    for i in self.inventory:
                        temp_inventory.extend([i] * int(self.inventory[i]["number"]))
                    checklist = []

                    for i in quest_target:
                        if i in temp_inventory:
                            temp_inventory.remove(i)
                            checklist.append(i)

                    if len(checklist) > 0:
                        if quests[quest_name]["one_by_one"] == True:
                            quest_complete = True
                            checklist = [random.choice(checklist)]
                        else:
                            if checklist == quest_target:
                                quest_complete = True
                            else:
                                quest_complete = False

                        if quest_complete == True:
                            for item in checklist:
                                if item not in summary:
                                    summary[item] = 1
                                else:
                                    summary[item] += 1
                            display = ""
                            for item in summary:
                                display += str(summary[item]) + " " + str(item)
                                self.get_item(item, -summary[item])

                            quest_status_update = "You delivered " + display + " and successfully finished the quest!"
                            exp_gain = quests[quest_name]["reward"].get("experience")
                            coin_gain = quests[quest_name]["reward"].get("coin")
                            reputation_gain = quests[quest_name]["reward"].get("reputation")
                            self.earn_exp(exp_gain)
                            self.earn_coin(coin_gain)
                            self.earn_reputation(reputation_gain)
                            modify_player_data(str(self.name), f"Quests.{quest_name}.cd", cd_max)
                            if len(quests[quest_name]["reward"]["loot"]) > 0:
                                loot_gain = ""
                                loot = random.choice(quests[quest_name]["reward"]["loot"])
                                self.get_item(loot, 1)
                                loot_gain += str(loot) + "  "
                            else:
                                loot_gain = "nothing"
                            quest_status_update += "\n" + "You obtained: " + str(exp_gain) + " exp, " + str(
                                coin_gain) + " coins, " + str(reputation_gain) + " reputation, and " + str(loot_gain)
                        else:
                            quest_status_update = "You not yet finished the quest!"
                    else:
                        quest_status_update = "You not yet finished the quest!"
            else:
                quest_status_update = "You still need to wait for {} minutes to finish this quest!".format(cd_now)
        else:
            quest_status_update = "You don't have this quest!"
        return quest_status_update

    def buy_manor(self, manor_price):
        if self.manor_center == "Tavern":
            if self.coin >= manor_price:
                self.earn_coin(-manor_price)
                locations = open_locations_db()
                new_room = str(random.getrandbits(32))
                modify_player_data(str(self.name), f"Assets.Manor.center", new_room)
                update = self.lands.append(new_room)
                modify_player_data(str(self.name), f"Assets.Manor.lands", update)
                locations[new_room] = {}
                locations[new_room]["area_type"] = "City"
                locations[new_room]["climate"] = None
                locations[new_room]["east"] = str(new_room)
                locations[new_room]["west"] = str(new_room)
                locations[new_room]["south"] = str(new_room)
                locations[new_room]["north"] = str(new_room)
                locations[new_room]["up"] = str(new_room)
                locations[new_room]["down"] = str(new_room)
                locations[new_room]["movement_type"] = None
                locations[new_room]["monsters"] = []
                locations[new_room]["monster_population"] = 0
                locations[new_room]["constructions"] = {}
                locations[new_room]["description"] = "You are standing inside " + str(self.name) + "'s manor."
                locations[new_room]["visible_object"] = []
                locations[new_room]["name"] = "Center of Manor"
                manor_type = str(random.randint(1, 15))
                locations[new_room]["icon"] = "🏦️"
                locations[new_room][
                    "portrait"] = "https://github.com/Chia-Inventory-The-Green-Whale/Chia-Inventory/blob/main/icons/manor{}.jpg?raw=true".format(
                    manor_type)
                save_location_db(locations)
                buy_manor_status_update = "Now you own a manor!"
            else:
                buy_manor_status_update = "You don't have enough funds..."
        else:
            buy_manor_status_update = "You already have a manor..."

        return buy_manor_status_update

    def purchase(self, merchandise_name, merchandise_price, merchandise_material, merchandise_number):
        item_list = ""
        temp_inventory = []
        for i in self.inventory:
            temp_inventory.extend([i] * int(self.inventory[i]["number"]))
        checklist = []

        for i in merchandise_material:
            if i in temp_inventory:
                temp_inventory.remove(i)
                checklist.append(i)

        if checklist == merchandise_material:
            material = True
        else:
            material = False

        if material == True:
            if self.coin >= merchandise_price:
                if len(checklist) > 0:
                    for i in checklist:
                        item_list += str(i) + "  "
                        self.get_item(i, -1)
                    purchase_status_update = "You delivered " + str(
                        item_list.rstrip(item_list[-2])) + "."
                else:
                    purchase_status_update = ""

                self.get_item(merchandise_name, merchandise_number)
                self.earn_coin(-merchandise_price)
                purchase_status_update += "\n" + "You paid " + str(merchandise_price)
                purchase_status_update += "\n" + "You bought " + str(merchandise_name)
            else:
                purchase_status_update = "You cannot afford " + str(merchandise_name)
        else:
            purchase_status_update = "You don't have enough material to make " + str(merchandise_name)

        return purchase_status_update

    def reforge(self, reforge_name, reforge_price, reforge_reputation):
        item_choose = "None"
        penalty = self.reforge_penalty.get(reforge_name)
        if penalty is None:
            penalty = 0
        else:
            penalty = penalty
        reforge_price = reforge_price + penalty * 50
        reforge_reputation = reforge_reputation + penalty * 5
        if self.coin >= reforge_price:
            if self.reputation > reforge_reputation:
                if self.inventory.get(str(reforge_name)) is not None:
                    if self.inventory[str(reforge_name)]["number"] > 0:
                        self.get_item(reforge_name, -1)
                        self.earn_coin(-reforge_price)
                        self.earn_reputation(-reforge_reputation)
                        item_list = os.listdir("./reforge/" + str(reforge_name))
                        item_number = len(item_list)
                        if item_number > 0:
                            item_choose = "./reforge/" + str(reforge_name) + "/" + random.choice(item_list)
                            purchase_status_update = "You paid " + str(reforge_price) + " CC."
                            purchase_status_update += "\n" + "You lost " + str(reforge_reputation) + " reputation."
                            purchase_status_update += "\n" + "You reforged " + str(reforge_name)
                            modify_player_data(str(self.name), f"Status.Reforge Penalty.{reforge_name}", penalty + 1)

                        else:
                            purchase_status_update = "Merchant does not have enough materials to reforge " + str(
                                reforge_name)
                    else:
                        purchase_status_update = "You don't have " + str(reforge_name)
                else:
                    purchase_status_update = "You don't have " + str(reforge_name)
            else:
                purchase_status_update = "Your reputation is not good enough to reforge " + str(reforge_name)
        else:
            purchase_status_update = "You cannot afford the reforge of " + str(reforge_name)

        return item_choose, purchase_status_update

    def nft_purchase(self, merchandise_name, merchandise_price):
        item_choose = "None"
        if self.coin >= merchandise_price:
            item_list = os.listdir("./reforge/" + str(merchandise_name))
            item_number = len(item_list)
            if item_number > 0:
                self.earn_coin(-merchandise_price)
                item_choose = "./reforge/" + str(merchandise_name) + "/" + random.choice(item_list)
                purchase_status_update = "You bought " + str(merchandise_name)
            else:
                purchase_status_update = "Merchant does not have " + str(merchandise_name)
        else:
            purchase_status_update = "You cannot afford " + str(merchandise_name)

        return item_choose, purchase_status_update

    def ask_npc(self, npc_name, keys):
        communication = open_communication_db()
        item_choose = "None"
        head = "💬 Talk with " + str(npc_name)
        message = ""
        outcome = None
        hint = "Type !ask index_number (1, 2, etc...) to ask more"
        if len(keys) == 0:
            for i in communication[str(npc_name)]:
                response = communication[str(npc_name)][str(i)]["question"]
                message += "\n" + str(i) + ": " + str(response)
        else:
            if len(keys) == 1:
                key_list1 = list(communication[str(npc_name)].keys())
                if str(keys[0]) in key_list1:
                    response = communication[str(npc_name)][str(keys[0])]["response"]
                    message += "\n" + response
                    if communication[str(npc_name)][str(keys[0])].get("ask") != None:
                        message += "\n" + "What do you want to ask?"
                        for i in communication[str(npc_name)][str(keys[0])]["ask"]:
                            response = communication[str(npc_name)][str(keys[0])]["ask"][str(i)]["question"]
                            message += "\n" + str(i) + ": " + str(response)
                else:
                    message += "\n" + "I don't understand your question."

            if len(keys) == 2:
                key_list1 = list(communication[str(npc_name)].keys())
                key_list2 = list(communication[str(npc_name)][str(keys[0])]["ask"].keys())
                if str(keys[0]) in key_list1 and str(keys[1]) in key_list2:
                    response = communication[str(npc_name)][str(keys[0])]["ask"][str(keys[1])]["response"]
                    message += "\n" + response
                    interaction_type = communication[str(npc_name)][str(keys[0])]["ask"][str(keys[1])]["type"]
                    if interaction_type == "accept_quest":
                        quest_name = communication[str(npc_name)][str(keys[0])]["ask"][str(keys[1])]["accept_quest"]
                        quest_status_update = self.accept_the_quest(str(quest_name))
                        outcome = str(quest_status_update)
                    if interaction_type == "finish_quest":
                        quest_name = communication[str(npc_name)][str(keys[0])]["ask"][str(keys[1])]["finish_quest"]
                        quest_status_update = self.finish_the_quest(str(quest_name))
                        outcome = str(quest_status_update)
                    if interaction_type == "merchant":
                        merchandise_name = communication[str(npc_name)][str(keys[0])]["ask"][str(keys[1])][
                            "merchandise"]
                        merchandise_price = communication[str(npc_name)][str(keys[0])]["ask"][str(keys[1])]["price"]
                        merchandise_material = communication[str(npc_name)][str(keys[0])]["ask"][str(keys[1])][
                            "material"]
                        merchandise_number = communication[str(npc_name)][str(keys[0])]["ask"][str(keys[1])][
                            "number"]
                        purchase_status_update = self.purchase(str(merchandise_name),
                                                               merchandise_price,
                                                               merchandise_material, merchandise_number)
                        outcome = str(purchase_status_update)
                    if interaction_type == "reforge":
                        reforge_name = communication[str(npc_name)][str(keys[0])]["ask"][str(keys[1])].get("reforge")
                        reforge_price = communication[str(npc_name)][str(keys[0])]["ask"][str(keys[1])].get("price")
                        reforge_reputation = communication[str(npc_name)][str(keys[0])]["ask"][str(keys[1])].get(
                            "reputation")
                        item_choose, reforge_status_update = self.reforge(str(reforge_name),
                                                                          reforge_price,
                                                                          reforge_reputation)
                        outcome = str(reforge_status_update)
                    if interaction_type == "buy_manor":
                        manor_price = communication[str(npc_name)][str(keys[0])]["ask"][str(keys[1])]["price"]
                        buy_manor_status_update = self.buy_manor(manor_price)
                        outcome = str(buy_manor_status_update)
                    if interaction_type == "nft_merchant":
                        merchandise_name = communication[str(npc_name)][str(keys[0])]["ask"][str(keys[1])][
                            "merchandise"]
                        merchandise_price = communication[str(npc_name)][str(keys[0])]["ask"][str(keys[1])]["price"]
                        item_choose, purchase_status_update = self.nft_purchase(merchandise_name, merchandise_price)
                        outcome = str(purchase_status_update)

                else:
                    message += "\n" + "I don't understand your question."

            if len(keys) > 2:
                message += "\n" + "I don't understand your question."

        return head, message, outcome, hint, item_choose

    def sell_item(self, item_name, number):
        log = ""
        if item_name in self.inventory:
            item_number = self.inventory[str(item_name)]["number"]
            if item_number >= number:
                item_list = get_item_list()
                if item_name in item_list:
                    item_data = query_item_data(item_name)
                    value = item_data.get("value")
                    if value == None:
                        value = 0
                    for n in range(0, number):
                        self.earn_coin(value)
                        self.lost_item(item_name)
                    log += f"You sold {str(number)} {str(item_name)} for {str(value)} CC"
                else:
                    log += f"{item_name} is from another world, no one knows its value in Chiania."
            else:
                log += f"You don't have enough {item_name}."
        else:
            log += f"You don't have {item_name}."

        return log

    def use_item(self, item_name, number):
        log = ""
        item_data = query_item_data(item_name)
        item_type = item_data["item_type"]
        item_number = self.inventory[str(item_name)]["number"]
        item_function = item_data.get("function")
        if item_type == "consumable":
            if item_number >= number:
                log += "\n" + "You consumed " + str(number) + " " + str(item_name)
                summary = {}
                for n in range(0, number):
                    if item_function == "key":
                        target = item_data.get("key")
                        mobile_objects = get_mobile_object(self.location)
                        if target in mobile_objects:
                            kill_monster(self.location, target)
                            loot, message = open_box(str(target))
                            self.get_item(item_name, -1)
                            self.get_item(loot, 1)
                            log += "\n" + message
                            log += "\n" + "You obtained a " + str(loot)
                        else:
                            log += "\n" + "You cannot find a " + str(
                                target) + " to unlock, so you put the key back to inventory."
                    if item_function == "food":
                        food_functions = item_data.get("food")
                        for function in food_functions:
                            if function == "Stamina":
                                update = food_functions.get("Stamina")
                                self.recover_stamina(update)
                            if function == "Drunk":
                                update = food_functions.get("Drunk")
                                self.get_drunk(update)
                            if function not in summary:
                                summary[function] = update
                            else:
                                summary[function] += update
                        self.get_item(item_name, -1)

                    if item_function == "treasure box":
                        contents = item_data["content"]
                        # distribute coins
                        minimum_coin = contents["coin"]["min"]
                        maximum_coin = contents["coin"]["max"]
                        coin_obtained = random.randint(minimum_coin, maximum_coin)
                        self.earn_coin(coin_obtained)

                        if "coin" not in summary:
                            summary["coin"] = coin_obtained
                        else:
                            summary["coin"] += coin_obtained

                        # distribute unlimited items
                        unlimited_items = contents["unlimited"]
                        item_number = contents["item_number"]
                        for i in range(item_number):
                            unlimited_item = random.choice(unlimited_items)
                            self.get_item(unlimited_item, 1)
                            if unlimited_item not in summary:
                                summary[unlimited_item] = 1
                            else:
                                summary[unlimited_item] += 1

                        # distribute limited items
                        if len(contents["limited"]) > 0:
                            limited_item = random.choice(contents["limited"])
                            item_data["content"]["limited"].remove(limited_item)
                            modify_item_data(item_name, "content.limited", update)
                            self.get_item(limited_item)
                            log += "\n" + " You obtained a " + str(limited_item)
                        self.get_item(item_name, -1)

                if summary != {}:
                    log += "\n" + " You obtained "
                    for item in summary:
                        log += str(summary[item]) + " " + str(item) + " "
            else:
                log += "\n" + "You don't have this item..."
        else:
            log += "\n" + "You cannot use this item..."

        return log

    def assign_attribute(self):
        # load nft and in-game item list
        global str, int
        on_chain_items = self.nft_inventory
        in_game_items = self.inventory
        all_items = {}
        for i in on_chain_items:
            all_items[i] = on_chain_items[i]
        for i in in_game_items:
            all_items[i] = in_game_items[i]

        # loop equipment attributes
        confidence = 0
        for i in self.equipment:
            if self.equipment[i] != "":
                confidence += 1
                item_name = self.equipment[i]
                if item_name in all_items:
                    item_attribute = all_items[item_name]
                    if item_attribute.get("number") != None:
                        item_attribute = all_items[item_name]["in-game-attributes"]
                    if "enhancement" in item_attribute:
                        enhancement = item_attribute["enhancement"].get("value")
                    else:
                        enhancement = 0
                    for j in item_attribute:
                        if type(item_attribute[j]) != str:
                            if item_attribute[j].get("factor") != None:
                                factor = item_attribute[j].get("factor")
                                value = item_attribute[j].get("value")
                                probability = item_attribute[j].get("probability")
                                modifier = 0
                                # how to determine attributes
                                if factor == "constant":
                                    modifier = value + enhancement * 0.1
                                elif factor == "random":
                                    if int(1 + enhancement * 0.2) > value:
                                        enhancement = (value - 1) / 0.2
                                    modifier = random.randint(int(1 + enhancement * 0.2), value)
                                elif factor == "level_scale":
                                    if (enhancement * 0.1) > (value - 1):
                                        enhancement = (value - 1) / 0.1
                                    modifier = round(self.level / (value - enhancement * 0.1))
                                elif factor == "probability":
                                    probability = (probability * 100) + enhancement
                                    chance = \
                                        random.choices([True, False], weights=(probability, 100 - probability), k=1)[0]
                                    if chance == True:
                                        modifier = value
                                # start to modify attribute: item effects
                                attribute = item_attribute[j].get("type")
                                # positive impacts
                                if attribute == "increase_str":
                                    self.str += modifier
                                elif attribute == "increase_dex":
                                    self.dex += modifier
                                elif attribute == "increase_con":
                                    self.con += modifier
                                elif attribute == "increase_int":
                                    self.int += modifier
                                elif attribute == "increase_wis":
                                    self.wis += modifier
                                elif attribute == "increase_cha":
                                    self.cha += modifier
                                elif attribute == "increase_luc":
                                    self.luc += modifier
                                elif attribute == "increase_defense":
                                    self.defense += modifier
                                elif attribute == "increase_pierce":
                                    self.pierce += modifier
                                elif attribute == "increase_bash":
                                    self.bash += modifier
                                elif attribute == "increase_slash":
                                    self.slash += modifier

                                # negative impacts
                                elif attribute == "decrease_str":
                                    self.str -= modifier
                                elif attribute == "decrease_dex":
                                    self.dex -= modifier
                                elif attribute == "decrease_con":
                                    self.con -= modifier
                                elif attribute == "decrease_int":
                                    self.int -= modifier
                                elif attribute == "decrease_wis":
                                    self.wis -= modifier
                                elif attribute == "decrease_cha":
                                    self.cha -= modifier
                                elif attribute == "decrease_luc":
                                    self.luc -= modifier
                                elif attribute == "decrease_defense":
                                    self.defense -= modifier
                                elif attribute == "decrease_pierce":
                                    self.pierce -= modifier
                                elif attribute == "decrease_bash":
                                    self.bash -= modifier
                                elif attribute == "decrease_slash":
                                    self.slash -= modifier

                else:
                    log = str(item_name) + " not found in inventory."
            else:
                log = "slot: " + str(i) + " = no equipment"

        # self
        self.str += round(self.level / 10)
        self.dex += round(self.level / 10)
        self.con += round(self.level / 10)
        self.int += round(self.level / 10)
        self.wis += round(self.level / 10)
        self.cha += round(self.level / 10)
        self.luc += round(self.level / 10)

        if self.str > self.level * 1.5 + 5 + confidence:
            self.str = 5 + confidence + round(self.level * 1.5)
        if self.dex > self.level * 1.5 + 5 + confidence:
            self.dex = 5 + confidence + round(self.level * 1.5)
        if self.con > self.level * 1.5 + 5 + confidence:
            self.con = 5 + confidence + round(self.level * 1.5)
        if self.int > self.level * 1.5 + 5 + confidence:
            self.int = 5 + confidence + round(self.level * 1.5)
        if self.wis > self.level * 1.5 + 5 + confidence:
            self.wis = 5 + confidence + round(self.level * 1.5)
        if self.cha > self.level * 1.5 + 5 + confidence:
            self.cha = 5 + confidence + round(self.level * 1.5)
        if self.luc > self.level * 1.5 + 5 + confidence:
            self.luc = 5 + confidence + round(self.level * 1.5)

        self.defense += int(self.con / 10)
        if self.defense > self.level * 1 + confidence / 3:
            self.defense = round(self.level * 1 + confidence / 3)

        self.health += int(self.con / 3)
        self.slash = self.slash + int(self.slash * self.str / 10)
        self.bash = self.bash + int(self.bash * self.str / 10)
        self.pierce = self.pierce + int(self.pierce * (self.str + self.dex) / 20)
        if self.slash > self.level * 1 + 1 + confidence / 3:
            self.slash = round(self.level * 1 + confidence / 3) + 1
        if self.bash > self.level * 1 + 1 + confidence / 3:
            self.bash = round(self.level * 1 + confidence / 3) + 1
        if self.pierce > self.level * 1 + 1 + confidence / 3:
            self.pierce = round(self.level * 1 + confidence / 3) + 1

        # 20220929 added buff
        if len(self.buff) > 0:
            for i in self.buff:
                attribute = self.buff[i].get("type")
                factor = self.buff[i].get("factor")
                value = self.buff[i].get("value")
                probability = self.buff[i].get("probability")
                enhancement = 0
                modifier = 0
                if factor == "constant":
                    modifier = value + enhancement * 0.1
                elif factor == "random":
                    if int(1 + enhancement * 0.2) > value:
                        enhancement = (value - 1) / 0.2
                    modifier = random.randint(int(1 + enhancement * 0.2), value)
                elif factor == "level_scale":
                    if (enhancement * 0.1) > (value - 1):
                        enhancement = (value - 1) / 0.1
                    modifier = round(self.level / (value - enhancement * 0.1))
                elif factor == "probability":
                    probability = (probability * 100) + enhancement
                    chance = random.choices([True, False], weights=(probability, 100 - probability), k=1)[0]
                    if chance == True:
                        modifier = value
                if attribute == "buff_str":
                    self.str += modifier
                elif attribute == "buff_dex":
                    self.dex += modifier
                elif attribute == "buff_con":
                    self.con += modifier
                elif attribute == "buff_int":
                    self.int += modifier
                elif attribute == "buff_wis":
                    self.wis += modifier
                elif attribute == "buff_cha":
                    self.cha += modifier
                elif attribute == "buff_luc":
                    self.luc += modifier
                elif attribute == "buff_defense":
                    self.defense += modifier
                elif attribute == "buff_pierce":
                    self.pierce += modifier
                elif attribute == "buff_bash":
                    self.bash += modifier
                elif attribute == "buff_slash":
                    self.slash += modifier


def level(player_exp):
    level = 1
    next_exp = 5
    while True:
        if player_exp > next_exp:
            level += 1
            player_exp -= next_exp
            next_exp = 5 + next_exp * 1.3
        else:
            break
    level = int(level)
    player_exp = int(player_exp)
    next_exp = int(next_exp)
    return level, player_exp, next_exp


def add_farm(current_location):
    locations = open_locations_db()
    constructions = locations[current_location].get("constructions")
    if constructions == None:
        locations[current_location]["constructions"] = {}

    # create a farm in the current room
    farm_name = str(random.getrandbits(32))
    style = str(random.randint(1, 11))
    structure_name = "Farm " + farm_name
    locations[current_location]["constructions"][structure_name] = {
        "name": "Farm",
        "construction_type": "farm",
        "teleport": False,
        "enter": False,
        "description": "A farm.",
        "icon": "🌾",
        "portrait": "https://raw.githubusercontent.com/Chia-Inventory-The-Green-Whale/Chia-Inventory/main/icons/farm" + str(
            style) + ".jpg"
    }
    save_location_db(locations)
    return structure_name


def yaml(log):
    output = "\n" + "```yaml" + "\n" + log + "```"
    return output
