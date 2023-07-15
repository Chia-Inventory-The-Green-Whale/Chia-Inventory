def modify_item_attributes():
    with open('./library/item_list.json', 'r') as file:
        item_list = json.load(file)
        file.close()

    for i in item_list:
        if item_list[i]["collection_name"] == "Haunted Home":
                item_list[i]["item_type"] = "house"
                item_list[i]["in-game-attributes"]["0"] = {}
                item_list[i]["in-game-attributes"]["0"]["type"] = "buff_cha"
                item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["0"]["value"] = 5
                item_list[i]["in-game-attributes"]["0"]["buff_requirement"] = "home_stay"
                item_list[i]["in-game-attributes"]["0"]["home_stay"] = 480
                item_list[i]["in-game-attributes"]["0"]["buff_duration"] = 60


    with open('./library/item_list.json', 'w') as file:
        json.dump(item_list, file)
