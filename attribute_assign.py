import random
from library.character import *
from library.item_list import *


def assign_attribute(stats):
    if stats.weapon in Knife_list:
        stats.slash = 1
        stats.pierce = 1
    if stats.weapon in Sword_list:
        stats.slash = 2
        stats.bash = 1
    if stats.weapon in Short_Axe_list:
        stats.slash = 2
        stats.bash = 1
    if stats.weapon in Wood_Club_list:
        stats.bash = 2
    if stats.weapon in Short_Bow_list:
        stats.pierce = 2
    if stats.weapon in Catapult_list:
        stats.bash = 1
    if stats.weapon in Enhanced_Tree_Root_list:
        stats.pierce = 1
    if stats.weapon in Khopesh_list:
        stats.slash = 1
        stats.bash = 1
        stats.pierce = 1
    if stats.weapon in Red_Nuclei_Weapon_list:
        stats.str = stats.str + random.randint(1, 5)
    if stats.weapon in Orange_Nuclei_Weapon_list:
        stats.con = stats.con + random.randint(1, 5)
    if stats.weapon in Green_Nuclei_Weapon_list:
        stats.dex = stats.dex + random.randint(1, 5)
    if stats.weapon in Purple_Nuclei_Weapon_list:
        stats.wis = stats.wis + random.randint(1, 5)
    if stats.weapon in Shadow_Sword:
        stats.slash = 5
        stats.pierce = 1
        stats.magic = 3
    if stats.shield in Bark_Shield_list:
        stats.defense = 1
    if stats.mount in Deer_list:
        stats.dex = stats.dex + random.randint(1, 5)
    if stats.mount in Majestic_Deer_list:
        stats.str = stats.str + random.randint(1, 5)
    if stats.ring == "Nuclei Ring 01":
        stats.str = stats.str + random.randint(1, 5)
    if stats.ring == "Nuclei Ring 02":
        stats.dex = stats.dex + random.randint(1, 5)
    if stats.ring == "Nuclei Ring 03":
        stats.int = stats.int + random.randint(1, 5)
    if stats.ring == "Nuclei Ring 04":
        stats.con = stats.con + random.randint(1, 5)
    if stats.ring == "Nuclei Ring 05":
        stats.wis = stats.wis + random.randint(1, 5)
    if stats.herb in Brave_Seedling_list:
        stats.health = stats.health + random.randint(1, 5)
    if stats.herb in Powerful_Brave_Seedling_list:
        stats.health = stats.health + random.randint(1, 5)
    if stats.familiar in Red_Chia_Slime_list:
        stats.str = stats.str + 1
        stats.int = stats.int - 1
    if stats.familiar in Blue_Chia_Slime_list:
        stats.int = stats.int + 1
        stats.str = stats.str - 1
    if stats.familiar in Green_Chia_Slime_list:
        stats.dex = stats.dex + 1
        stats.con = stats.con - 1
    if stats.familiar in Orange_Chia_Slime_list:
        stats.con = stats.con + 1
        stats.dex = stats.dex - 1
    if stats.familiar in Yellow_Chia_Slime_list:
        stats.cha = stats.cha + 1
        stats.wis = stats.wis - 1
    if stats.familiar in Purple_Chia_Slime_list:
        stats.wis = stats.wis + 1
        stats.cha = stats.cha - 1
    if stats.familiar in Healing_Chia_Slime_list:
        Healing_castchance = random.randint(1, 20)
        if Healing_castchance in [17, 18, 19, 20]:
            stats.health = stats.health + random.randint(2, 4)
    if stats.familiar in Identify_Chia_Slime_list:
        Identify_castchance = random.randint(1, 20)
        if Identify_castchance in [17, 18, 19, 20]:
            stats.int = stats.int + random.randint(2, 4)
    if stats.familiar in Snail_List:
        stats.dex = stats.dex - random.randint(1, 5)
        stats.luc = stats.luc + random.randint(1, 5)
    if stats.herb in Super_Powerful_Brave_Seedling_list:
        stats.con = stats.con + random.randint(1, 5)
    if stats.familiar in Hard_Snail_list:
        stats.con = stats.con + random.randint(1, 5)
    if stats.portrait in CeruleanBlueSkin_Chia_Farmers_List:
        stats.int = stats.int + 1
    if stats.portrait in CyanSkin_Chia_Farmers_List:
        stats.con = stats.con + 1
    if stats.portrait in DarkPurpleSkin_Chia_Farmers_List:
        stats.cha = stats.cha + 1
    if stats.portrait in GoldSkin_Chia_Farmers_List:
        stats.luc = stats.luc + 1
    if stats.portrait in GreenSkin_Chia_Farmers_List:
        stats.wis = stats.wis + 1
    if stats.portrait in JasmineSkin_Chia_Farmers_List:
        stats.dex = stats.dex + 1
    if stats.portrait in NarcissusSkin_Chia_Farmers_List:
        stats.int = stats.int + 1
    if stats.portrait in PaleMauveSkin_Chia_Farmers_List:
        stats.wis = stats.wis + 1
    if stats.portrait in VermeilSkin_Chia_Farmers_List:
        stats.str = stats.str + 1
    if stats.portrait in CrySkin_Chia_Farmers_List:
        stats.cha = stats.cha + 1
        stats.wis = stats.wis + 1
        stats.luc = stats.luc - 2
    if stats.portrait in RainbowSkin_Chia_Farmers_List:
        stats.health = stats.health + 1
        Rainbow_castchance = random.randint(1, 20)
        if Rainbow_castchance in [10, 20]:
            stats.int = stats.int + 1
            stats.cha = stats.cha + 1
            stats.wis = stats.wis + 1
            stats.dex = stats.dex + 1
            stats.str = stats.str + 1
            stats.con = stats.con + 1
            stats.health = stats.health + 1

    if stats.portrait in WaterTools_Chia_Farmers_List:
        stats.con = stats.con + 1
    if stats.portrait in SickleTools_Chia_Farmers_List:
        stats.str = stats.str + 1
    if stats.portrait in ShelfTools_Chia_Farmers_List:
        stats.dex = stats.dex + 1
    if stats.portrait in SaplingTools_Chia_Farmers_List:
        stats.luc = stats.luc + 1
    if stats.portrait in PitchforkTools_Chia_Farmers_List:
        stats.str = stats.str + 1
    if stats.portrait in MagicTools_Chia_Farmers_List:
        stats.int = stats.int + 1
    if stats.portrait in FlowersTools_Chia_Farmers_List:
        stats.cha = stats.cha + 1
    if stats.portrait in DoorplateTools_Chia_Farmers_List:
        stats.wis = stats.wis + 1
    if stats.portrait in ChiaFarmTools_Chia_Farmers_List:
        stats.health = stats.health + 1
        ChiaFarm_castchance = random.randint(1, 20)
        if ChiaFarm_castchance in [10, 20]:
            stats.health = stats.health + 2

    return stats
