def modify_item_attributes():
    with open('./library/item_list.json', 'r') as file:
        item_list = json.load(file)
        file.close()

    for i in item_list:
        if item_list[i]["collection_name"] == "Balldog Collection":
            item_list[i]["item_type"] = "pet"
            attr_list = ["buff_str", "buff_dex", "buff_con", "buff_int", "buff_wis", "buff_cha", "buff_luc"]
            item_list[i]["in-game-attributes"]["0"] = {}
            item_list[i]["in-game-attributes"]["0"]["type"] = choice(attr_list)
            item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
            item_list[i]["in-game-attributes"]["0"]["value"] = 5
            item_list[i]["in-game-attributes"]["0"]["buff_requirement"] = "feed"
            item_list[i]["in-game-attributes"]["0"]["feed"] = "Dog Food"
            item_list[i]["in-game-attributes"]["0"]["buff_duration"] = 30
            item_list[i]["in-game-attributes"]["1"] = {}
            item_list[i]["in-game-attributes"]["1"]["type"] = choice(attr_list)
            item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
            item_list[i]["in-game-attributes"]["1"]["value"] = 5
            item_list[i]["in-game-attributes"]["1"]["buff_requirement"] = "feed"
            item_list[i]["in-game-attributes"]["1"]["feed"] = "Dog Food"
            item_list[i]["in-game-attributes"]["1"]["buff_duration"] = 30
        if item_list[i]["collection_name"] == "Balldog Collection":
            item_list[i]["item_type"] = "pet"
            attr_list = ["buff_str", "buff_dex", "buff_con", "buff_int", "buff_wis", "buff_cha", "buff_luc"]
            if item_list[i]["on-chain-attributes"].get("10") != None:
                if item_list[i]["on-chain-attributes"]["10"]["value"] == "Bloodstone":
                    item_list[i]["in-game-attributes"]["0"] = {}
                    item_list[i]["in-game-attributes"]["0"]["type"] = "buff_health"
                    item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["0"]["value"] = 5
                    item_list[i]["in-game-attributes"]["0"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["0"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["0"]["buff_duration"] = 30
                    item_list[i]["in-game-attributes"]["1"] = {}
                    item_list[i]["in-game-attributes"]["1"]["type"] = "buff_health"
                    item_list[i]["in-game-attributes"]["1"]["factor"] = "constant"
                    item_list[i]["in-game-attributes"]["1"]["value"] = 1
                    item_list[i]["in-game-attributes"]["1"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["1"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["1"]["buff_duration"] = 30
                if item_list[i]["on-chain-attributes"]["10"]["value"] == "Bobo":
                    item_list[i]["in-game-attributes"]["0"] = {}
                    item_list[i]["in-game-attributes"]["0"]["type"] = "buff_cha"
                    item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["0"]["value"] = 5
                    item_list[i]["in-game-attributes"]["0"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["0"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["0"]["buff_duration"] = 30
                    item_list[i]["in-game-attributes"]["1"] = {}
                    item_list[i]["in-game-attributes"]["1"]["type"] = "buff_cha"
                    item_list[i]["in-game-attributes"]["1"]["factor"] = "constant"
                    item_list[i]["in-game-attributes"]["1"]["value"] = 1
                    item_list[i]["in-game-attributes"]["1"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["1"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["1"]["buff_duration"] = 30
                if item_list[i]["on-chain-attributes"]["10"]["value"] == "Brain":
                    item_list[i]["in-game-attributes"]["0"] = {}
                    item_list[i]["in-game-attributes"]["0"]["type"] = "buff_int"
                    item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["0"]["value"] = 5
                    item_list[i]["in-game-attributes"]["0"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["0"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["0"]["buff_duration"] = 30
                    item_list[i]["in-game-attributes"]["1"] = {}
                    item_list[i]["in-game-attributes"]["1"]["type"] = "buff_wis"
                    item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["1"]["value"] = 5
                    item_list[i]["in-game-attributes"]["1"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["1"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["1"]["buff_duration"] = 30
                if item_list[i]["on-chain-attributes"]["10"]["value"] == "Chia":
                    item_list[i]["in-game-attributes"]["0"] = {}
                    item_list[i]["in-game-attributes"]["0"]["type"] = "buff_dex"
                    item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["0"]["value"] = 5
                    item_list[i]["in-game-attributes"]["0"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["0"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["0"]["buff_duration"] = 30
                    item_list[i]["in-game-attributes"]["1"] = {}
                    item_list[i]["in-game-attributes"]["1"]["type"] = "buff_dex"
                    item_list[i]["in-game-attributes"]["1"]["factor"] = "constant"
                    item_list[i]["in-game-attributes"]["1"]["value"] = 1
                    item_list[i]["in-game-attributes"]["1"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["1"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["1"]["buff_duration"] = 30
                if item_list[i]["on-chain-attributes"]["10"]["value"] == "Craze":
                    item_list[i]["in-game-attributes"]["0"] = {}
                    item_list[i]["in-game-attributes"]["0"]["type"] = "buff_str"
                    item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["0"]["value"] = 5
                    item_list[i]["in-game-attributes"]["0"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["0"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["0"]["buff_duration"] = 30
                    item_list[i]["in-game-attributes"]["1"] = {}
                    item_list[i]["in-game-attributes"]["1"]["type"] = choice(attr_list)
                    item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["1"]["value"] = 5
                    item_list[i]["in-game-attributes"]["1"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["1"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["1"]["buff_duration"] = 30
                if item_list[i]["on-chain-attributes"]["10"]["value"] == "Drgon Ball":
                    item_list[i]["in-game-attributes"]["0"] = {}
                    item_list[i]["in-game-attributes"]["0"]["type"] = choice(attr_list)
                    item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                    item_list[i]["in-game-attributes"]["0"]["value"] = 1
                    item_list[i]["in-game-attributes"]["0"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["0"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["0"]["buff_duration"] = 30
                    item_list[i]["in-game-attributes"]["1"] = {}
                    item_list[i]["in-game-attributes"]["1"]["type"] = choice(attr_list)
                    item_list[i]["in-game-attributes"]["1"]["factor"] = "constant"
                    item_list[i]["in-game-attributes"]["1"]["value"] = 1
                    item_list[i]["in-game-attributes"]["1"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["1"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["1"]["buff_duration"] = 30
                if item_list[i]["on-chain-attributes"]["10"]["value"] == "Melon":
                    item_list[i]["in-game-attributes"]["0"] = {}
                    item_list[i]["in-game-attributes"]["0"]["type"] = "buff_health"
                    item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["0"]["value"] = 1
                    item_list[i]["in-game-attributes"]["0"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["0"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["0"]["buff_duration"] = 30
                    item_list[i]["in-game-attributes"]["1"] = {}
                    item_list[i]["in-game-attributes"]["1"]["type"] = choice(attr_list)
                    item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["1"]["value"] = 1
                    item_list[i]["in-game-attributes"]["1"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["1"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["1"]["buff_duration"] = 30
                if item_list[i]["on-chain-attributes"]["10"]["value"] == "Mordor":
                    item_list[i]["in-game-attributes"]["0"] = {}
                    item_list[i]["in-game-attributes"]["0"]["type"] = "buff_int"
                    item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                    item_list[i]["in-game-attributes"]["0"]["value"] = 1
                    item_list[i]["in-game-attributes"]["0"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["0"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["0"]["buff_duration"] = 30
                    item_list[i]["in-game-attributes"]["1"] = {}
                    item_list[i]["in-game-attributes"]["1"]["type"] = "buff_int"
                    item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["1"]["value"] = 5
                    item_list[i]["in-game-attributes"]["1"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["1"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["1"]["buff_duration"] = 30
                if item_list[i]["on-chain-attributes"]["10"]["value"] == "Oblation":
                    item_list[i]["in-game-attributes"]["0"] = {}
                    item_list[i]["in-game-attributes"]["0"]["type"] = "buff_luc"
                    item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["0"]["value"] = 5
                    item_list[i]["in-game-attributes"]["0"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["0"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["0"]["buff_duration"] = 30
                    item_list[i]["in-game-attributes"]["1"] = {}
                    item_list[i]["in-game-attributes"]["1"]["type"] = "buff_luc"
                    item_list[i]["in-game-attributes"]["1"]["factor"] = "constant"
                    item_list[i]["in-game-attributes"]["1"]["value"] = 1
                    item_list[i]["in-game-attributes"]["1"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["1"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["1"]["buff_duration"] = 30
                if item_list[i]["on-chain-attributes"]["10"]["value"] == "Revenge":
                    item_list[i]["in-game-attributes"]["0"] = {}
                    item_list[i]["in-game-attributes"]["0"]["type"] = "buff_bash"
                    item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["0"]["value"] = 2
                    item_list[i]["in-game-attributes"]["0"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["0"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["0"]["buff_duration"] = 30
                    item_list[i]["in-game-attributes"]["1"] = {}
                    item_list[i]["in-game-attributes"]["1"]["type"] = "buff_str"
                    item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["1"]["value"] = 5
                    item_list[i]["in-game-attributes"]["1"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["1"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["1"]["buff_duration"] = 30
                if item_list[i]["on-chain-attributes"]["10"]["value"] == "Thor":
                    item_list[i]["in-game-attributes"]["0"] = {}
                    item_list[i]["in-game-attributes"]["0"]["type"] = "buff_pierce"
                    item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["0"]["value"] = 2
                    item_list[i]["in-game-attributes"]["0"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["0"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["0"]["buff_duration"] = 30
                    item_list[i]["in-game-attributes"]["1"] = {}
                    item_list[i]["in-game-attributes"]["1"]["type"] = "buff_dex"
                    item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["1"]["value"] = 5
                    item_list[i]["in-game-attributes"]["1"]["buff_requirement"] = "feed"
                    item_list[i]["in-game-attributes"]["1"]["feed"] = "Dog Food"
                    item_list[i]["in-game-attributes"]["1"]["buff_duration"] = 30
                    
    with open('./library/item_list.json', 'w') as file:
        json.dump(item_list, file)
