import urllib3
from bs4 import BeautifulSoup
import json
from time import sleep
from random import choice, randint
from library.mongo import *

http = urllib3.PoolManager()
collection_id = ["col16fpva26fhdjp2echs3cr7c30gzl7qe67hu9grtsjcqldz354asjsyzp6wx",  # CI
                 "col1ucr852c8uzgemuashmz65kmnt2nn4wuhecevrwhtkk72ukfc5c7s6wn3sj",  # CI
                 "col1w0h8kkkh37sfvmhqgd4rac0m0llw4mwl69n53033h94fezjp6jaq4pcd3g",  # Chreatures
                 "col19z8k90wfezt55jj2zm526yzmk8dq0fcyqamzmtqv7hv4wkafhnjsp8fsz2",  # ChiaSlime
                 "col1jgw23rce22aucy0vrseqa3dte8sd0924sdjw5xuxzljcnhgr8fpqnjcu7q",  # BS
                 "col1syclna803y6h3zl24fwswk0thmm7ad845cfc6sv4sndfzu26q8cq3pprct",  # snail
                 "col1ffwmq5aumd96sxlw6l665hkccq9w3w2w0a4pcfhl329u07sz92cqg7vjkj",  # chia farmer
                 "col1z0ef7w5n4vq9qkue67y8jnwumd9799sm50t8fyle73c70ly4z0ws0p2rhl",  # Chia Friends
                 "col1ykj00rq56xs235zumwcwa3w7j927cqfgqatvp795q4wav5fs5hrqu668my",  # Chia Mounts
                 "col1eqaw4clqxpzex6g9lhdr8hc8s7ygz45m7j7zesru4j37vq8qgzvs9zc7vr",  # open box
                 "col1u59x6saj9v5yl7jddf9ms4yfcltxnx7mdmskwcqt53yxfuhljr2shjvf7j",  # season home
                 "col17jxrr7pwxuhxra86z4gr08tajk3mpr7gjst643a7gv0dc8p8p9aqdcvj30",  # ball dog
                 "col1lqdkghxfwj7v0ajka0ww4q5ljkzjh8xgm28h7e3s4sh03smrmxxsn8qcpw",  # anti ball dog
                 "col1lend2dcn558km4wcwta4xnkfv3xpcmlp9kyt0m909emvfxechlyqdl5ndg",  # City illusion
                 "col1smsk8mra4jk65svyr72u9rmam48yedtxp8z3k8pg3r62eaw4k0vqqr6yyw",  # Haunted home
                 "col14acdqqllx66yqt9lwykwvqs2jpsys3nzmq6yqhlnvqx7pevpez4sqhzzug",  # freckle girl
                 "col1ae2z2zpqm4v6rkm0j8mds7cy6yh055wjfdsxjn5jsx6jvntagf8sra4t2h",  # Dog food
                 "col1r95a7kxtnhdgg0w3w48gvpvc3jjeaccx38tf0d56727muk3ngqcqm9drw6"   # Maple Pixel Girl
                 ]


def update_nft_list():  # import nft list from cloud api
    nft_list = get_nft_list()
    for i in collection_id:
        print(i)
        url = 'https://api.mintgarden.io/collections/' + str(i) + '/nfts/ids'
        response = http.request('GET', url)
        nft_ids = BeautifulSoup(response.data, features="html.parser")
        nft_ids = json.loads(nft_ids.text)

        for j in nft_ids:
            nft_id = str(j["encoded_id"])
            if nft_id not in nft_list:
                print("new nft: " + nft_id + " detected!")
                new_item = {"nft_id": nft_id, "collection_id": str(i), "item_name": j["name"],
                            "item_description": j["description"], "endurance": "∞", "on-chain-attributes": {},
                            "in-game-attributes": {}, "DB synced": False}

                if i == "col16fpva26fhdjp2echs3cr7c30gzl7qe67hu9grtsjcqldz354asjsyzp6wx":
                    new_item["collection_name"] = "Chia Inventory"
                elif i == "col1ucr852c8uzgemuashmz65kmnt2nn4wuhecevrwhtkk72ukfc5c7s6wn3sj":
                    new_item["collection_name"] = "Chia Inventory"
                elif i == "col1w0h8kkkh37sfvmhqgd4rac0m0llw4mwl69n53033h94fezjp6jaq4pcd3g":
                    new_item["collection_name"] = "Chreatures"
                    new_item["item_type"] = "mount"
                elif i == "col19z8k90wfezt55jj2zm526yzmk8dq0fcyqamzmtqv7hv4wkafhnjsp8fsz2":
                    new_item["collection_name"] = "Chia Slimes"
                    new_item["item_type"] = "familiar"
                elif i == "col1jgw23rce22aucy0vrseqa3dte8sd0924sdjw5xuxzljcnhgr8fpqnjcu7q":
                    new_item["collection_name"] = "Brave Leef"
                    new_item["item_type"] = "herb"
                elif i == "col1syclna803y6h3zl24fwswk0thmm7ad845cfc6sv4sndfzu26q8cq3pprct":
                    new_item["collection_name"] = "Sheesh! Snail"
                    new_item["item_type"] = "familiar"
                elif i == "col1z0ef7w5n4vq9qkue67y8jnwumd9799sm50t8fyle73c70ly4z0ws0p2rhl":
                    new_item["collection_name"] = "Chia Friends"
                    new_item["item_type"] = "spirit"
                elif i == "col1ffwmq5aumd96sxlw6l665hkccq9w3w2w0a4pcfhl329u07sz92cqg7vjkj":
                    new_item["collection_name"] = "Chia Farmers"
                    new_item["item_type"] = "farmer"
                elif i == "col1ykj00rq56xs235zumwcwa3w7j927cqfgqatvp795q4wav5fs5hrqu668my":
                    new_item["collection_name"] = "Chia Mounts"
                    new_item["item_type"] = "mount"
                elif i == "col1eqaw4clqxpzex6g9lhdr8hc8s7ygz45m7j7zesru4j37vq8qgzvs9zc7vr":
                    new_item["collection_name"] = "open box"
                    new_item["item_type"] = "producer"
                elif i == "col1u59x6saj9v5yl7jddf9ms4yfcltxnx7mdmskwcqt53yxfuhljr2shjvf7j":
                    new_item["collection_name"] = "Seasons Home"
                    new_item["item_type"] = "house"
                elif i == "col17jxrr7pwxuhxra86z4gr08tajk3mpr7gjst643a7gv0dc8p8p9aqdcvj30":
                    new_item["collection_name"] = "Balldog Collection"
                    new_item["item_type"] = "familiar"
                elif i == "col1lqdkghxfwj7v0ajka0ww4q5ljkzjh8xgm28h7e3s4sh03smrmxxsn8qcpw":
                    new_item["collection_name"] = "Anti Dogg Collection"
                    new_item["item_type"] = "pet"
                elif i == "col1lend2dcn558km4wcwta4xnkfv3xpcmlp9kyt0m909emvfxechlyqdl5ndg":
                    new_item["collection_name"] = "City Illusion"
                    new_item["item_type"] = "painting"
                elif i == "col1smsk8mra4jk65svyr72u9rmam48yedtxp8z3k8pg3r62eaw4k0vqqr6yyw":
                    new_item["collection_name"] = "Haunted Home"
                    new_item["item_type"] = "house"
                elif i == "col1ae2z2zpqm4v6rkm0j8mds7cy6yh055wjfdsxjn5jsx6jvntagf8sra4t2h":
                    new_item["collection_name"] = "BD Shop"
                    new_item["item_type"] = "dog food"
                elif i == "col14acdqqllx66yqt9lwykwvqs2jpsys3nzmq6yqhlnvqx7pevpez4sqhzzug":
                    new_item["collection_name"] = "Freckle Girls II"
                    new_item["item_type"] = "portrait"
                elif i == "col1r95a7kxtnhdgg0w3w48gvpvc3jjeaccx38tf0d56727muk3ngqcqm9drw6":
                    new_item["collection_name"] = "Maple Pixel Girl"
                    new_item["item_type"] = "portrait"

                add_a_nft(nft_id, new_item)
                print("new nft: " + nft_id + " added!")


def update_on_chain_attributes():  # download on-chain attributes
    with open('not_used/item_list.json', 'r', encoding="utf-8") as file:
        item_list = json.load(file)
        file.close()
    new_item_list = item_list.copy()
    total = len(new_item_list)
    done = 0
    for i in new_item_list:
        if new_item_list[i].get("DB synced") == True:
            done += 1
    print(str(done) + "/" + str(total) + " of nfts are synced.")
    sleep(2)
    for i in new_item_list.copy():
        if new_item_list[i].get("DB synced") != True:
            print("start to update attribute of NFT: " + new_item_list[i]["item_name"] + str(i))
            url = 'https://api.mintgarden.io/nfts/' + str(i)
            response = http.request('GET', url)
            nft = BeautifulSoup(response.data, features="html.parser")
            nft = json.loads(nft.text)
            icon = nft["data"]["preview_uri"]
            new_item_list[i]["icon"] = icon
            if nft["data"]["metadata_json"].get("attributes") != None:
                on_chai_attributes = nft["data"]["metadata_json"]["attributes"]
            if nft["data"]["metadata_json"].get("attribute") != None:
                on_chai_attributes = nft["data"]["metadata_json"]["attribute"]
            new_item_list[i]["DB synced"] = True
            for j in range(0, len(on_chai_attributes)):
                print("add attribute: " + str(j) + " as " + str(on_chai_attributes[j]))
                new_item_list[i]["on-chain-attributes"][str(j)] = on_chai_attributes[j]
                print(new_item_list[i]["on-chain-attributes"][str(j)])
            with open('not_used/item_list.json', 'w') as file:
                json.dump(new_item_list, file)
            print("db updated!")
            done += 1
            print(str(done) + "/" + str(total) + " of nfts are synced.")
            sleep(2)

        elif new_item_list[i].get("icon") == None:
            new_item_list[i]["DB synced"] == False
        else:
            print("attributes exist")


def modify_item_attributes():
    with open('not_used/item_list.json', 'r') as file:
        item_list = json.load(file)
        file.close()

    for i in item_list:
        if item_list[i]["collection_name"] == "open box":
            if item_list[i]["in-game-attributes"].get("enhancement") == None:
                item_list[i]["in-game-attributes"]["enhancement"] = {}
                item_list[i]["in-game-attributes"]["enhancement"]["type"] = "enhancement"
                item_list[i]["in-game-attributes"]["enhancement"]["value"] = 0

            item_list[i]["item_type"] = "producer"
            if type(item_list[i]["in-game-attributes"].get("0")) is not dict:
                item_list[i]["in-game-attributes"]["0"] = {}
                item_list[i]["in-game-attributes"]["0"]["type"] = "produce_item"
                item_list[i]["in-game-attributes"]["0"]["factor"] = "Common Lootbox"
                item_list[i]["in-game-attributes"]["0"]["value"] = 1

    with open('not_used/item_list.json', 'w') as file:
        json.dump(item_list, file)


update_nft_list()
# update_on_chain_attributes()
# modify_item_attributes()

# run code
# update_nft_list()
# update_on_chain_attributes()
