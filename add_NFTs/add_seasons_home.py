def modify_item_attributes():
    with open('./library/item_list.json', 'r') as file:
        item_list = json.load(file)
        file.close()

    for i in item_list:
        if item_list[i]["collection_name"] == "Seasons Home":
                item_list[i]["item_type"] = "house"
                if item_list[i]["on-chain-attributes"]["1"]["value"] == "Spring":
                    item_list[i]["in-game-attributes"]["0"] = {}
                    item_list[i]["in-game-attributes"]["0"]["type"] = "buff_str"
                    item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["0"]["value"] = 5
                    item_list[i]["in-game-attributes"]["0"]["buff_requirement"] = "home_stay"
                    item_list[i]["in-game-attributes"]["0"]["home_stay"] = 480
                    item_list[i]["in-game-attributes"]["0"]["buff_duration"] = 60
                if item_list[i]["on-chain-attributes"]["1"]["value"] == "Summer":
                    item_list[i]["in-game-attributes"]["0"] = {}
                    item_list[i]["in-game-attributes"]["0"]["type"] = "buff_dex"
                    item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["0"]["value"] = 5
                    item_list[i]["in-game-attributes"]["0"]["buff_requirement"] = "home_stay"
                    item_list[i]["in-game-attributes"]["0"]["home_stay"] = 480
                    item_list[i]["in-game-attributes"]["0"]["buff_duration"] = 60
                if item_list[i]["on-chain-attributes"]["1"]["value"] == "Autumn":
                    item_list[i]["in-game-attributes"]["0"] = {}
                    item_list[i]["in-game-attributes"]["0"]["type"] = "buff_con"
                    item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["0"]["value"] = 5
                    item_list[i]["in-game-attributes"]["0"]["buff_requirement"] = "home_stay"
                    item_list[i]["in-game-attributes"]["0"]["home_stay"] = 480
                    item_list[i]["in-game-attributes"]["0"]["buff_duration"] = 60
                if item_list[i]["on-chain-attributes"]["1"]["value"] == "Winter":
                    item_list[i]["in-game-attributes"]["0"] = {}
                    item_list[i]["in-game-attributes"]["0"]["type"] = "buff_int"
                    item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                    item_list[i]["in-game-attributes"]["0"]["value"] = 5
                    item_list[i]["in-game-attributes"]["0"]["buff_requirement"] = "home_stay"
                    item_list[i]["in-game-attributes"]["0"]["home_stay"] = 480
                    item_list[i]["in-game-attributes"]["0"]["buff_duration"] = 60

    with open('./library/item_list.json', 'w') as file:
        json.dump(item_list, file)
