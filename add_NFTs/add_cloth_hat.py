def modify_item_attributes():
    with open('./library/item_list.json', 'r') as file:
        item_list = json.load(file)
        file.close()
    print("read db")
    for i in item_list.copy():
        if item_list[i]["in-game-attributes"].get("enhancement") == None:
            item_list[i]["in-game-attributes"]["enhancement"] = {}
            item_list[i]["in-game-attributes"]["enhancement"]["type"] = "enhancement"
            item_list[i]["in-game-attributes"]["enhancement"]["value"] = 0

        if item_list[i]["collection_name"] == "Chia Inventory":
            if item_list[i]["on-chain-attributes"].get("0") != None:
                if item_list[i]["on-chain-attributes"]["0"].get("value") == "hat":
                    item_list[i]["item_type"] = "hat"
                    name_args = item_list[i]["item_name"].split()
                    number = name_args[4][:-1]
                    item_list[i][
                        "icon"] = "https://bafybeiemr53c7xu67fwvgo3p3cv33orahl5bhphjontlkzxbex64ouqrcm.ipfs.nftstorage.link/" + str(
                        number) + ".gif"
                    item_list[i]["in-game-attributes"]["basic1"] = {}
                    item_list[i]["in-game-attributes"]["basic1"]["type"] = "increase_defense"
                    item_list[i]["in-game-attributes"]["basic1"]["factor"] = "constant"
                    item_list[i]["in-game-attributes"]["basic1"]["value"] = 1
                    item_list[i]["in-game-attributes"]["basic2"] = {}
                    item_list[i]["in-game-attributes"]["basic2"]["type"] = "increase_health"
                    item_list[i]["in-game-attributes"]["basic2"]["factor"] = "level_scale"
                    item_list[i]["in-game-attributes"]["basic2"]["value"] = 10
                    item_list[i]["in-game-attributes"]["basic3"] = {}
                    item_list[i]["in-game-attributes"]["basic3"]["type"] = "increase_dex"
                    item_list[i]["in-game-attributes"]["basic3"]["factor"] = "level_scale"
                    item_list[i]["in-game-attributes"]["basic3"]["value"] = 8
                    decoration = item_list[i]["on-chain-attributes"]["6"].get("value")
                    print(decoration)
                    if decoration in ["yellow feather"]:
                        item_list[i]["in-game-attributes"]["decoration_effect"] = {}
                        item_list[i]["in-game-attributes"]["decoration_effect"]["type"] = "increase_luc"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["value"] = 5
                    if decoration in ["red feather"]:
                        item_list[i]["in-game-attributes"]["decoration_effect"] = {}
                        item_list[i]["in-game-attributes"]["decoration_effect"]["type"] = "increase_str"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["value"] = 5
                    if decoration in ["blue feather"]:
                        item_list[i]["in-game-attributes"]["decoration_effect"] = {}
                        item_list[i]["in-game-attributes"]["decoration_effect"]["type"] = "increase_int"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["value"] = 5
                    if decoration in ["green feather"]:
                        item_list[i]["in-game-attributes"]["decoration_effect"] = {}
                        item_list[i]["in-game-attributes"]["decoration_effect"]["type"] = "increase_dex"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["value"] = 5
                    if decoration in ["green bird"]:
                        item_list[i]["in-game-attributes"]["decoration_effect"] = {}
                        item_list[i]["in-game-attributes"]["decoration_effect"]["type"] = "increase_dex"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["factor"] = "constant"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["value"] = 2
                    if decoration in ["orange bird"]:
                        item_list[i]["in-game-attributes"]["decoration_effect"] = {}
                        item_list[i]["in-game-attributes"]["decoration_effect"]["type"] = "increase_con"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["factor"] = "constant"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["value"] = 2
                    if decoration in ["blue bird"]:
                        item_list[i]["in-game-attributes"]["decoration_effect"] = {}
                        item_list[i]["in-game-attributes"]["decoration_effect"]["type"] = "increase_int"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["factor"] = "constant"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["value"] = 2
                    if decoration in ["brown bird"]:
                        item_list[i]["in-game-attributes"]["decoration_effect"] = {}
                        item_list[i]["in-game-attributes"]["decoration_effect"]["type"] = "increase_luc"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["factor"] = "constant"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["value"] = 2
                    if decoration in ["sword medal"]:
                        item_list[i]["in-game-attributes"]["decoration_effect"] = {}
                        item_list[i]["in-game-attributes"]["decoration_effect"]["type"] = "increase_slash"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["value"] = 3
                    if decoration in ["round medal"]:
                        item_list[i]["in-game-attributes"]["decoration_effect"] = {}
                        item_list[i]["in-game-attributes"]["decoration_effect"]["type"] = "increase_health"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["value"] = 8
                    if decoration in ["shield medal"]:
                        item_list[i]["in-game-attributes"]["decoration_effect"] = {}
                        item_list[i]["in-game-attributes"]["decoration_effect"]["type"] = "increase_defense"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["decoration_effect"]["value"] = 3
                    attr_list = ["increase_str", "increase_dex", "increase_con", "increase_int", "increase_wis",
                                 "increase_cha",
                                 "increase_luc"]
                    item_list[i]["in-game-attributes"]["random_attribute"] = {}
                    item_list[i]["in-game-attributes"]["random_attribute"]["type"] = choice(attr_list)
                    item_list[i]["in-game-attributes"]["random_attribute"]["factor"] = "constant"
                    item_list[i]["in-game-attributes"]["random_attribute"]["value"] = randint(10, 11) / 10
    with open('./library/item_list.json', 'w') as file:
        json.dump(item_list, file)
