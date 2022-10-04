def generate_in_game_attributes():  # generate in-game attributes
    attr_list = ["increase_str", "increase_dex", "increase_con", "increase_int", "increase_wis", "increase_cha",
                 "increase_luc"]

    for i in new_item_list:

        item_name = new_item_list[i]["item_name"]
        print("generate in game attributes for " + str(item_name))

        new_item_list[i]["in-game-attributes"]["enhancement"] = {}
        new_item_list[i]["in-game-attributes"]["enhancement"]["type"] = "enhancement"
        new_item_list[i]["in-game-attributes"]["enhancement"]["value"] = 0
        new_item_list[i]["in-game-attributes"]["random_attribute"] = {}
        new_item_list[i]["in-game-attributes"]["random_attribute"]["type"] = choice(attr_list)
        new_item_list[i]["in-game-attributes"]["random_attribute"]["factor"] = "constant"
        new_item_list[i]["in-game-attributes"]["random_attribute"]["value"] = randint(10, 11) / 10

        if new_item_list[i]["collection_name"] == "Chia Friends":
            new_item_list[i]["in-game-attributes"]["0"] = {}
            new_item_list[i]["in-game-attributes"]["0"]["type"] = choice(attr_list)
            new_item_list[i]["in-game-attributes"]["0"]["factor"] = "level_scale"
            new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(19, 20)
            new_item_list[i]["in-game-attributes"]["1"] = {}
            new_item_list[i]["in-game-attributes"]["1"]["type"] = choice(attr_list)
            new_item_list[i]["in-game-attributes"]["1"]["factor"] = "level_scale"
            new_item_list[i]["in-game-attributes"]["1"]["value"] = randint(19, 20)
            new_item_list[i]["in-game-attributes"]["2"] = {}
            new_item_list[i]["in-game-attributes"]["2"]["type"] = choice(attr_list)
            new_item_list[i]["in-game-attributes"]["2"]["factor"] = "level_scale"
            new_item_list[i]["in-game-attributes"]["2"]["value"] = randint(19, 20)
            new_item_list[i]["in-game-attributes"]["3"] = {}
            new_item_list[i]["in-game-attributes"]["3"]["type"] = choice(attr_list)
            new_item_list[i]["in-game-attributes"]["3"]["factor"] = "constant"
            new_item_list[i]["in-game-attributes"]["3"]["value"] = randint(10, 11) / 10

        # weapons
        if new_item_list[i]["item_type"] == "Weapons":
            weapon = get_item_attributes("Weapons", item_name)
            if weapon["Weapon_type"] == "Chiania Long Arm Blade":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_slash"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(20, 22) / 10
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "catch_insect"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 1
                new_item_list[i]["in-game-attributes"]["2"] = {}
                new_item_list[i]["in-game-attributes"]["2"]["type"] = "increase_str"
                new_item_list[i]["in-game-attributes"]["2"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["2"]["value"] = 5
                new_item_list[i]["in-game-attributes"]["3"] = {}
                new_item_list[i]["in-game-attributes"]["3"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["3"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["3"]["value"] = 5
                new_item_list[i]["in-game-attributes"]["4"] = {}
                new_item_list[i]["in-game-attributes"]["4"]["type"] = choice(attr_list)
                new_item_list[i]["in-game-attributes"]["4"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["4"]["value"] = randint(10, 11) / 10

            if weapon["Weapon_type"] == "Knife":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_slash"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(10, 11) / 10
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_pierce"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = randint(10, 11) / 10
                new_item_list[i]["in-game-attributes"]["2"] = {}
                new_item_list[i]["in-game-attributes"]["2"]["type"] = "increase_luc"
                new_item_list[i]["in-game-attributes"]["2"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["2"]["value"] = 5
                new_item_list[i]["in-game-attributes"]["3"] = {}
                new_item_list[i]["in-game-attributes"]["3"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["3"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["3"]["value"] = 5
                new_item_list[i]["in-game-attributes"]["4"] = {}
                new_item_list[i]["in-game-attributes"]["4"]["type"] = choice(attr_list)
                new_item_list[i]["in-game-attributes"]["4"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["4"]["value"] = randint(10, 11) / 10

            if weapon["Weapon_type"] == "Sword":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_slash"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(20, 22) / 10
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_pierce"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = randint(10, 11) / 10
                new_item_list[i]["in-game-attributes"]["2"] = {}
                new_item_list[i]["in-game-attributes"]["2"]["type"] = "increase_str"
                new_item_list[i]["in-game-attributes"]["2"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["2"]["value"] = 5
                new_item_list[i]["in-game-attributes"]["3"] = {}
                new_item_list[i]["in-game-attributes"]["3"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["3"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["3"]["value"] = 5
                new_item_list[i]["in-game-attributes"]["4"] = {}
                new_item_list[i]["in-game-attributes"]["4"]["type"] = choice(attr_list)
                new_item_list[i]["in-game-attributes"]["4"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["4"]["value"] = randint(10, 11) / 10

            if weapon["Weapon_type"] == "Short Axe":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_slash"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(20, 22) / 10
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_bash"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = randint(10, 11) / 10
                new_item_list[i]["in-game-attributes"]["2"] = {}
                new_item_list[i]["in-game-attributes"]["2"]["type"] = "increase_str"
                new_item_list[i]["in-game-attributes"]["2"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["2"]["value"] = 5
                new_item_list[i]["in-game-attributes"]["3"] = {}
                new_item_list[i]["in-game-attributes"]["3"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["3"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["3"]["value"] = 5
                new_item_list[i]["in-game-attributes"]["4"] = {}
                new_item_list[i]["in-game-attributes"]["4"]["type"] = choice(attr_list)
                new_item_list[i]["in-game-attributes"]["4"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["4"]["value"] = randint(10, 11) / 10

            if weapon["Weapon_type"] == "Wood Club":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_bash"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(20, 22) / 10
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_str"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 5
                new_item_list[i]["in-game-attributes"]["2"] = {}
                new_item_list[i]["in-game-attributes"]["2"]["type"] = "increase_con"
                new_item_list[i]["in-game-attributes"]["2"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["2"]["value"] = 5
                new_item_list[i]["in-game-attributes"]["3"] = {}
                new_item_list[i]["in-game-attributes"]["3"]["type"] = choice(attr_list)
                new_item_list[i]["in-game-attributes"]["3"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["3"]["value"] = randint(10, 11) / 10

            if weapon["Weapon_type"] == "Short Bow":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_pierce"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(20, 22) / 10
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 4
                new_item_list[i]["in-game-attributes"]["2"] = {}
                new_item_list[i]["in-game-attributes"]["2"]["type"] = choice(attr_list)
                new_item_list[i]["in-game-attributes"]["2"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["2"]["value"] = randint(10, 11) / 10

            if weapon["Weapon_type"] == "Catapult":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_bash"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(10, 11) / 10
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_str"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 6
                new_item_list[i]["in-game-attributes"]["2"] = {}
                new_item_list[i]["in-game-attributes"]["2"]["type"] = "increase_con"
                new_item_list[i]["in-game-attributes"]["2"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["2"]["value"] = 6
                new_item_list[i]["in-game-attributes"]["3"] = {}
                new_item_list[i]["in-game-attributes"]["3"]["type"] = choice(attr_list)
                new_item_list[i]["in-game-attributes"]["3"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["3"]["value"] = randint(10, 11) / 10

            if weapon["Weapon_type"] == "Enhanced Tree Root":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_pierce"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(10, 11) / 10
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_luc"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 7
                new_item_list[i]["in-game-attributes"]["2"] = {}
                new_item_list[i]["in-game-attributes"]["2"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["2"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["2"]["value"] = 7
                new_item_list[i]["in-game-attributes"]["3"] = {}
                new_item_list[i]["in-game-attributes"]["3"]["type"] = choice(attr_list)
                new_item_list[i]["in-game-attributes"]["3"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["3"]["value"] = randint(10, 11) / 10

            if weapon["Weapon_type"] == "Khopesh":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_slash"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(10, 11) / 10
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_pierce"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = randint(10, 11) / 10
                new_item_list[i]["in-game-attributes"]["2"] = {}
                new_item_list[i]["in-game-attributes"]["2"]["type"] = "increase_bash"
                new_item_list[i]["in-game-attributes"]["2"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["2"]["value"] = randint(10, 11) / 10
                new_item_list[i]["in-game-attributes"]["3"] = {}
                new_item_list[i]["in-game-attributes"]["3"]["type"] = "increase_str"
                new_item_list[i]["in-game-attributes"]["3"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["3"]["value"] = 8
                new_item_list[i]["in-game-attributes"]["4"] = {}
                new_item_list[i]["in-game-attributes"]["4"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["4"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["4"]["value"] = 8
                new_item_list[i]["in-game-attributes"]["5"] = {}
                new_item_list[i]["in-game-attributes"]["5"]["type"] = "increase_con"
                new_item_list[i]["in-game-attributes"]["5"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["5"]["value"] = 8
                new_item_list[i]["in-game-attributes"]["6"] = {}
                new_item_list[i]["in-game-attributes"]["6"]["type"] = choice(attr_list)
                new_item_list[i]["in-game-attributes"]["6"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["6"]["value"] = randint(10, 11) / 10

            if weapon["Weapon_type"] == "Halberd":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_slash"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(10, 11) / 10
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_pierce"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = randint(20, 22) / 10
                new_item_list[i]["in-game-attributes"]["2"] = {}
                new_item_list[i]["in-game-attributes"]["2"]["type"] = "increase_str"
                new_item_list[i]["in-game-attributes"]["2"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["2"]["value"] = 4
                new_item_list[i]["in-game-attributes"]["3"] = {}
                new_item_list[i]["in-game-attributes"]["3"]["type"] = choice(attr_list)
                new_item_list[i]["in-game-attributes"]["3"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["3"]["value"] = randint(10, 11) / 10

            if weapon["Nuclei"] == "Red":
                new_item_list[i]["in-game-attributes"]["nuclei"] = {}
                new_item_list[i]["in-game-attributes"]["nuclei"]["type"] = "increase_str"
                new_item_list[i]["in-game-attributes"]["nuclei"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["nuclei"]["value"] = randint(40, 50) / 10
            if weapon["Nuclei"] == "Orange":
                new_item_list[i]["in-game-attributes"]["nuclei"] = {}
                new_item_list[i]["in-game-attributes"]["nuclei"]["type"] = "increase_con"
                new_item_list[i]["in-game-attributes"]["nuclei"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["nuclei"]["value"] = randint(40, 50) / 10
            if weapon["Nuclei"] == "Green":
                new_item_list[i]["in-game-attributes"]["nuclei"] = {}
                new_item_list[i]["in-game-attributes"]["nuclei"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["nuclei"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["nuclei"]["value"] = randint(40, 50) / 10
            if weapon["Nuclei"] == "Purple":
                new_item_list[i]["in-game-attributes"]["nuclei"] = {}
                new_item_list[i]["in-game-attributes"]["nuclei"]["type"] = "increase_wis"
                new_item_list[i]["in-game-attributes"]["nuclei"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["nuclei"]["value"] = randint(40, 50) / 10

        if new_item_list[i]["item_type"] == "Shields":
            shield = get_item_attributes("Shields", item_name)
            if shield["Shield_type"] == "Bark Shield":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_defense"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(10, 11) / 10
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_defense"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 5

            if shield["Shield_type"] == "Small Round Shield":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_defense"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(20, 22) / 10
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_defense"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 5
                new_item_list[i]["in-game-attributes"]["enhancement"] = {}
                new_item_list[i]["in-game-attributes"]["enhancement"]["type"] = "enhancement"
                new_item_list[i]["in-game-attributes"]["enhancement"]["value"] = 0

        if new_item_list[i]["item_type"] == "Armors":
            armor = get_item_attributes("Armors", item_name)
            if armor["Armor_type"] == "Cloth Armor":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_defense"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(10, 11) / 10
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_defense"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 10
                new_item_list[i]["in-game-attributes"]["2"] = {}
                new_item_list[i]["in-game-attributes"]["2"]["type"] = "increase_health"
                new_item_list[i]["in-game-attributes"]["2"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["2"]["value"] = 5
                new_item_list[i]["in-game-attributes"]["3"] = {}
                new_item_list[i]["in-game-attributes"]["3"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["3"]["factor"] = "level_scale"
                new_item_list[i]["in-game-attributes"]["3"]["value"] = 5

        if new_item_list[i]["item_type"] == "Rings":
            ring = get_item_attributes("Rings", item_name)
            if ring["Nuclei"] == "Red":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_str"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(30, 33) / 10

            if ring["Nuclei"] == "Green":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(30, 33) / 10

            if ring["Nuclei"] == "Blue":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_int"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(30, 33) / 10

            if ring["Nuclei"] == "Orange":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_con"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(30, 33) / 10

            if ring["Nuclei"] == "Purple":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_wis"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = randint(30, 33) / 10

        # mount
        if new_item_list[i]["item_type"] == "Mounts":
            mount = get_item_attributes("Mounts", item_name)
            new_item_list[i]["in-game-attributes"]["mount_attribute"] = {}
            new_item_list[i]["in-game-attributes"]["mount_attribute"]["type"] = "mount_stamina"
            new_item_list[i]["in-game-attributes"]["mount_attribute"]["value"] = randint(100, 110)

            if mount.get("Mount_type") == "Deer":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3

            if mount.get("Mount_type") == "Adult Deer":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_str"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = randint(10, 11) / 10

            if mount.get("Mount_type") == "Majestic Deer":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_str"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 3

            if mount.get("Mount_type") == "Vines Deer":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_wis"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = randint(10, 11) / 10

            if mount.get("Mount_type") == "Slime Deer":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_luc"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 3

            if mount.get("Mount_type") == "Bandana Purple Deer":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_con"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = randint(10, 11) / 10

            if mount.get("Mount_type") == "Bandana Red Deer":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_int"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 2

            if mount.get("Mount_type") == "One Blink Deer":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_cha"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 2

            if mount.get("Mount_type") == "Two Blink Deer":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_cha"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = randint(10, 11) / 10

            if mount.get("Species") == "Dragon":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_str"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 4
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 2

            if mount.get("Species") == "Nightsaber":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_str"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 2
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 3

            if mount.get("Species") == "Warsheep":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_str"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 2

            if mount.get("Species") == "Magic Marmot":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_int"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 4
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 2

            if mount.get("Rarity") == "Common":
                new_item_list[i]["in-game-attributes"]["rarity_effect1"] = {}
                new_item_list[i]["in-game-attributes"]["rarity_effect1"]["type"] = "increase_cha"
                new_item_list[i]["in-game-attributes"]["rarity_effect1"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["rarity_effect1"]["value"] = randint(10, 11) / 10

            if mount.get("Rarity") == "Uncommon":
                new_item_list[i]["in-game-attributes"]["rarity_effect1"] = {}
                new_item_list[i]["in-game-attributes"]["rarity_effect1"]["type"] = "increase_cha"
                new_item_list[i]["in-game-attributes"]["rarity_effect1"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["rarity_effect1"]["value"] = randint(10, 11) / 10
                new_item_list[i]["in-game-attributes"]["rarity_effect2"] = {}
                new_item_list[i]["in-game-attributes"]["rarity_effect2"]["type"] = "increase_luc"
                new_item_list[i]["in-game-attributes"]["rarity_effect2"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["rarity_effect2"]["value"] = randint(10, 11) / 10

            if mount.get("Rarity") == "Rare":
                new_item_list[i]["in-game-attributes"]["rarity_effect1"] = {}
                new_item_list[i]["in-game-attributes"]["rarity_effect1"]["type"] = "increase_cha"
                new_item_list[i]["in-game-attributes"]["rarity_effect1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["rarity_effect1"]["value"] = 2
                new_item_list[i]["in-game-attributes"]["rarity_effect2"] = {}
                new_item_list[i]["in-game-attributes"]["rarity_effect2"]["type"] = "increase_luc"
                new_item_list[i]["in-game-attributes"]["rarity_effect2"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["rarity_effect2"]["value"] = randint(10, 11) / 10

            if mount.get("Rarity") == "Epic":
                new_item_list[i]["in-game-attributes"]["rarity_effect1"] = {}
                new_item_list[i]["in-game-attributes"]["rarity_effect1"]["type"] = "increase_cha"
                new_item_list[i]["in-game-attributes"]["rarity_effect1"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["rarity_effect1"]["value"] = randint(20, 22) / 10
                new_item_list[i]["in-game-attributes"]["rarity_effect2"] = {}
                new_item_list[i]["in-game-attributes"]["rarity_effect2"]["type"] = "increase_luc"
                new_item_list[i]["in-game-attributes"]["rarity_effect2"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["rarity_effect2"]["value"] = randint(10, 11) / 10

            if mount.get("Rarity") == "Legendary":
                new_item_list[i]["in-game-attributes"]["rarity_effect1"] = {}
                new_item_list[i]["in-game-attributes"]["rarity_effect1"]["type"] = "increase_cha"
                new_item_list[i]["in-game-attributes"]["rarity_effect1"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["rarity_effect1"]["value"] = randint(20, 22) / 10
                new_item_list[i]["in-game-attributes"]["rarity_effect2"] = {}
                new_item_list[i]["in-game-attributes"]["rarity_effect2"]["type"] = "increase_luc"
                new_item_list[i]["in-game-attributes"]["rarity_effect2"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["rarity_effect2"]["value"] = randint(20, 22) / 10

            # herb
        if new_item_list[i]["item_type"] == "Herbs":
            herb = get_item_attributes("Herbs", item_name)
            if herb["Herb_type"] == "Ordinary Brave Seedling":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_health"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
            if herb["Herb_type"] == "Strong Brave Seedling":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_health"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_con"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 3
            if herb["Herb_type"] == "Powerful Brave Seedling":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_health"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_con"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["2"] = {}
                new_item_list[i]["in-game-attributes"]["2"]["type"] = "increase_health"
                new_item_list[i]["in-game-attributes"]["2"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["2"]["value"] = 3
            if herb["Herb_type"] == "Super Powerful Brave Seedling":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_health"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_con"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["2"] = {}
                new_item_list[i]["in-game-attributes"]["2"]["type"] = "increase_health"
                new_item_list[i]["in-game-attributes"]["2"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["2"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["3"] = {}
                new_item_list[i]["in-game-attributes"]["3"]["type"] = "increase_con"
                new_item_list[i]["in-game-attributes"]["3"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["3"]["value"] = 3

        # familiar
        # chia slime
        if new_item_list[i]["item_type"] == "Familiars":
            familiar = get_item_attributes("Familiars", item_name)
            if familiar.get("Familiar_type") == "Red Chia Slime":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_str"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "decrease_int"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 3
            if familiar.get("Familiar_type") == "Blue Chia Slime":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_int"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "decrease_str"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 3
            if familiar.get("Familiar_type") == "Green Chia Slime":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_dex"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "decrease_con"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 3
            if familiar.get("Familiar_type") == "Orange Chia Slime":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_con"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "decrease_dex"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 3
            if familiar.get("Familiar_type") == "Yellow Chia Slime":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_cha"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "decrease_wis"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 3
            if familiar.get("Familiar_type") == "Purple Chia Slime":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_wis"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "decrease_cha"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 3
            if familiar.get("Familiar_type") == "Healing Chia Slime":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_health"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "probability"
                new_item_list[i]["in-game-attributes"]["0"]["probability"] = 0.2
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 4
            if familiar.get("Familiar_type") == "Identity Chia Slime":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_int"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "probability"
                new_item_list[i]["in-game-attributes"]["0"]["probability"] = 0.2
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 4
            if familiar.get("Familiar_type") == "Rock Chia Slime":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_con"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 2
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "decrease_dex"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 1
                new_item_list[i]["in-game-attributes"]["2"] = {}
                new_item_list[i]["in-game-attributes"]["2"]["type"] = "decrease_cha"
                new_item_list[i]["in-game-attributes"]["2"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["2"]["value"] = 1
            if familiar.get("Familiar_type") == "Defensive Aura Chia Slime":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_defense"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "probability"
                new_item_list[i]["in-game-attributes"]["0"]["probability"] = 0.2
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 1
            if familiar.get("Familiar_type") == "Rock Spike Chia Slime":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_pierce"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "probability"
                new_item_list[i]["in-game-attributes"]["0"]["probability"] = 0.2
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 1
            if familiar.get("Habitat") == "Water":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_int"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 2
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "decrease_con"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 1
                new_item_list[i]["in-game-attributes"]["2"] = {}
                new_item_list[i]["in-game-attributes"]["2"]["type"] = "decrease_str"
                new_item_list[i]["in-game-attributes"]["2"]["factor"] = "constant"
                new_item_list[i]["in-game-attributes"]["2"]["value"] = 1
            if familiar.get("Familiar_type") == "Slip Stream Chia Slime":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_bash"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "probability"
                new_item_list[i]["in-game-attributes"]["0"]["probability"] = 0.2
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 1

            # snail
            if familiar["Familiar_type"] == "Snail":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_luc"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 5
                new_item_list[i]["in-game-attributes"]["1"] = {}
                new_item_list[i]["in-game-attributes"]["1"]["type"] = "decrease_dex"
                new_item_list[i]["in-game-attributes"]["1"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["1"]["value"] = 5
            if familiar["Familiar_type"] == "Hard Snail":
                new_item_list[i]["in-game-attributes"]["0"] = {}
                new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_con"
                new_item_list[i]["in-game-attributes"]["0"]["factor"] = "random"
                new_item_list[i]["in-game-attributes"]["0"]["value"] = 5

        # portrait
        if new_item_list[i]["item_type"] == "Portraits":
            try:
                portrait = get_item_attributes("Portraits", item_name)
            except:
                print("not in db")
            if portrait["Portrait_type"] == "An Adventurer Disguised as Goblin":
                if portrait["Skin_type"] == "Green":
                    new_item_list[i]["in-game-attributes"]["0"] = {}
                    new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_dex"
                    new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                if portrait["Skin_type"] == "Gray":
                    new_item_list[i]["in-game-attributes"]["0"] = {}
                    new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_con"
                    new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["0"]["value"] = 3
                if portrait["Skin_type"] == "Brown":
                    new_item_list[i]["in-game-attributes"]["0"] = {}
                    new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_str"
                    new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["0"]["value"] = 3

            if new_item_list[i]["collection_name"] == "Chia Farmers":
                if new_item_list[i]["on-chain-attributes"]["1"]["value"] == "CeruleanBlue":
                    new_item_list[i]["in-game-attributes"]["0"] = {}
                    new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_int"
                    new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["0"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["1"]["value"] == "Cyan":
                    new_item_list[i]["in-game-attributes"]["0"] = {}
                    new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_con"
                    new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["0"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["1"]["value"] == "DarkPurple":
                    new_item_list[i]["in-game-attributes"]["0"] = {}
                    new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_cha"
                    new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["0"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["1"]["value"] == "Gold":
                    new_item_list[i]["in-game-attributes"]["0"] = {}
                    new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_luc"
                    new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["0"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["1"]["value"] == "Green":
                    new_item_list[i]["in-game-attributes"]["0"] = {}
                    new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_wis"
                    new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["0"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["1"]["value"] == "Jasmine":
                    new_item_list[i]["in-game-attributes"]["0"] = {}
                    new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_dex"
                    new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["0"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["1"]["value"] == "Narcissus":
                    new_item_list[i]["in-game-attributes"]["0"] = {}
                    new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_int"
                    new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["0"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["1"]["value"] == "PaleMauve":
                    new_item_list[i]["in-game-attributes"]["0"] = {}
                    new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_wis"
                    new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["0"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["1"]["value"] == "Vermeil":
                    new_item_list[i]["in-game-attributes"]["0"] = {}
                    new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_str"
                    new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["0"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["1"]["value"] == "Cry":
                    new_item_list[i]["in-game-attributes"]["0"] = {}
                    new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_cha"
                    new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["0"]["value"] = 1
                    new_item_list[i]["in-game-attributes"]["1"] = {}
                    new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_wis"
                    new_item_list[i]["in-game-attributes"]["1"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["1"]["value"] = 1
                    new_item_list[i]["in-game-attributes"]["2"] = {}
                    new_item_list[i]["in-game-attributes"]["2"]["type"] = "decrease_luc"
                    new_item_list[i]["in-game-attributes"]["2"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["2"]["value"] = 2
                if new_item_list[i]["on-chain-attributes"]["1"]["value"] == "Rainbow":
                    new_item_list[i]["in-game-attributes"]["0"] = {}
                    new_item_list[i]["in-game-attributes"]["0"]["type"] = "increase_health"
                    new_item_list[i]["in-game-attributes"]["0"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["0"]["value"] = 1
                    new_item_list[i]["in-game-attributes"]["1"] = {}
                    new_item_list[i]["in-game-attributes"]["1"]["type"] = "increase_all"
                    new_item_list[i]["in-game-attributes"]["1"]["factor"] = "probability"
                    new_item_list[i]["in-game-attributes"]["1"]["probability"] = 0.2
                    new_item_list[i]["in-game-attributes"]["1"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["7"]["value"] == "Water":
                    new_item_list[i]["in-game-attributes"]["3"] = {}
                    new_item_list[i]["in-game-attributes"]["3"]["type"] = "increase_con"
                    new_item_list[i]["in-game-attributes"]["3"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["3"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["7"]["value"] == "Sickle":
                    new_item_list[i]["in-game-attributes"]["3"] = {}
                    new_item_list[i]["in-game-attributes"]["3"]["type"] = "increase_str"
                    new_item_list[i]["in-game-attributes"]["3"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["3"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["7"]["value"] == "Shelf":
                    new_item_list[i]["in-game-attributes"]["3"] = {}
                    new_item_list[i]["in-game-attributes"]["3"]["type"] = "increase_dex"
                    new_item_list[i]["in-game-attributes"]["3"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["3"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["7"]["value"] == "Sapling":
                    new_item_list[i]["in-game-attributes"]["3"] = {}
                    new_item_list[i]["in-game-attributes"]["3"]["type"] = "increase_luc"
                    new_item_list[i]["in-game-attributes"]["3"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["3"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["7"]["value"] == "Pitchfork":
                    new_item_list[i]["in-game-attributes"]["3"] = {}
                    new_item_list[i]["in-game-attributes"]["3"]["type"] = "increase_str"
                    new_item_list[i]["in-game-attributes"]["3"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["3"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["7"]["value"] == "Magic":
                    new_item_list[i]["in-game-attributes"]["3"] = {}
                    new_item_list[i]["in-game-attributes"]["3"]["type"] = "increase_int"
                    new_item_list[i]["in-game-attributes"]["3"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["3"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["7"]["value"] == "Flowers":
                    new_item_list[i]["in-game-attributes"]["3"] = {}
                    new_item_list[i]["in-game-attributes"]["3"]["type"] = "increase_cha"
                    new_item_list[i]["in-game-attributes"]["3"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["3"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["7"]["value"] == "Doorplate":
                    new_item_list[i]["in-game-attributes"]["3"] = {}
                    new_item_list[i]["in-game-attributes"]["3"]["type"] = "increase_wis"
                    new_item_list[i]["in-game-attributes"]["3"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["3"]["value"] = 1
                if new_item_list[i]["on-chain-attributes"]["7"]["value"] == "ChiaFarm":
                    new_item_list[i]["in-game-attributes"]["3"] = {}
                    new_item_list[i]["in-game-attributes"]["3"]["type"] = "increase_health"
                    new_item_list[i]["in-game-attributes"]["3"]["factor"] = "constant"
                    new_item_list[i]["in-game-attributes"]["3"]["value"] = 1
                    new_item_list[i]["in-game-attributes"]["4"] = {}
                    new_item_list[i]["in-game-attributes"]["4"]["type"] = "increase_health"
                    new_item_list[i]["in-game-attributes"]["4"]["factor"] = "probability"
                    new_item_list[i]["in-game-attributes"]["4"]["probability"] = 0.1
                    new_item_list[i]["in-game-attributes"]["4"]["value"] = 2

    print("updated!")
    with open('./library/item_list.json', 'w') as file:
        json.dump(new_item_list, file)
