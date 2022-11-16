def modify_item_attributes():
    with open('./library/item_list.json', 'r') as file:
        item_list = json.load(file)
        file.close()
    print("read db")
    body_list = []
    jewelry_list = []
    hair_list = []
    clothes_list = []
    for i in item_list.copy():
        print(i)
        if item_list[i]["in-game-attributes"].get("enhancement") == None:
            item_list[i]["in-game-attributes"]["enhancement"] = {}
            item_list[i]["in-game-attributes"]["enhancement"]["type"] = "enhancement"
            item_list[i]["in-game-attributes"]["enhancement"]["value"] = 0

        if item_list[i]["collection_name"] == "Freckle Girls II":
            item_list[i]["item_type"] = "portrait"

            for trait in item_list[i]["on-chain-attributes"]:
                trait_type = item_list[i]["on-chain-attributes"][trait].get("trait_type")
                if trait_type == "hair":
                    trait_value = item_list[i]["on-chain-attributes"][trait].get("value")
                    if trait_value not in hair_list:
                        hair_list.append(trait_value)
                    if trait_value == 'silver snow':
                        item_list[i]["in-game-attributes"]["hair_effect"] = {}
                        item_list[i]["in-game-attributes"]["hair_effect"]["type"] = "increase_wis"
                        item_list[i]["in-game-attributes"]["hair_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["hair_effect"]["value"] = 5
                    if trait_value == 'blue fireworks':
                        item_list[i]["in-game-attributes"]["hair_effect"] = {}
                        item_list[i]["in-game-attributes"]["hair_effect"]["type"] = "increase_int"
                        item_list[i]["in-game-attributes"]["hair_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["hair_effect"]["value"] = 5
                    if trait_value == 'deep blue':
                        item_list[i]["in-game-attributes"]["hair_effect"] = {}
                        item_list[i]["in-game-attributes"]["hair_effect"]["type"] = "increase_int"
                        item_list[i]["in-game-attributes"]["hair_effect"]["factor"] = "constant"
                        item_list[i]["in-game-attributes"]["hair_effect"]["value"] = 2
                    if trait_value == 'chunli':
                        item_list[i]["in-game-attributes"]["hair_effect"] = {}
                        item_list[i]["in-game-attributes"]["hair_effect"]["type"] = "increase_luc"
                        item_list[i]["in-game-attributes"]["hair_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["hair_effect"]["value"] = 5
                    if trait_value == 'booming':
                        item_list[i]["in-game-attributes"]["hair_effect"] = {}
                        item_list[i]["in-game-attributes"]["hair_effect"]["type"] = "increase_str"
                        item_list[i]["in-game-attributes"]["hair_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["hair_effect"]["value"] = 5
                    if trait_value == 'cat ear afro':
                        item_list[i]["in-game-attributes"]["hair_effect"] = {}
                        item_list[i]["in-game-attributes"]["hair_effect"]["type"] = "increase_dex"
                        item_list[i]["in-game-attributes"]["hair_effect"]["factor"] = "constant"
                        item_list[i]["in-game-attributes"]["hair_effect"]["value"] = 5
                    if trait_value == 'emerald green':
                        item_list[i]["in-game-attributes"]["hair_effect"] = {}
                        item_list[i]["in-game-attributes"]["hair_effect"]["type"] = "increase_dex"
                        item_list[i]["in-game-attributes"]["hair_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["hair_effect"]["value"] = 5

                if trait_type == "jewelry":
                    trait_value = item_list[i]["on-chain-attributes"][trait].get("value")
                    if trait_value not in jewelry_list:
                        jewelry_list.append(trait_value)
                    if trait_value == 'sapphire':
                        item_list[i]["in-game-attributes"]["jewelry_effect"] = {}
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["type"] = "increase_int"
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["value"] = 5
                    if trait_value == 'white pearl':
                        item_list[i]["in-game-attributes"]["jewelry_effect"] = {}
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["type"] = "increase_wis"
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["value"] = 5
                    if trait_value == 'emerald':
                        item_list[i]["in-game-attributes"]["jewelry_effect"] = {}
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["type"] = "increase_dex"
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["value"] = 5
                    if trait_value == 'spike':
                        item_list[i]["in-game-attributes"]["jewelry_effect"] = {}
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["type"] = "increase_pierce"
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["value"] = 2
                    if trait_value == 'topaz':
                        item_list[i]["in-game-attributes"]["jewelry_effect"] = {}
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["type"] = "increase_con"
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["value"] = 5
                    if trait_value == 'ruby':
                        item_list[i]["in-game-attributes"]["jewelry_effect"] = {}
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["type"] = "increase_str"
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["value"] = 5
                    if trait_value == 'dark ruby':
                        item_list[i]["in-game-attributes"]["jewelry_effect"] = {}
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["type"] = "increase_str"
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["factor"] = "constant"
                        item_list[i]["in-game-attributes"]["jewelry_effect"]["value"] = 3

                if trait_type == "clothes":
                    trait_value = item_list[i]["on-chain-attributes"][trait].get("value")
                    if trait_value not in clothes_list:
                        clothes_list.append(trait_value)

                if trait_type == "body":
                    trait_value = item_list[i]["on-chain-attributes"][trait].get("value")
                    if trait_value not in body_list:
                        body_list.append(trait_value)
                    if trait_value == 'chocolate powder':
                        item_list[i]["in-game-attributes"]["body_effect"] = {}
                        item_list[i]["in-game-attributes"]["body_effect"]["type"] = "increase_defense"
                        item_list[i]["in-game-attributes"]["body_effect"]["factor"] = "constant"
                        item_list[i]["in-game-attributes"]["body_effect"]["value"] = 1
                    if trait_value == 'clear water green':
                        item_list[i]["in-game-attributes"]["body_effect"] = {}
                        item_list[i]["in-game-attributes"]["body_effect"]["type"] = "increase_int"
                        item_list[i]["in-game-attributes"]["body_effect"]["factor"] = "constant"
                        item_list[i]["in-game-attributes"]["body_effect"]["value"] = 1
                    if trait_value == 'black grapes':
                        item_list[i]["in-game-attributes"]["body_effect"] = {}
                        item_list[i]["in-game-attributes"]["body_effect"]["type"] = "increase_wis"
                        item_list[i]["in-game-attributes"]["body_effect"]["factor"] = "constant"
                        item_list[i]["in-game-attributes"]["body_effect"]["value"] = 1
                    if trait_value == 'bright pink':
                        item_list[i]["in-game-attributes"]["body_effect"] = {}
                        item_list[i]["in-game-attributes"]["body_effect"]["type"] = "increase_cha"
                        item_list[i]["in-game-attributes"]["body_effect"]["factor"] = "constant"
                        item_list[i]["in-game-attributes"]["body_effect"]["value"] = 1
                    if trait_value == 'caramel':
                        item_list[i]["in-game-attributes"]["body_effect"] = {}
                        item_list[i]["in-game-attributes"]["body_effect"]["type"] = "increase_health"
                        item_list[i]["in-game-attributes"]["body_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["body_effect"]["value"] = 5
                    if trait_value == 'earth blue':
                        item_list[i]["in-game-attributes"]["body_effect"] = {}
                        item_list[i]["in-game-attributes"]["body_effect"]["type"] = "increase_int"
                        item_list[i]["in-game-attributes"]["body_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["body_effect"]["value"] = 5
                    if trait_value == 'fiery rabbit':
                        item_list[i]["in-game-attributes"]["body_effect"] = {}
                        item_list[i]["in-game-attributes"]["body_effect"]["type"] = "increase_luc"
                        item_list[i]["in-game-attributes"]["body_effect"]["factor"] = "random"
                        item_list[i]["in-game-attributes"]["body_effect"]["value"] = 5



    print(hair_list)
    print(jewelry_list)
    print(clothes_list)
    print(body_list)




    with open('./library/item_list.json', 'w') as file:
        json.dump(item_list, file)
