def modify_item_attributes():
    with open('./library/item_list.json', 'r') as file:
        item_list = json.load(file)
        file.close()
    print("read db")
    feature_list = []
    for i in item_list.copy():
        if item_list[i]["in-game-attributes"].get("enhancement") == None:
            item_list[i]["in-game-attributes"]["enhancement"] = {}
            item_list[i]["in-game-attributes"]["enhancement"]["type"] = "enhancement"
            item_list[i]["in-game-attributes"]["enhancement"]["value"] = 0

        if item_list[i]["collection_name"] == "Chia Mounts":
            print("Chia Mounts = mount")
            if item_list[i]["in-game-attributes"].get("0") != None:
                item_list[i]["in-game-attributes"].pop("0")
            if item_list[i]["in-game-attributes"].get("1") != None:
                item_list[i]["in-game-attributes"].pop("1")
            if item_list[i]["in-game-attributes"].get("2") != None:
                item_list[i]["in-game-attributes"].pop("2")
            if item_list[i]["in-game-attributes"].get("3") != None:
                item_list[i]["in-game-attributes"].pop("3")

            item_list[i]["item_type"] = "mount"

            for j in item_list[i]["on-chain-attributes"]:
                if item_list[i]["on-chain-attributes"][j].get("trait_type") == "Species":
                    species = item_list[i]["on-chain-attributes"][j].get("value")
                    if species in ['dragon']:
                        species = 'dragon'
                    if species in ['warsheep']:
                        species = 'warsheep'
                    if species in ['nightsaber']:
                        species = 'nightsaber'
                    if species in ['magic marmot']:
                        species = 'magic marmot'

            print(feature_list)
            if species == "dragon":
                item_list[i]["in-game-attributes"]["species_effect_1"] = {}
                item_list[i]["in-game-attributes"]["species_effect_1"]["type"] = "increase_defense"
                item_list[i]["in-game-attributes"]["species_effect_1"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_1"]["value"] = 3
                item_list[i]["in-game-attributes"]["species_effect_2"] = {}
                item_list[i]["in-game-attributes"]["species_effect_2"]["type"] = "increase_bash"
                item_list[i]["in-game-attributes"]["species_effect_2"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_2"]["value"] = 1
                item_list[i]["in-game-attributes"]["species_effect_3"] = {}
                item_list[i]["in-game-attributes"]["species_effect_3"]["type"] = "increase_dex"
                item_list[i]["in-game-attributes"]["species_effect_3"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_3"]["value"] = 5
                item_list[i]["in-game-attributes"]["species_effect_4"] = {}
                item_list[i]["in-game-attributes"]["species_effect_4"]["type"] = "increase_str"
                item_list[i]["in-game-attributes"]["species_effect_4"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_4"]["value"] = 2
                item_list[i]["in-game-attributes"]["species_effect_5"] = {}
                item_list[i]["in-game-attributes"]["species_effect_5"]["type"] = "increase_wis"
                item_list[i]["in-game-attributes"]["species_effect_5"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_5"]["value"] = 2
                item_list[i]["in-game-attributes"]["species_effect_6"] = {}
                item_list[i]["in-game-attributes"]["species_effect_6"]["type"] = "increase_luc"
                item_list[i]["in-game-attributes"]["species_effect_6"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_6"]["value"] = 3

            if species == "warsheep":
                item_list[i]["in-game-attributes"]["species_effect_1"] = {}
                item_list[i]["in-game-attributes"]["species_effect_1"]["type"] = "increase_defense"
                item_list[i]["in-game-attributes"]["species_effect_1"]["factor"] = "constant"
                item_list[i]["in-game-attributes"]["species_effect_1"]["value"] = 1
                item_list[i]["in-game-attributes"]["species_effect_2"] = {}
                item_list[i]["in-game-attributes"]["species_effect_2"]["type"] = "increase_con"
                item_list[i]["in-game-attributes"]["species_effect_2"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_2"]["value"] = 5
                item_list[i]["in-game-attributes"]["species_effect_3"] = {}
                item_list[i]["in-game-attributes"]["species_effect_3"]["type"] = "increase_dex"
                item_list[i]["in-game-attributes"]["species_effect_3"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_3"]["value"] = 3
                item_list[i]["in-game-attributes"]["species_effect_4"] = {}
                item_list[i]["in-game-attributes"]["species_effect_4"]["type"] = "increase_str"
                item_list[i]["in-game-attributes"]["species_effect_4"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_4"]["value"] = 2
                item_list[i]["in-game-attributes"]["species_effect_5"] = {}
                item_list[i]["in-game-attributes"]["species_effect_5"]["type"] = "increase_wis"
                item_list[i]["in-game-attributes"]["species_effect_5"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_5"]["value"] = 1
                item_list[i]["in-game-attributes"]["species_effect_6"] = {}
                item_list[i]["in-game-attributes"]["species_effect_6"]["type"] = "increase_luc"
                item_list[i]["in-game-attributes"]["species_effect_6"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_6"]["value"] = 2

            if species == "nightsaber":
                item_list[i]["in-game-attributes"]["species_effect_1"] = {}
                item_list[i]["in-game-attributes"]["species_effect_1"]["type"] = "increase_defense"
                item_list[i]["in-game-attributes"]["species_effect_1"]["factor"] = "constant"
                item_list[i]["in-game-attributes"]["species_effect_1"]["value"] = 1
                item_list[i]["in-game-attributes"]["species_effect_2"] = {}
                item_list[i]["in-game-attributes"]["species_effect_2"]["type"] = "increase_slash"
                item_list[i]["in-game-attributes"]["species_effect_2"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_2"]["value"] = 1
                item_list[i]["in-game-attributes"]["species_effect_3"] = {}
                item_list[i]["in-game-attributes"]["species_effect_3"]["type"] = "increase_dex"
                item_list[i]["in-game-attributes"]["species_effect_3"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_3"]["value"] = 6
                item_list[i]["in-game-attributes"]["species_effect_4"] = {}
                item_list[i]["in-game-attributes"]["species_effect_4"]["type"] = "increase_str"
                item_list[i]["in-game-attributes"]["species_effect_4"]["factor"] = "constant"
                item_list[i]["in-game-attributes"]["species_effect_4"]["value"] = 1
                item_list[i]["in-game-attributes"]["species_effect_5"] = {}
                item_list[i]["in-game-attributes"]["species_effect_5"]["type"] = "increase_wis"
                item_list[i]["in-game-attributes"]["species_effect_5"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_5"]["value"] = 2
                item_list[i]["in-game-attributes"]["species_effect_6"] = {}
                item_list[i]["in-game-attributes"]["species_effect_6"]["type"] = "increase_luc"
                item_list[i]["in-game-attributes"]["species_effect_6"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_6"]["value"] = 2

            if species == "magic marmot":
                item_list[i]["in-game-attributes"]["species_effect_1"] = {}
                item_list[i]["in-game-attributes"]["species_effect_1"]["type"] = "increase_defense"
                item_list[i]["in-game-attributes"]["species_effect_1"]["factor"] = "constant"
                item_list[i]["in-game-attributes"]["species_effect_1"]["value"] = 1
                item_list[i]["in-game-attributes"]["species_effect_2"] = {}
                item_list[i]["in-game-attributes"]["species_effect_2"]["type"] = "increase_pierce"
                item_list[i]["in-game-attributes"]["species_effect_2"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_2"]["value"] = 1
                item_list[i]["in-game-attributes"]["species_effect_3"] = {}
                item_list[i]["in-game-attributes"]["species_effect_3"]["type"] = "increase_dex"
                item_list[i]["in-game-attributes"]["species_effect_3"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_3"]["value"] = 2
                item_list[i]["in-game-attributes"]["species_effect_4"] = {}
                item_list[i]["in-game-attributes"]["species_effect_4"]["type"] = "increase_str"
                item_list[i]["in-game-attributes"]["species_effect_4"]["factor"] = "constant"
                item_list[i]["in-game-attributes"]["species_effect_4"]["value"] = 2
                item_list[i]["in-game-attributes"]["species_effect_5"] = {}
                item_list[i]["in-game-attributes"]["species_effect_5"]["type"] = "increase_wis"
                item_list[i]["in-game-attributes"]["species_effect_5"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_5"]["value"] = 5
                item_list[i]["in-game-attributes"]["species_effect_6"] = {}
                item_list[i]["in-game-attributes"]["species_effect_6"]["type"] = "increase_luc"
                item_list[i]["in-game-attributes"]["species_effect_6"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["species_effect_6"]["value"] = 3

            attr_list = ["increase_str", "increase_dex", "increase_con", "increase_int", "increase_wis", "increase_cha",
                         "increase_luc"]
            item_list[i]["in-game-attributes"]["random_attribute"] = {}
            item_list[i]["in-game-attributes"]["random_attribute"]["type"] = choice(attr_list)
            item_list[i]["in-game-attributes"]["random_attribute"]["factor"] = "constant"
            item_list[i]["in-game-attributes"]["random_attribute"]["value"] = randint(10, 11) / 10
            item_list[i]["in-game-attributes"]["mount_attribute"] = {}
            item_list[i]["in-game-attributes"]["mount_attribute"]["type"] = "mount_stamina"
            item_list[i]["in-game-attributes"]["mount_attribute"]["value"] = randint(100, 120)
