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

        if item_list[i]["collection_name"] == "Chreatures":
            print("Chreatures = mount")
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
                if item_list[i]["on-chain-attributes"][j].get("trait_type") == "Antlers":
                    antler = item_list[i]["on-chain-attributes"][j].get("value")
                    if antler in ['Small', 'Small (Mold)']:
                        antler = 'Small'
                    if antler in ['Medium (Mold)', 'Medium', 'Medium (Vines)']:
                        antler = 'Medium'
                    if antler in ['Majestic', 'Majestic (Mold)', 'Majestic (Vines)']:
                        antler = 'Majestic'

                if item_list[i]["on-chain-attributes"][j].get("trait_type") == "Accessory":
                    accessory = item_list[i]["on-chain-attributes"][j].get("value")
                    if accessory in ['Slime', 'Slime&Glitch']:
                        accessory = "Slime"
                    if accessory in ['Bandage', 'Bandana (Purple)', 'Bandana (Red)']:
                        accessory = "Bandage"
                    if accessory in ['Arrow', 'Glitch', 'Arrow&Glitch']:
                        accessory = "Arrow"
                    if accessory in ["Laser"]:
                        accessory = "Laser"

                if item_list[i]["on-chain-attributes"][j].get("trait_type") == "Eye":
                    eye = item_list[i]["on-chain-attributes"][j].get("value")
                    if eye in ['Slime', 'Slime%Laser']:
                        eye = 'Slime'
                    if eye in ["Laser"]:
                        eye = "Laser"
                    if eye in ['Emerald', 'Emerald (Blink)']:
                        eye = 'Emerald'
                    if eye in ['Yellow', 'Yellow (Blink)']:
                        eye = 'Yellow'
                    if eye in ['Blue']:
                        eye = 'Blue'
                    if eye in ['White', 'White (Blink)']:
                        eye = 'White'
                    if eye in ['Pink (Blink)', 'Pink']:
                        eye = 'Pink'
                    if eye in ['Black']:
                        eye = 'Black'

                if item_list[i]["on-chain-attributes"][j].get("trait_type") == "Hooves":
                    hooves = item_list[i]["on-chain-attributes"][j].get("value")
                    if hooves in ['Black (Flashy)', 'Grey (Flashy)', 'Fern (Flashy)', 'Pink (Flashy)', 'Grey (Flashy']:
                        hooves = 'Flashy'

            print(feature_list)
            if antler == "Small":
                item_list[i]["in-game-attributes"]["antler_effect_1"] = {}
                item_list[i]["in-game-attributes"]["antler_effect_1"]["type"] = "increase_dex"
                item_list[i]["in-game-attributes"]["antler_effect_1"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["antler_effect_1"]["value"] = 5
            if antler == "Medium":
                item_list[i]["in-game-attributes"]["antler_effect_1"] = {}
                item_list[i]["in-game-attributes"]["antler_effect_1"]["type"] = "increase_dex"
                item_list[i]["in-game-attributes"]["antler_effect_1"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["antler_effect_1"]["value"] = 3
                item_list[i]["in-game-attributes"]["antler_effect_2"] = {}
                item_list[i]["in-game-attributes"]["antler_effect_2"]["type"] = "increase_str"
                item_list[i]["in-game-attributes"]["antler_effect_2"]["factor"] = "constant"
                item_list[i]["in-game-attributes"]["antler_effect_2"]["value"] = 1
            if antler == "Majestic":
                item_list[i]["in-game-attributes"]["antler_effect_1"] = {}
                item_list[i]["in-game-attributes"]["antler_effect_1"]["type"] = "increase_dex"
                item_list[i]["in-game-attributes"]["antler_effect_1"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["antler_effect_1"]["value"] = 3
                item_list[i]["in-game-attributes"]["antler_effect_2"] = {}
                item_list[i]["in-game-attributes"]["antler_effect_2"]["type"] = "increase_str"
                item_list[i]["in-game-attributes"]["antler_effect_2"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["antler_effect_2"]["value"] = 5

            if accessory == "Slime":
                item_list[i]["in-game-attributes"]["accessory_effect_1"] = {}
                item_list[i]["in-game-attributes"]["accessory_effect_1"]["type"] = "increase_luc"
                item_list[i]["in-game-attributes"]["accessory_effect_1"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["accessory_effect_1"]["value"] = 5
            if accessory == "Bandage":
                item_list[i]["in-game-attributes"]["accessory_effect_1"] = {}
                item_list[i]["in-game-attributes"]["accessory_effect_1"]["type"] = "increase_health"
                item_list[i]["in-game-attributes"]["accessory_effect_1"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["accessory_effect_1"]["value"] = 5

            if eye == 'Slime':
                item_list[i]["in-game-attributes"]["eye_effect_1"] = {}
                item_list[i]["in-game-attributes"]["eye_effect_1"]["type"] = "increase_luc"
                item_list[i]["in-game-attributes"]["eye_effect_1"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["eye_effect_1"]["value"] = 3
            if eye == "Laser":
                item_list[i]["in-game-attributes"]["eye_effect_1"] = {}
                item_list[i]["in-game-attributes"]["eye_effect_1"]["type"] = "increase_magic"
                item_list[i]["in-game-attributes"]["eye_effect_1"]["factor"] = "constant"
                item_list[i]["in-game-attributes"]["eye_effect_1"]["value"] = 1
            if eye == 'Emerald':
                item_list[i]["in-game-attributes"]["eye_effect_1"] = {}
                item_list[i]["in-game-attributes"]["eye_effect_1"]["type"] = "increase_dex"
                item_list[i]["in-game-attributes"]["eye_effect_1"]["factor"] = "constant"
                item_list[i]["in-game-attributes"]["eye_effect_1"]["value"] = 1
            if eye == 'Yellow':
                item_list[i]["in-game-attributes"]["eye_effect_1"] = {}
                item_list[i]["in-game-attributes"]["eye_effect_1"]["type"] = "increase_con"
                item_list[i]["in-game-attributes"]["eye_effect_1"]["factor"] = "constant"
                item_list[i]["in-game-attributes"]["eye_effect_1"]["value"] = 1
            if eye == 'Blue':
                item_list[i]["in-game-attributes"]["eye_effect_1"] = {}
                item_list[i]["in-game-attributes"]["eye_effect_1"]["type"] = "increase_int"
                item_list[i]["in-game-attributes"]["eye_effect_1"]["factor"] = "constant"
                item_list[i]["in-game-attributes"]["eye_effect_1"]["value"] = 1
            if eye == 'White':
                item_list[i]["in-game-attributes"]["eye_effect_1"] = {}
                item_list[i]["in-game-attributes"]["eye_effect_1"]["type"] = "increase_wis"
                item_list[i]["in-game-attributes"]["eye_effect_1"]["factor"] = "constant"
                item_list[i]["in-game-attributes"]["eye_effect_1"]["value"] = 1
            if eye == 'Pink':
                item_list[i]["in-game-attributes"]["eye_effect_1"] = {}
                item_list[i]["in-game-attributes"]["eye_effect_1"]["type"] = "increase_cha"
                item_list[i]["in-game-attributes"]["eye_effect_1"]["factor"] = "constant"
                item_list[i]["in-game-attributes"]["eye_effect_1"]["value"] = 1
            if eye == 'Black':
                item_list[i]["in-game-attributes"]["eye_effect_1"] = {}
                item_list[i]["in-game-attributes"]["eye_effect_1"]["type"] = "increase_str"
                item_list[i]["in-game-attributes"]["eye_effect_1"]["factor"] = "constant"
                item_list[i]["in-game-attributes"]["eye_effect_1"]["value"] = 1

            if hooves == 'Flashy':
                item_list[i]["in-game-attributes"]["hooves_effect_1"] = {}
                item_list[i]["in-game-attributes"]["hooves_effect_1"]["type"] = "increase_dex"
                item_list[i]["in-game-attributes"]["hooves_effect_1"]["factor"] = "constant"
                item_list[i]["in-game-attributes"]["hooves_effect_1"]["value"] = 1

            attr_list = ["increase_str", "increase_dex", "increase_con", "increase_int", "increase_wis", "increase_cha",
                         "increase_luc"]
            item_list[i]["in-game-attributes"]["random_attribute"] = {}
            item_list[i]["in-game-attributes"]["random_attribute"]["type"] = choice(attr_list)
            item_list[i]["in-game-attributes"]["random_attribute"]["factor"] = "constant"
            item_list[i]["in-game-attributes"]["random_attribute"]["value"] = randint(10, 11) / 10
            item_list[i]["in-game-attributes"]["mount_attribute"] = {}
            item_list[i]["in-game-attributes"]["mount_attribute"]["type"] = "mount_stamina"
            item_list[i]["in-game-attributes"]["mount_attribute"]["value"] = randint(100, 120)


    with open('./library/item_list.json', 'w') as file:
        json.dump(item_list, file)
