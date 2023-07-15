import random
from library.character import *
import ujson as json
import math

def assign_attribute(stats):

    # spirits
    if stats.spirit != None:
        spirit = get_item_attributes("Spirits", stats.spirit)
        if spirit["Spirit_type"] == "Chia Friends":
            attr_list = ["str", "dex", "con", "int", "wis", "cha", "luc"]
            random.choice(attr_list)
            attr_list.remove(random.choice(attr_list))
            attr_list.remove(random.choice(attr_list))
            attr_list.remove(random.choice(attr_list))
            attr_list.remove(random.choice(attr_list))

            if "str" in attr_list:
                stats.str += round(stats.level / 20)
            if "dex" in attr_list:
                stats.dex += round(stats.level / 20)
            if "con" in attr_list:
                stats.con += round(stats.level / 20)
            if "int" in attr_list:
                stats.int += round(stats.level / 20)
            if "wis" in attr_list:
                stats.wis += round(stats.level / 20)
            if "cha" in attr_list:
                stats.cha += round(stats.level / 20)
            if "luc" in attr_list:
                stats.luc += round(stats.level / 20)

    # weapons
    if stats.weapon != None:
        weapon = get_item_attributes("Weapons", stats.weapon)
        if weapon["Weapon_type"] == "Chiania Long Arm Blade":
            stats.slash = 2

            stats.str += random.randint(int(2 * stats.level / 5), int(5 * stats.level / 5))
            stats.dex += random.randint(int(2 * stats.level / 5), int(5 * stats.level / 5))

        if weapon["Weapon_type"] == "Knife":
            stats.slash = 1
            stats.pierce = 1
            stats.luc += random.randint(int(2 * stats.level / 5), int(5 * stats.level / 5))
            stats.dex += random.randint(int(2 * stats.level / 5), int(5 * stats.level / 5))

        if weapon["Weapon_type"] == "Sword":
            stats.slash = 2
            stats.pierce = 1
            stats.str += random.randint(int(2 * stats.level / 5), int(5 * stats.level / 5))
            stats.dex += random.randint(int(2 * stats.level / 5), int(5 * stats.level / 5))

        if weapon["Weapon_type"] == "Short Axe":
            stats.slash = 2
            stats.bash = 1
            stats.str += random.randint(int(2 * stats.level / 5), int(5 * stats.level / 5))
            stats.dex += random.randint(int(2 * stats.level / 5), int(5 * stats.level / 5))

        if weapon["Weapon_type"] == "Wood Club":
            stats.bash = 2
            stats.str += random.randint(int(2 * stats.level / 5), int(5 * stats.level / 5))
            stats.con += random.randint(int(2 * stats.level / 5), int(5 * stats.level / 5))

        if weapon["Weapon_type"] == "Short Bow":
            stats.pierce = 2
            stats.dex += random.randint(int(2 * stats.level / 4), int(5 * stats.level / 4))

        if weapon["Weapon_type"] == "Catapult":
            stats.bash = 1
            stats.str += random.randint(int(2 * stats.level / 6), int(5 * stats.level / 6))
            stats.con += random.randint(int(2 * stats.level / 6), int(5 * stats.level / 6))

        if weapon["Weapon_type"] == "Enhanced Tree Root":
            stats.pierce = 1
            stats.luc += random.randint(int(2 * stats.level / 7), int(5 * stats.level / 7))
            stats.dex += random.randint(int(2 * stats.level / 7), int(5 * stats.level / 7))

        if weapon["Weapon_type"] == "Khopesh":
            stats.slash = 1
            stats.bash = 1
            stats.pierce = 1
            stats.str += random.randint(int(2 * stats.level / 8), int(5 * stats.level / 8))
            stats.dex += random.randint(int(2 * stats.level / 8), int(5 * stats.level / 8))
            stats.con += random.randint(int(2 * stats.level / 8), int(5 * stats.level / 8))

        if weapon["Weapon_type"] == "Halberd":
            stats.slash = 1
            stats.pierce = 2
            stats.str += random.randint(int(2 * stats.level / 4), int(5 * stats.level / 4))

        if weapon["Nuclei"] == "Red":
            stats.str = stats.str + random.randint(1, 5)
        if weapon["Nuclei"] == "Orange":
            stats.con = stats.con + random.randint(1, 5)
        if weapon["Nuclei"] == "Green":
            stats.dex = stats.dex + random.randint(1, 5)
        if weapon["Nuclei"] == "Purple":
            stats.wis = stats.wis + random.randint(1, 5)

    # shield
    if stats.shield != None:
        shield = get_item_attributes("Shields", stats.shield)
        if shield["Shield_type"] == "Bark Shield":
            stats.defense += 1 + int(stats.level / 5)
        if shield["Shield_type"] == "Small Round Shield":
            stats.defense += 2 + int(stats.level / 5)

    # armor
    if stats.armor != None:
        armor = get_item_attributes("Armors", stats.armor)
        if armor["Armor_type"] == "Cloth Armor":
            stats.defense += 1 + int(stats.level / 10)
            stats.health += int(stats.level / 5)
            stats.dex += random.randint(int(2 * stats.level / 5), int(5 * stats.level / 5))

    # ring
    if stats.ring != None:
        ring = get_item_attributes("Rings", stats.ring)
        if ring["Nuclei"] == "Red":
            stats.str = stats.str + random.randint(1, 5)
        if ring["Nuclei"] == "Green":
            stats.dex = stats.dex + random.randint(1, 5)
        if ring["Nuclei"] == "Blue":
            stats.int = stats.int + random.randint(1, 5)
        if ring["Nuclei"] == "Orange":
            stats.con = stats.con + random.randint(1, 5)
        if ring["Nuclei"] == "Purple":
            stats.wis = stats.wis + random.randint(1, 5)

    # mount
    if stats.mount != None:
        mount = get_item_attributes("Mounts", stats.mount)
        if mount.get("Mount_type") == "Deer":
            stats.dex = stats.dex + random.randint(1, 3)
        if mount.get("Mount_type") == "Adult Deer":
            stats.dex = stats.dex + random.randint(1, 3)
            stats.str = stats.str + 1
        if mount.get("Mount_type") == "Majestic Deer":
            stats.dex = stats.dex + random.randint(1, 3)
            stats.str = stats.str + random.randint(1, 3)
        if mount.get("Mount_type") == "Vines Deer":
            stats.dex = stats.dex + random.randint(1, 3)
            stats.wis = stats.wis + 1
        if mount.get("Mount_type") == "Slime Deer":
            stats.dex = stats.dex + random.randint(1, 3)
            stats.dex = stats.dex + random.randint(1, 3)
            stats.luc = stats.luc + random.randint(1, 3)
        if mount.get("Mount_type") == "Bandana Purple Deer":
            stats.dex = stats.dex + random.randint(1, 3)
            stats.con = stats.con + 1
        if mount.get("Mount_type") == "Bandana Red Deer":
            stats.dex = stats.dex + random.randint(1, 3)
            stats.int = stats.int + random.randint(1, 2)
        if mount.get("Mount_type") == "One Blink Deer":
            stats.dex = stats.dex + random.randint(1, 3)
            stats.cha = stats.cha + random.randint(0, 1)
        if mount.get("Mount_type") == "Two Blink Deer":
            stats.dex = stats.dex + random.randint(1, 3)
            stats.cha = stats.cha + 1
        if mount.get("Species") == "Dragon":
            stats.str += random.randint(1, 4)
            stats.dex += random.randint(1, 2)
        if mount.get("Species") == "Nightsaber":
            stats.str += random.randint(1, 2)
            stats.dex += random.randint(1, 3)
        if mount.get("Species") == "Warsheep":
            stats.str += random.randint(1, 3)
            stats.dex += random.randint(1, 2)
        if mount.get("Species") == "Magic Marmot":
            stats.int += random.randint(1, 4)
            stats.dex += random.randint(1, 2)
        if mount.get("Rarity") == "Common":
            stats.cha += 1
        if mount.get("Rarity") == "Uncommon":
            stats.cha += 1
            stats.luc += 1
        if mount.get("Rarity") == "Rare":
            stats.cha += random.randint(1, 2)
            stats.luc += 1
        if mount.get("Rarity") == "Epic":
            stats.cha += 2
            stats.luc += 1
        if mount.get("Rarity") == "Legendary":
            stats.cha += 2
            stats.luc += 1

    # herb
    if stats.herb != None:
        herb = get_item_attributes("Herbs", stats.herb)
        if herb["Herb_type"] == "Ordinary Brave Seedling":
            stats.health = stats.health + random.randint(1, 3)
        if herb["Herb_type"] == "Strong Brave Seedling":
            stats.health = stats.health + random.randint(1, 3)
            stats.con = stats.con + random.randint(1, 3)
        if herb["Herb_type"] == "Powerful Brave Seedling":
            stats.health = stats.health + random.randint(1, 3) + random.randint(1, 3)
            stats.con = stats.con + random.randint(1, 3)
        if herb["Herb_type"] == "Super Powerful Brave Seedling":
            stats.health = stats.health + random.randint(1, 3) + random.randint(1, 3)
            stats.con = stats.con + random.randint(1, 3) + random.randint(1, 3)

    # familiar
    # chia slime
    if stats.familiar != None:
        familiar = get_item_attributes("Familiars", stats.familiar)
        if familiar.get("Familiar_type") == "Red Chia Slime":
            stats.str = stats.str + 1
            stats.int = stats.int - 1
        if familiar.get("Familiar_type") == "Blue Chia Slime":
            stats.int = stats.int + 1
            stats.str = stats.str - 1
        if familiar.get("Familiar_type") == "Green Chia Slime":
            stats.dex = stats.dex + 1
            stats.con = stats.con - 1
        if familiar.get("Familiar_type") == "Orange Chia Slime":
            stats.con = stats.con + 1
            stats.dex = stats.dex - 1
        if familiar.get("Familiar_type") == "Yellow Chia Slime":
            stats.cha = stats.cha + 1
            stats.wis = stats.wis - 1
        if familiar.get("Familiar_type") == "Purple Chia Slime":
            stats.wis = stats.wis + 1
            stats.cha = stats.cha - 1
        if familiar.get("Familiar_type") == "Healing Chia Slime":
            healing_castchance = random.randint(1, 20)
            if healing_castchance in [17, 18, 19, 20]:
                stats.health = stats.health + random.randint(2, 4)
        if familiar.get("Familiar_type") == "Identity Chia Slime":
            identify_castchance = random.randint(1, 20)
            if identify_castchance in [17, 18, 19, 20]:
                stats.int = stats.int + random.randint(2, 4)
        if familiar.get("Familiar_type") == "Rock Chia Slime":
            stats.con = stats.con + 2
            stats.dex = stats.dex - 1
            stats.cha = stats.cha - 1
        if familiar.get("Familiar_type") == "Defensive Aura Chia Slime":
            defensiveAura_castchance = random.randint(1, 20)
            if defensiveAura_castchance in [17, 18, 19, 20]:
                stats.defense = stats.defense + 1
        if familiar.get("Familiar_type") == "Rock Spike Chia Slime":
            rockSpike_castchance = random.randint(1, 20)
            if rockSpike_castchance in [17, 18, 19, 20]:
                stats.pierce = stats.pierce + 1
        if familiar.get("Familiar_type") == "Rock Spike Chia Slime":
            rockSpike_castchance = random.randint(1, 20)
            if rockSpike_castchance in [17, 18, 19, 20]:
                stats.pierce = stats.pierce + 1
        if familiar.get("Habitat") == "Water":
            stats.int += 2
            stats.con -= 1
            stats.str -= 1
        if familiar.get("Familiar_type") == "Slip Stream Chia Slime":
            rockSpike_castchance = random.randint(1, 20)
            if rockSpike_castchance in [17, 18, 19, 20]:
                stats.bash += 1


        # snail
        if familiar["Familiar_type"] == "Snail":
            stats.dex = stats.dex - random.randint(1, 5)
            stats.luc = stats.luc + random.randint(1, 5)
        if familiar["Familiar_type"] == "Hard Snail":
            stats.con = stats.con + random.randint(1, 5)

    # portrait
    # Chia Farmers
    if stats.portrait != None:
        portrait = get_item_attributes("Portraits", stats.portrait)
        if portrait["Portrait_type"] == "An Adventurer Disguised as Goblin":
            if portrait["Skin_type"] == "Green":
                stats.dex += 3
            if portrait["Skin_type"] == "Gray":
                stats.con += 3
            if portrait["Skin_type"] == "Brown":
                stats.str += 3

        if portrait["Portrait_type"] == "Chia Farmers":
            if portrait["Skin_type"] == "Cerulean Blue":
                stats.int = stats.int + 1
            if portrait["Skin_type"] == "Cyan":
                stats.con = stats.con + 1
            if portrait["Skin_type"] == "Dark Purple":
                stats.cha = stats.cha + 1
            if portrait["Skin_type"] == "Gold":
                stats.luc = stats.luc + 1
            if portrait["Skin_type"] == "Green":
                stats.wis = stats.wis + 1
            if portrait["Skin_type"] == "Jasmine":
                stats.dex = stats.dex + 1
            if portrait["Skin_type"] == "Narcissus":
                stats.int = stats.int + 1
            if portrait["Skin_type"] == "Pale Mauve":
                stats.wis = stats.wis + 1
            if portrait["Skin_type"] == "Vermeil":
                stats.str = stats.str + 1
            if portrait["Skin_type"] == "Cry":
                stats.cha = stats.cha + 1
                stats.wis = stats.wis + 1
                stats.luc = stats.luc - 2
                if mount.get("Rarity") == "Epic":
                    stats.dex += 1
                    stats.wis += 1
                    stats.luc -= 1
            if portrait["Skin_type"] == "Rainbow":
                stats.health = stats.health + 1
                rainbow_castchance = random.randint(1, 20)
                if rainbow_castchance in [10, 20]:
                    stats.int = stats.int + 1
                    stats.cha = stats.cha + 1
                    stats.wis = stats.wis + 1
                    stats.dex = stats.dex + 1
                    stats.str = stats.str + 1
                    stats.con = stats.con + 1
                    stats.health = stats.health + 1
            if portrait["Tool_type"] == "Water Tools":
                stats.con += 1
                if mount.get("Species") == "Dragon":
                    stats.str += 1
                if mount.get("Mount_type") == "Deer":
                    stats.dex += 1
                if mount.get("Mount_type") == "Adult Deer":
                    stats.dex += 1
                if mount.get("Mount_type") == "Majestic Deer":
                    stats.dex += 1
                if mount.get("Mount_type") == "Vines Deer":
                    stats.dex += 1
                if mount.get("Mount_type") == "Slime Deer":
                    stats.dex += 1
                if mount.get("Mount_type") == "Bandana Purple Deer":
                    stats.dex += 1
                if mount.get("Mount_type") == "Bandana Red Deer":
                    stats.dex += 1
                if mount.get("Mount_type") == "One Blink Deer":
                    stats.dex += 1
                if mount.get("Mount_type") == "Two Blink Deer":
                    stats.dex += 1

            if portrait["Tool_type"] == "Sickle Tools":
                stats.str = stats.str + 1
                if stats.herb != None:
                    stats.con += 1
            if portrait["Tool_type"] == "Shelf Tools":
                stats.dex = stats.dex + 1
            if portrait["Tool_type"] == "Sapling Tools":
                stats.luc = stats.luc + 1
                if mount.get("Species") == "Nightsaber":
                    stats.dex += 1
            if portrait["Tool_type"] == "Pitchfork Tools":
                stats.str = stats.str + 1
                if stats.herb != None:
                    stats.health += 1
            if portrait["Tool_type"] == "Magic Tools":
                stats.int = stats.int + 1
                if mount.get("Species") == "Magic Marmot":
                    stats.int += 1
            if portrait["Tool_type"] == "Flowers Tools":
                stats.cha = stats.cha + 1
                if mount.get("Species") == "Warsheep":
                    stats.cha += 1
            if portrait["Tool_type"] == "Doorplate Tools":
                stats.wis = stats.wis + 1
                if stats.herb != None:
                    stats.health += 1
            if portrait["Tool_type"] == "Chia Farm Tools":
                stats.health = stats.health + 1
                chiafarm_castchance = random.randint(1, 20)
                if chiafarm_castchance in [10, 20]:
                    stats.health = stats.health + 2

    # self
    stats.defense += int(stats.con / 10)
    stats.health += int(stats.con / 3)
    stats.slash = stats.slash + int(stats.slash*stats.str / 10)
    stats.bash = stats.bash + int(stats.bash*stats.str / 10)
    stats.pierce = stats.pierce + int(stats.pierce*(stats.str + stats.dex) / 20)
    stats.str += round(stats.level / 10)
    stats.dex += round(stats.level / 10)
    stats.con += round(stats.level / 10)
    stats.int += round(stats.level / 10)
    stats.wis += round(stats.level / 10)
    stats.cha += round(stats.level / 10)
    stats.luc += round(stats.level / 10)

    return stats

def get_item_attributes(category, item):
    with open('./library/item_list.json', 'r') as file:
        item_list = json.load(file)
        file.close()
        attributes = item_list[category][item]
    return attributes