def modify_item_attributes():
    with open('./library/item_list.json', 'r') as file:
        item_list = json.load(file)
        file.close()
    print("read db")

    for i in item_list:
        if item_list[i]["collection_name"] == "Chia Slimes":
            print("Chia Slimes = familiar")
            item_list[i]["item_type"] = "familiar"
            for j in item_list[i]["on-chain-attributes"]:
                if item_list[i]["on-chain-attributes"][j].get("trait_type") == "Color":
                    color = item_list[i]["on-chain-attributes"][j].get("value")
                    if color in ["Alpha-Blue-0101b5", "T-Alpha-Blue-0101b5"]:
                        color = "Blue"
                    if color in ["Alpha-Green-00af29", "T-Alpha-Green-00af29", "Plant-CoolVine-25ae78",
                                 "Plant-DryGrass-72c83e15", "Plant-ForestShadow-3a6557",
                                 "Plant-HeartoftheForest-33652b", "Plant-MoreGreen-68a145", "Plant-Swamp-303d21",
                                 "Plant-Unnatural-155f01", "T-Plant-Unnatural-155f01"]:
                        color = "Green"
                    if color in ["Beta-Orange-ff9c01", "T-Beta-Orange-ff9c01"]:
                        color = "Orange"
                    if color in ["Beta-Purple-8401ff", "T-Beta-Purple-8401ff"]:
                        color = "Purple"
                    if color in ["Alpha-Red-d30000", "T-Alpha-Red-d30000"]:
                        color = "Red"
                    if color in ["Rock-GolemAdam-0c2d04-", "Rock-GolemAsh-565655", "Rock-GolemGray-565655",
                                 "Rock-GolemMith-0f1d4a-", "Rock-GolemObsid-3b215a", "Rock-MoltenIron-909596",
                                 "Rock-RockyBrown-5b482a", "Rock-RockyMuddy-725930"]:
                        color = "Rock"
                    if color in ["Water-Algae-269ac2", "Water-ClearBlue-1f9bf4", "Water-CrabKissed-9d628e",
                                 "Water-Murky-2c5b79", "Water-Ocean-4094d7", "Water-OctoInked-5963e8"]:
                        color = "Water"
                    if color in ["Beta-Yellow-fffc01", "T-Beta-Yellow-fffc01"]:
                        color = "Yellow"

                if item_list[i]["on-chain-attributes"][j].get("trait_type") == "Hidden Power":
                    hidden_power = item_list[i]["on-chain-attributes"][j].get("value")

                if item_list[i]["on-chain-attributes"][j].get("trait_type") == "Acs2":
                    asc = item_list[i]["on-chain-attributes"][j].get("value")

            if color == "Blue":
                item_list[i]["in-game-attributes"]["color_effect"] = {}
                item_list[i]["in-game-attributes"]["color_effect"]["type"] = "increase_int"
                item_list[i]["in-game-attributes"]["color_effect"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["color_effect"]["value"] = 5
            if color == "Green":
                item_list[i]["in-game-attributes"]["color_effect"] = {}
                item_list[i]["in-game-attributes"]["color_effect"]["type"] = "increase_dex"
                item_list[i]["in-game-attributes"]["color_effect"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["color_effect"]["value"] = 5
            if color == "Orange":
                item_list[i]["in-game-attributes"]["color_effect"] = {}
                item_list[i]["in-game-attributes"]["color_effect"]["type"] = "increase_con"
                item_list[i]["in-game-attributes"]["color_effect"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["color_effect"]["value"] = 5
            if color == "Purple":
                item_list[i]["in-game-attributes"]["color_effect"] = {}
                item_list[i]["in-game-attributes"]["color_effect"]["type"] = "increase_wis"
                item_list[i]["in-game-attributes"]["color_effect"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["color_effect"]["value"] = 5
            if color == "Red":
                item_list[i]["in-game-attributes"]["color_effect"] = {}
                item_list[i]["in-game-attributes"]["color_effect"]["type"] = "increase_str"
                item_list[i]["in-game-attributes"]["color_effect"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["color_effect"]["value"] = 5
            if color == "Rock":
                item_list[i]["in-game-attributes"]["color_effect"] = {}
                item_list[i]["in-game-attributes"]["color_effect"]["type"] = "increase_con"
                item_list[i]["in-game-attributes"]["color_effect"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["color_effect"]["value"] = 5
            if color == "Water":
                item_list[i]["in-game-attributes"]["color_effect"] = {}
                item_list[i]["in-game-attributes"]["color_effect"]["type"] = "increase_int"
                item_list[i]["in-game-attributes"]["color_effect"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["color_effect"]["value"] = 5
            if color == "Yellow":
                item_list[i]["in-game-attributes"]["color_effect"] = {}
                item_list[i]["in-game-attributes"]["color_effect"]["type"] = "increase_cha"
                item_list[i]["in-game-attributes"]["color_effect"]["factor"] = "random"
                item_list[i]["in-game-attributes"]["color_effect"]["value"] = 5
            if hidden_power == "Defensive Aura":
                item_list[i]["in-game-attributes"]["hidden_power_effect"] = {}
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["type"] = "increase_defense"
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["factor"] = "probability"
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["probability"] = 0.2
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["value"] = 2
            if hidden_power == "Heal":
                item_list[i]["in-game-attributes"]["hidden_power_effect"] = {}
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["type"] = "increase_health"
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["factor"] = "probability"
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["probability"] = 0.2
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["value"] = 8
            if hidden_power == "Identify":
                item_list[i]["in-game-attributes"]["hidden_power_effect"] = {}
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["type"] = "increase_int"
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["factor"] = "probability"
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["probability"] = 0.2
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["value"] = 5
            if hidden_power == "Slip Stream":
                item_list[i]["in-game-attributes"]["hidden_power_effect"] = {}
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["type"] = "increase_bash"
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["factor"] = "probability"
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["probability"] = 0.2
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["value"] = 2
            if hidden_power == "Stealth":
                item_list[i]["in-game-attributes"]["hidden_power_effect"] = {}
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["type"] = "increase_dex"
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["factor"] = "probability"
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["probability"] = 0.2
                item_list[i]["in-game-attributes"]["hidden_power_effect"]["value"] = 5
            if asc == "GolemSpikes":
                item_list[i]["in-game-attributes"]["asc_effect"] = {}
                item_list[i]["in-game-attributes"]["asc_effect"]["type"] = "increase_pierce"
                item_list[i]["in-game-attributes"]["asc_effect"]["factor"] = "probability"
                item_list[i]["in-game-attributes"]["asc_effect"]["probability"] = 0.2
                item_list[i]["in-game-attributes"]["asc_effect"]["value"] = 2
            if asc == "RockSpikes":
                item_list[i]["in-game-attributes"]["asc_effect"] = {}
                item_list[i]["in-game-attributes"]["asc_effect"]["type"] = "increase_pierce"
                item_list[i]["in-game-attributes"]["asc_effect"]["factor"] = "probability"
                item_list[i]["in-game-attributes"]["asc_effect"]["probability"] = 0.2
                item_list[i]["in-game-attributes"]["asc_effect"]["value"] = 2
            if asc == "VineWhips":
                item_list[i]["in-game-attributes"]["asc_effect"] = {}
                item_list[i]["in-game-attributes"]["asc_effect"]["type"] = "increase_slash"
                item_list[i]["in-game-attributes"]["asc_effect"]["factor"] = "probability"
                item_list[i]["in-game-attributes"]["asc_effect"]["probability"] = 0.2
                item_list[i]["in-game-attributes"]["asc_effect"]["value"] = 2
            if asc == "Apple":
                item_list[i]["in-game-attributes"]["asc_effect"] = {}
                item_list[i]["in-game-attributes"]["asc_effect"]["type"] = "produce_item"
                item_list[i]["in-game-attributes"]["asc_effect"]["factor"] = "Apple"
                item_list[i]["in-game-attributes"]["asc_effect"]["value"] = 0.25
            if asc == "Banana":
                item_list[i]["in-game-attributes"]["asc_effect"] = {}
                item_list[i]["in-game-attributes"]["asc_effect"]["type"] = "produce_item"
                item_list[i]["in-game-attributes"]["asc_effect"]["factor"] = "Banana"
                item_list[i]["in-game-attributes"]["asc_effect"]["value"] = 0.25
            if asc == "Grape":
                item_list[i]["in-game-attributes"]["asc_effect"] = {}
                item_list[i]["in-game-attributes"]["asc_effect"]["type"] = "produce_item"
                item_list[i]["in-game-attributes"]["asc_effect"]["factor"] = "Grape"
                item_list[i]["in-game-attributes"]["asc_effect"]["value"] = 0.25
            if asc == "Lemon":
                item_list[i]["in-game-attributes"]["asc_effect"] = {}
                item_list[i]["in-game-attributes"]["asc_effect"]["type"] = "produce_item"
                item_list[i]["in-game-attributes"]["asc_effect"]["factor"] = "Lemon"
                item_list[i]["in-game-attributes"]["asc_effect"]["value"] = 0.25
            if asc == "Mango":
                item_list[i]["in-game-attributes"]["asc_effect"] = {}
                item_list[i]["in-game-attributes"]["asc_effect"]["type"] = "produce_item"
                item_list[i]["in-game-attributes"]["asc_effect"]["factor"] = "Mango"
                item_list[i]["in-game-attributes"]["asc_effect"]["value"] = 0.25
            if asc == "Orange":
                item_list[i]["in-game-attributes"]["asc_effect"] = {}
                item_list[i]["in-game-attributes"]["asc_effect"]["type"] = "produce_item"
                item_list[i]["in-game-attributes"]["asc_effect"]["factor"] = "Orange"
                item_list[i]["in-game-attributes"]["asc_effect"]["value"] = 0.25
            if asc == "Strawberry":
                item_list[i]["in-game-attributes"]["asc_effect"] = {}
                item_list[i]["in-game-attributes"]["asc_effect"]["type"] = "produce_item"
                item_list[i]["in-game-attributes"]["asc_effect"]["factor"] = "Strawberry"
                item_list[i]["in-game-attributes"]["asc_effect"]["value"] = 0.25
            attr_list = ["increase_str", "increase_dex", "increase_con", "increase_int", "increase_wis", "increase_cha",
                         "increase_luc"]
            item_list[i]["in-game-attributes"]["random_attribute"] = {}
            item_list[i]["in-game-attributes"]["random_attribute"]["type"] = choice(attr_list)
            item_list[i]["in-game-attributes"]["random_attribute"]["factor"] = "constant"
            item_list[i]["in-game-attributes"]["random_attribute"]["value"] = randint(10, 11) / 10
            item_list[i]["in-game-attributes"]["familiar_attribute"] = {}
            item_list[i]["in-game-attributes"]["familiar_attribute"]["type"] = "assist_attack"
            item_list[i]["in-game-attributes"]["familiar_attribute"]["factor"] = "probability"
            item_list[i]["in-game-attributes"]["familiar_attribute"]["probability"] = 0.2
            item_list[i]["in-game-attributes"]["familiar_attribute"]["value"] = randint(30, 33) / 10


    with open('./library/item_list.json', 'w') as file:
        json.dump(item_list, file)
