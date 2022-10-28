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

        if item_list[i]["collection_name"] == "Chia Inventory":
            if item_list[i]["item_type"] == "scroll":
                name_args = item_list[i]["item_name"].split()
                number = name_args[4][:-1]
                item_list[i]["icon"] = "https://bafybeiedchbx2uxijacfvmzzalafcoujqvogzdzgnk4zn5gots5yme2vey.ipfs.nftstorage.link/" + str(number) + ".gif"

    with open('./library/item_list.json', 'w') as file:
        json.dump(item_list, file)
