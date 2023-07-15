import pymongo
import time
import random
from library.json_db import *
import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
client = pymongo.MongoClient()


# start to reorganize player db
def generate_players_v2_mongodb():
    players = open_player_db()
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["players"]

    for i in players:
        players_v2 = {
            "Name": players[i].get("Name"),
            "Address": {
                "DID": players[i].get("Address"),
                "Reward Address": players[i].get("Reward Address")
            },
            "Status": {
                "Exp": players[i]["Exp"],
                "Life": players[i]["Life"],
                "Stamina": players[i]["Stamina"],
                "Mount Stamina": players[i].get("Mount Stamina"),
                "Drunk": players[i]["Drunk"],
                "Life_count": players[i]["Life_count"],
                "Location": players[i].get("Location"),
                "Channel": players[i].get("Channel"),
                "Cool Down": {
                    "Latest Withdraw": players[i].get("Latest Withdraw"),
                    "Latest Hunt": players[i].get("Latest Hunt")
                },
                "Production": players[i].get("Production"),
                "Home": players[i].get("Home"),
                "Buff": {},
                "Home Stay": 0,
                "Reforge Penalty": players[i].get("NFT_reforge_penalty"),
                "Equipment": players[i].get("Equipment"),
                "Message": players[i].get("Message")
            },
            "Class": {
                "Basic": {
                    "Name": None,
                    "Level": 0
                },
                "Advance": {
                    "Name": None,
                    "Level": 0
                }
            },
            "Skills": {

            },
            'Assets': {
                "Wallet": players[i].get("Wallet"),
                "Reputation": players[i].get("Reputation"),
                "Manor": players[i].get("Manor"),
                "Inventory": {
                    "Items": players[i].get("Inventory"),
                    "NFTs": players[i].get("NFT Inventory")
                },
                "Catch": players[i].get("Hunts")
            },
            "Achievements": {},
            "Quests": players[i].get("Quest")
        }
        if collection.count_documents({"Name": i}) == 0:
            collection.insert_one(players_v2)
        else:
            target = {"Name": i}
            data = collection.find_one(target)
            print(data)
            print(players_v2)
            for j in data:
                if j != "_id":
                    if data[j] != players_v2[j]:
                        collection.update_one(target, {"$set": {j: players_v2[j]}})
                        print(f"Update database of {i}, {data[j]} into {players_v2[j]}")
                    else:
                        print(f"Data not updated!")


def generate_nft_v2_mongodb():
    nfts = open_on_chain_items_db()
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["nfts"]
    for nft in nfts:
        portrait = nfts[nft].get("icon")
        nfts[nft]["portrait"] = portrait
        nfts[nft]["icon"] = "❓"
        if collection.count_documents({"nft_id": nft}) == 0:
            collection.insert_one(nfts[nft])


def generate_item_v2_mongodb():
    items = open_in_game_items_db()
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["items"]
    for item in items:
        items[item]["name"] = item
        if collection.count_documents({"name": item}) == 0:
            collection.insert_one(items[item])


def add_a_nft(nft_id, metadata):
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["nfts"]
    if collection.count_documents({"nft_id": nft_id}) == 0:
        collection.insert_one(metadata)
        print(f"{str(nft_id)} has been added to database.")
    else:
        print(f"{str(nft_id)} is already in database.")


def query_nft_data(nft_id):
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["nfts"]
    target = {"nft_id": nft_id}
    nft_data = collection.find_one(target)
    return nft_data


def find_nft_id(item_name):
    nft_name_list = get_nft_name_list()
    if item_name in nft_name_list:
        client = pymongo.MongoClient()
        db = client["Chiania"]
        collection = db["nfts"]
        target = {"item_name": str(item_name)}
        selected_nfts = collection.find(target)
        nft_id_return = None
        for nft in selected_nfts:
            nft_id = nft.get("nft_id")
            if nft.get("burned") is None:
                url = 'https://api.mintgarden.io/nfts/' + str(nft_id)
                response = http.request('GET', url)
                data = BeautifulSoup(response.data, features="html.parser")
                data = json.loads(data.text)
                owner = data["owner_address"].get("encoded_id")
                if owner == "xch1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqm6ks6e8mvy" or owner == "xch1x0lmv0hv4cafhdanj49n0ugjm9crhuzte8m8r8cxus5haw64dhws6da2cf":
                    nft["burned"] = True
                else:
                    nft["burned"] = False
                    nft_id_return = nft_id
                target = {"nft_id": nft_id}
                collection.replace_one(target, nft)

            elif nft.get("burned") == False:
                nft_id_return = nft.get("nft_id")

    return nft_id_return


def query_item_data(item_name):
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["items"]
    target = {"name": item_name}
    item_data = collection.find_one(target)
    return item_data


def enhance_nft(nft_id):
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["nfts"]
    target = {"nft_id": nft_id}
    nft_data = collection.find_one(target)
    current_enhancement = nft_data["in-game-attributes"]["enhancement"].get("value")
    update = current_enhancement + 1
    field = "in-game-attributes.enhancement.value"
    modify_nft_data(nft_id, field, update)


def throw_a_dice():
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["server"]
    dice_list = ["small", "large", "odd", "even", "1", "20"]
    update = random.choice(dice_list)
    if collection.count_documents({"category": "dice"}) == 0:
        dice_db = {
            "category": "dice",
            "current_dice": update,
            "small": {
                "list": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                "reward": 1
            },
            "large": {
                "list": ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20"],
                "reward": 1
            },
            "odd": {
                "list": ["1", "3", "5", "7", "9", "11", "13", "15", "17", "19"],
                "reward": 1
            },
            "even": {
                "list": ["2", "4", "6", "8", "10", "12", "14", "16", "18", "20"],
                "reward": 1
            },
            "1": {
                "list": ["1"],
                "reward": 10
            },
            "20": {
                "list": ["20"],
                "reward": 10
            }
        }
        collection.insert_one(dice_db)
        print(f"dice_db has been added to database.")
        log = f"; Mimic throw a dice... it's {update}"
        print(log)
    else:
        target = {"category": "dice"}
        field = "current_dice"
        collection.update_one(target, {"$set": {field: update}})
        log = f"; Mimic throw a dice... it's {update}"
        print(log)
    return log


def what_is_current_dice():
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["server"]
    target = {"category": "dice"}
    dice_db = collection.find_one(target)
    current_dice = dice_db["current_dice"]
    win_list = dice_db[current_dice]["list"]
    reward = dice_db[current_dice]["reward"]
    return win_list, reward


def change_nft_owner(nft_id, player_name):
    update = player_name
    field = "in-game owner"
    modify_nft_data(nft_id, field, update)


def modify_nft_data(nft_id, field, update):
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["nfts"]
    target = {"nft_id": nft_id}
    collection.update_one(target, {"$set": {field: update}})
    print(f"{str(nft_id)}'s field {field} updated as {update}")


def modify_item_data(item_name, field, update):
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["items"]
    target = {"name": item_name}
    collection.update_one(target, {"$set": {field: update}})
    print(f"{str(item_name)}'s field {field} updated as {update}")


def get_player_list():
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["players"]
    player_list = collection.distinct("Name")
    return player_list


def get_nft_list():
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["nfts"]
    nft_list = collection.distinct("nft_id")
    return nft_list


def get_nft_name_list():
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["nfts"]
    nft_name_list = collection.distinct("item_name")
    return nft_name_list


def get_item_list():
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["items"]
    item_list = collection.distinct("name")
    return item_list


def get_all_players():
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["players"]
    players = collection.find()
    return players


def get_did_list():
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["players"]
    did_list = collection.distinct("Address.DID")
    return did_list


def get_player_data(player_name):
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["players"]
    target = {"Name": player_name}
    player_data = collection.find_one(target)
    return player_data


def get_player_nfts(player_name):
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["players"]
    target = {"Name": player_name}
    player_data = collection.find_one(target)
    nfts = player_data["Assets"]["Inventory"].get("NFTs")
    return nfts


def modify_player_wallet(player_name, amount):
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["players"]
    target = {"Name": player_name}
    player_data = collection.find_one(target)
    player_data["Assets"]["Wallet"] += amount
    update = player_data["Assets"]["Wallet"]
    field = "Assets.Wallet"
    collection.update_one(target, {"$set": {field: update}})


def modify_player_hunt_cd(player_name, timestamp):
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["players"]
    target = {"Name": player_name}
    player_data = collection.find_one(target)
    field = "Status.Cool Down.Latest Hunt"
    collection.update_one(target, {"$set": {field: timestamp}})


def get_player_location(player_name):
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["players"]
    target = {"Name": player_name}
    player_data = collection.find_one(target)
    location_name = player_data["Status"].get("Location")
    return location_name


def get_player_message_status(player_name):
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["players"]
    target = {"Name": player_name}
    player_data = collection.find_one(target)
    message_status = player_data["Status"].get("Message")
    return message_status


def save_player_db(player_name, player_db):
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["players"]
    target = {"Name": player_name}
    collection.replace_one(target, player_db)
    print(f"{str(player_name)}'s db updated!")


def modify_player_data(player_name, field, update):
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["players"]
    target = {"Name": player_name}
    collection.update_one(target, {"$set": {field: update}})
    print(f"{str(player_name)}'s field {field} updated as {update}")


# modify_player_data("Chia Inventory#9520", "Status.Exp", 10000)

def clear_mobile_object():
    client = pymongo.MongoClient()
    db = client.Chiania
    collection = db.mobile_object
    result = collection.find()
    for i in result:
        collection.delete_one({})
        print(result)


def insert_mobile_object():
    with open('mobile_object.json', 'r') as file:
        mobile_objects = json.load(file)
        file.close()

    client = pymongo.MongoClient()
    db = client.Chiania
    collection = db.mobile_object

    for i in mobile_objects:
        collection.insert_one(mobile_objects[i])
    result = collection.find()

    for j in result:
        print(j)


def all_mobs_python_way():
    st = time.time()
    client = pymongo.MongoClient()
    db = client.Chiania
    collection = db.mobile_object
    result = collection.find({}, {"_id": 0, "name": 1})
    mob_list = []
    for i in result:
        mob_list.append(i["name"])
    et = time.time()
    print(et - st)
    return mob_list


def all_mobs():
    st = time.time()
    client = pymongo.MongoClient()
    db = client.Chiania
    collection = db.mobile_object
    mob_list = collection.distinct("name")
    et = time.time()
    print(et - st)
    return mob_list


def who_is_here(location_name):
    client = pymongo.MongoClient()
    db = client["Chiania"]
    collection = db["players"]
    target = {"Status.Location": str(location_name)}
    players = collection.find(target)
    player_list = []
    for player in players:
        player_list.append(player["Name"])
    return player_list
