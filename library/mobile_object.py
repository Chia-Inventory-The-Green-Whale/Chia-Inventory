import random
import ujson as json


class mobile_object:
    def __init__(self, name):
        self.name = name
        self.type = "monster"
        self.health = 20
        self.attack = 0
        self.attack_method = "attack"
        self.skill = self.attack_method
        self.DEFslash = 0
        self.DEFbash = 0
        self.DEFpierce = 0
        self.loot = []
        self.description = ""
        self.author = ""
        self.coin = 0
        self.exp = 0
        self.interaction = False
        self.interaction_link = None
        self.ask = []
        self.listen = []
        self.answer = []
        self.aggression = "passive"
        self.category = "not_defined"


def encounter(monster_name):
    monster = mobile_object(monster_name)
    with open('./library/mobile_object.json', 'r', encoding="utf-8") as file:
        mobile_objects = json.load(file)
        file.close()

    # monster attributes
    monster.name = str(mobile_objects[str(monster_name)]["name"])
    monster.type = str(mobile_objects[str(monster_name)]["type"])
    monster.health = mobile_objects[str(monster_name)]["health"]
    monster.attack = mobile_objects[str(monster_name)]["attack"]
    monster.attack_method = mobile_objects[str(monster_name)]["attack_method"]
    monster.skill = mobile_objects[str(monster_name)]["skill"]
    monster.DEFslash = mobile_objects[str(monster_name)]["slash_defense"]
    monster.DEFbash = mobile_objects[str(monster_name)]["bash_defense"]
    monster.DEFpierce = mobile_objects[str(monster_name)]["pierce_defense"]
    monster.loot = mobile_objects[str(monster_name)]["loot"]
    monster.description = mobile_objects[str(monster_name)]["description"]
    monster.author = mobile_objects[str(monster_name)]["author"]
    monster.aggression = mobile_objects[str(monster_name)]["aggression"]
    monster.category = mobile_objects[str(monster_name)]["category"]

    # hp and attack adjustion
    monster.health = monster.health + random.randint(0, int(monster.health / 3))
    monster.attack = monster.attack + random.randint(0, int(monster.attack / 3))

    # exp and coin formula
    monster.exp = int(monster.health / 7) + int((monster.DEFslash + monster.DEFbash + monster.DEFpierce) / 3) + int(
        monster.attack / 6)
    monster.coin = int(monster.exp / 5) + random.randint(0, int(monster.exp / 2))

    return monster


def add_monster(monster_name):
    with open('./library/mobile_object.json', 'r', encoding="utf-8") as file:
        mobile_objects = json.load(file)
        file.close()

    mobile_objects[str(monster_name)] = {}
    mobile_objects[str(monster_name)]["name"] = str(monster_name)
    mobile_objects[str(monster_name)]["type"] = "monster"
    mobile_objects[str(monster_name)]["health"] = 20
    mobile_objects[str(monster_name)]["attack"] = 0
    mobile_objects[str(monster_name)]["attack_method"] = "attack"
    mobile_objects[str(monster_name)]["skill"] = []
    mobile_objects[str(monster_name)]["slash_defense"] = 0
    mobile_objects[str(monster_name)]["bash_defense"] = 0
    mobile_objects[str(monster_name)]["pierce_defense"] = 0
    mobile_objects[str(monster_name)]["loot"] = []
    mobile_objects[str(monster_name)]["description"] = None
    mobile_objects[str(monster_name)]["author"] = None
    mobile_objects[str(monster_name)]["interaction"] = False
    mobile_objects[str(monster_name)]["interaction_link"] = None
    mobile_objects[str(monster_name)]["ask"] = []
    mobile_objects[str(monster_name)]["listen"] = []
    mobile_objects[str(monster_name)]["answer"] = []
    mobile_objects[str(monster_name)]["aggression"] = "passive"
    mobile_objects[str(monster_name)]["category"] = "not_defined"

    with open('./library/mobile_object.json', 'w') as file:
        json.dump(mobile_objects, file)


def add_npc(npc_name):
    with open('./library/mobile_object.json', 'r') as file:
        mobile_objects = json.load(file)
        file.close()

    mobile_objects[str(npc_name)] = {}
    mobile_objects[str(npc_name)]["name"] = str(npc_name)
    mobile_objects[str(npc_name)]["type"] = "npc"
    mobile_objects[str(npc_name)]["health"] = 999
    mobile_objects[str(npc_name)]["attack"] = 999
    mobile_objects[str(npc_name)]["attack_method"] = "attack"
    mobile_objects[str(npc_name)]["skill"] = []
    mobile_objects[str(npc_name)]["slash_defense"] = 99
    mobile_objects[str(npc_name)]["bash_defense"] = 99
    mobile_objects[str(npc_name)]["pierce_defense"] = 99
    mobile_objects[str(npc_name)]["loot"] = []
    mobile_objects[str(npc_name)]["description"] = None
    mobile_objects[str(npc_name)]["author"] = None
    mobile_objects[str(npc_name)]["interaction"] = True
    mobile_objects[str(npc_name)]["aggression"] = "passive"
    mobile_objects[str(npc_name)]["category"] = "not_defined"
    mobile_objects[str(npc_name)]["icon"] = ""

    with open('./library/mobile_object.json', 'w') as file:
        json.dump(mobile_objects, file)


def add_treasure_box(treasure_box_name):
    with open('./library/mobile_object.json', 'r') as file:
        mobile_objects = json.load(file)
        file.close()

    mobile_objects[str(treasure_box_name)] = {}
    mobile_objects[str(treasure_box_name)]["name"] = str(treasure_box_name)
    mobile_objects[str(treasure_box_name)]["type"] = "treasure_box"
    mobile_objects[str(treasure_box_name)]["health"] = 999
    mobile_objects[str(treasure_box_name)]["attack"] = 999
    mobile_objects[str(treasure_box_name)]["attack_method"] = "attack"
    mobile_objects[str(treasure_box_name)]["skill"] = []
    mobile_objects[str(treasure_box_name)]["slash_defense"] = 99
    mobile_objects[str(treasure_box_name)]["bash_defense"] = 99
    mobile_objects[str(treasure_box_name)]["pierce_defense"] = 99
    mobile_objects[str(treasure_box_name)]["loot"] = []
    mobile_objects[str(treasure_box_name)]["description"] = None
    mobile_objects[str(treasure_box_name)]["author"] = None
    mobile_objects[str(treasure_box_name)]["interaction"] = True
    mobile_objects[str(treasure_box_name)]["aggression"] = "passive"
    mobile_objects[str(treasure_box_name)]["category"] = "not_defined"

    with open('./library/mobile_object.json', 'w') as file:
        json.dump(mobile_objects, file)


def place_mob(location_name, mob_name):
    with open('./library/locations.json', 'r') as file:
        locations = json.load(file)
        file.close()
    locations[location_name]["npc"].append(str(mob_name))
    with open('./library/locations.json', 'w') as file:
        json.dump(locations, file)


def place_farmer(location_name, farmer_name):
    with open('./library/locations.json', 'r') as file:
        locations = json.load(file)
        file.close()
    locations[location_name]["farmer"].append(str(farmer_name))
    with open('./library/locations.json', 'w') as file:
        json.dump(locations, file)


def npc_all():
    with open('./library/locations.json', 'r') as file:
        locations = json.load(file)
        file.close()
    for i in locations:
        locations[str(i)]["npc"] = []
    with open('./library/locations.json', 'w') as file:
        json.dump(locations, file)


def check_player_quest(player_name, quest_name):
    with open('./Players.json', 'r') as file:
        players = json.load(file)
        file.close()
    if players[str(player_name)].get("quest") == None:
        players[player_name]["quest"] = {}
        result = False
    else:
        if quest_name in players[player_name]["quest"]:
            if players[player_name]["quest"][quest_name]["begin"] == True:
                result = True
            else:
                result = False
        else:
            result = False
    return result


def add_communication(mob_name, question_number):
    with open('./library/communication.json', 'r') as file:
        communications = json.load(file)
        file.close()
    communications[str(mob_name)] = {}
    for i in range(1, question_number):
        communications[str(mob_name)][str(i)] = {
            "question": "",
            "response": "",
            "type": "rumor"
        }
    with open('./library/communication.json', 'w') as file:
        json.dump(communications, file)


def open_box(treasure_box_name):
    with open('./library/mobile_object.json', 'r', encoding="utf-8") as file:
        mobile_objects = json.load(file)
        file.close()
    loot = random.choice(mobile_objects[str(treasure_box_name)]["loot"])
    message = mobile_objects[str(treasure_box_name)]["description"]

    return loot, message


def add_icon():
    with open('./library/in_game_item.json', 'r') as file:
        in_game_item = json.load(file)
        file.close()
    for i in in_game_item:
        in_game_item[str(i)]["icon"] = "❓"
    with open('./library/in_game_item.json', 'w') as file:
        json.dump(in_game_item, file)
