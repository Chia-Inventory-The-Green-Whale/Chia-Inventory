import random

class enemy:
    def __init__(self, name):
        self.name = name
        self.health = 20
        self.DEFslash = 0
        self.DEFbash = 0
        self.DEFpierce = 0
        self.loot = []
        self.attack = 0
        self.attack_name = "attack"
        self.coin = 0
        self.exp = 0
        self.description = ""
        self.author = ""
        self.skill = self.attack_name


def encounter(monster):
    monster = enemy(monster)
    if monster.name == "Cockroach":
        monster.DEFpierce = 1
        monster.attack = 1 + random.randint(1, 3)
        monster.health = 5 + random.randint(1, 3)
        monster.exp = 1
        monster.author = "Chia Inventory#9520" #
        monster.description = "A house pest common in urban area"
        monster.skill = "rush"
        monster.attack_name = "bite"

    if monster.name == "Mouse":
        monster.DEFpierce = 1
        monster.attack = 1 + random.randint(1, 3)
        monster.health = 10 + random.randint(1, 5)
        monster.exp = 1
        monster.author = "Chia Inventory#9520"
        monster.description = "A house pest common in urban area"
        monster.skill = "rush"
        monster.attack_name = "bite"

    if monster.name == "Forest Slime":
        monster.DEFpierce = 1
        monster.attack = 1 + random.randint(1, 5)
        monster.coin = 1
        monster.health = 20 + random.randint(1, 5)
        monster.exp = 1
        monster.author = "Chia Inventory#9520"
        monster.description = "A slime adapts forest environment"
        monster.skill = "rush"
        monster.attack_name = "bump"

    if monster.name == "Aquatic Slime":
        monster.DEFslash = 1
        monster.DEFpierce = 1
        monster.attack = 1 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 2
        monster.health = 30 + random.randint(1, 10)
        monster.exp = 2
        monster.author = "Chia Inventory#9520"
        monster.description = "A slime adapts aquatic environment"
        monster.skill = "spray water"
        monster.attack_name = "bump"

    if monster.name == "Swamp Slime":
        monster.DEFslash = 0
        monster.DEFbash = 0
        monster.DEFpierce = 1
        monster.attack = 2 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 3
        monster.health = 100 + random.randint(1, 10)
        monster.exp = 3
        monster.author = "Chia Inventory#9520"
        monster.description = "A slime adapts swamp environment"
        monster.skill = "acid eruption"
        monster.attack_name = "bump"

    return (monster)
