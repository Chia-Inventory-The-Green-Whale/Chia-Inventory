import json
import random

def list_generate(item_name, number1, number2, digital):
    list = ["{}".format(item_name) + "%.{}d".format(digital) % i for i in range(number1, number2 + 1)]
    return list


def create_category(category):
    with open('../not_used/item_list.json', 'r') as file:
        item_list = json.load(file)
        file.close()
        item_list[category] = {}
    with open('../not_used/item_list.json', 'w') as file:
        json.dump(item_list, file)


def insert_item(small_list, category):
    with open('./library/item_list.json', 'r') as file:
        item_list = json.load(file)
        file.close()
    for i in small_list:
        item_list[category][i] = {}
    with open('./library/item_list.json', 'w') as file:
        json.dump(item_list, file)


def insert_attribute(small_list, category, type, attr):
    with open('./library/item_list.json', 'r') as file:
        item_list = json.load(file)
        file.close()
    for i in small_list:
        if item_list[category].get(str(i)) == None:
            item_list[category][i] = {}
        item_list[category][i][type] = attr
    with open('./library/item_list.json', 'w') as file:
        json.dump(item_list, file)


def get_keys(category):
    with open('../not_used/item_list.json', 'r') as file:
        item_list = json.load(file)
        file.close()
        keys = item_list[category].keys()
    return keys


def remove_item(small_list, category):
    with open('../not_used/item_list.json', 'r') as file:
        item_list = json.load(file)
        file.close()
        for i in small_list:
            del item_list[category][i]
    with open('../not_used/item_list.json', 'w') as file:
        json.dump(item_list, file)



#new_list = list_generate("Small Round Shield ", 1, 100, 1)
#print(new_list)
#create_category("Spirits")
# insert_item(Cloth_Armor_List, "Armors")
#remove_item(new_list, "Familiars")
#insert_attribute(new_list, "Shields", "Shield_type", 'Small Round Shield')

def update_item(category, key, attribute):
    with open('./library/item_list.json', 'r') as file:
        item_list = json.load(file)
        file.close()
    for i in item_list[category]:
        if item_list[category][str(i)][str(key)] == attribute:
            item_list[category][str(i)]["slash_base"] = 1
            item_list[category][str(i)]["bash_base"] = 0
            item_list[category][str(i)]["pierce_base"] = 2
            item_list[category][str(i)]["magic_base"] = 0
            item_list[category][str(i)]["fire_base"] = 0
            item_list[category][str(i)]["water_base"] = 0
            item_list[category][str(i)]["air_base"] = 0
            item_list[category][str(i)]["earth_base"] = 0
            item_list[category][str(i)]["str_growth"] = 10
            item_list[category][str(i)]["dex_growth"] = 6
            item_list[category][str(i)]["con_growth"] = 0
            item_list[category][str(i)]["int_growth"] = 0
            item_list[category][str(i)]["wis_growth"] = 0
            item_list[category][str(i)]["cha_growth"] = 0
            item_list[category][str(i)]["luc_growth"] = 0
            item_list[category][str(i)]["defense_growth"] = 0
            item_list[category][str(i)]["defense_static"] = 0
            item_list[category][str(i)]["str_static"] = random.randint(0, 1)
            item_list[category][str(i)]["dex_static"] = random.randint(0, 1)
            item_list[category][str(i)]["con_static"] = random.randint(0, 1)
            item_list[category][str(i)]["int_static"] = random.randint(0, 1)
            item_list[category][str(i)]["wis_static"] = random.randint(0, 1)
            item_list[category][str(i)]["cha_static"] = random.randint(0, 1)
            item_list[category][str(i)]["luc_static"] = random.randint(0, 1)
            item_list[category][str(i)]["enhancement"] = 0
            item_list[category][str(i)]["species_affinity"] = ""
            item_list[category][str(i)]["capture"] = ""



    with open('./library/item_list.json', 'w') as file:
        json.dump(item_list, file)

#update_item("Weapons", "Weapon_type", "Chiania Long Arm Blade")
#update_item("Weapons", "Weapon_type", "Knife")
#update_item("Weapons", "Weapon_type", "Halberd")