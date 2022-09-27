def modify_item_attributes():
    with open('./library/item_list.json', 'r') as file:
        item_list = json.load(file)
        file.close()

    for i in item_list:
        if item_list[i]["collection_name"] == "open box":
                item_list[i]["item_type"] = "producer"
                item_list[i]["in-game-attributes"]["0"] = {}
                item_list[i]["in-game-attributes"]["0"]["type"] = "produce_item"
                item_list[i]["in-game-attributes"]["0"]["factor"] = "Common Lootbox"
                item_list[i]["in-game-attributes"]["0"]["value"] = 1

    with open('./library/item_list.json', 'w') as file:
        json.dump(item_list, file)
