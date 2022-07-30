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
        
    if monster.name == "Murloc Grunt":
        monster.DEFslash = 1
        monster.DEFbash = 0
        monster.DEFpierce = 0
        monster.attack = 1 + random.randint(1, 5)
        monster.coin = 1
        monster.health = 20 + random.randint(1, 5)
        monster.exp = 1
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A murloc adapts aquatic environment"
        monster.skill = "spear attack"
        monster.attack_name = "piercing mrglwglwlg"

    if monster.name == "Murloc Queen":
        monster.DEFslash = 0
        monster.DEFbash = 1
        monster.DEFpierce = 0
        monster.attack = 4 + random.randint(1, 5)
        monster.coin = 2
        monster.health = 40 + random.randint(1, 10)
        monster.exp = 2
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A murloc adapts aquatic environment"
        monster.skill = "charming blink"
        monster.attack_name = "selfharm mrglwglwlg"

    if monster.name == "Murloc King":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 6 + random.randint(1, 5)
        monster.coin = 4
        monster.health = 100 + random.randint(1, 10)
        monster.exp = 5
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A murloc king adapts aquatic environment"
        monster.skill = "trident fury"
        monster.attack_name = "flesh slash mrglwglwlg"
       
    if monster.name == "Skeleton Warrior":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 4 + random.randint(1, 5)
        monster.coin = 3
        monster.health = 50 + random.randint(1, 10)
        monster.exp = 3
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A skeleton warrior adapts graveyard environment"
        monster.skill = "slash attack"
        monster.attack_name = "flesh wound"

    if monster.name == "Skeleton Mage":
        monster.DEFslash = 0
        monster.DEFbash = 0
        monster.DEFpierce = 0
        monster.attack = 4 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 3
        monster.health = 20 + random.randint(1, 5)
        monster.exp = 3
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A skeleton mage adapts graveyard environment"
        monster.skill = "fireball"
        monster.attack_name = "burn"

    if monster.name == "Zombie":
        monster.DEFslash = 0
        monster.DEFbash = 2
        monster.DEFpierce = 0
        monster.attack = 3 + random.randint(1, 5)
        monster.coin = 3
        monster.health = 150 + random.randint(1, 10)
        monster.exp = 3
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A zombie adapts graveyard environment"
        monster.skill = "bite"
        monster.attack_name = "eat brains"

    if monster.name == "Undead slime":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 3 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 5
        monster.health = 120 + random.randint(1, 10)
        monster.exp = 5
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A undead slime adapts graveyard environment"
        monster.skill = "death breath"
        monster.attack_name = "bump"

    if monster.name == "Ghost":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 1 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 3
        monster.health = 30 + random.randint(1, 5)
        monster.exp = 3
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A ghost adapts graveyard environment"
        monster.skill = "fear"
        monster.attack_name = "scare"
        
    if monster.name == "Bat":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 1 + random.randint(1, 5)
        monster.coin = 2
        monster.health = 40 + random.randint(1, 10)
        monster.exp = 2
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A bat adapts cave environment"
        monster.skill = "echo"
        monster.attack_name = "suck"

    if monster.name == "Sleepy Bear":
        monster.DEFslash = 1
        monster.DEFbash = 2
        monster.DEFpierce = 1
        monster.attack = 3 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 5
        monster.health = 120 + random.randint(1, 10)
        monster.exp = 5
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A sleepy bear adapts cave environment"
        monster.skill = "Honey hunger"
        monster.attack_name = "big bite"

    if monster.name == "Hungry Wolf":
        monster.DEFslash = 0
        monster.DEFbash = 1
        monster.DEFpierce = 0
        monster.attack = 3 + random.randint(1, 5)
        monster.coin = 2
        monster.health = 45 + random.randint(1, 5)
        monster.exp = 2
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A hungry wolf adapts dark woods environment"
        monster.skill = "howl"
        monster.attack_name = "bite"

    if monster.name == "Thief":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 0
        monster.attack = 5 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 4
        monster.health = 35 + random.randint(1, 5)
        monster.exp = 4
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A thief adapts dark woods environment"
        monster.skill = "sneaky"
        monster.attack_name = "backstab"

    if monster.name == "Corrupted living tree":
        monster.DEFslash = 0
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 1 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 3
        monster.health = 100 + random.randint(1, 5)
        monster.exp = 3
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A corrupted living tree adapts dark woods environment"
        monster.skill = "grab"
        monster.attack_name = "squeeze"
        
    if monster.name == "Crazy witch":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 4 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 5
        monster.health = 60 + random.randint(1, 5)
        monster.exp = 5
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A crazy witch adapts dark woods environment"
        monster.skill = "witchcraft"
        monster.attack_name = "curse"
        
    if monster.name == "Poisonous Fungus":
        monster.DEFslash = 0
        monster.DEFbash = 0
        monster.DEFpierce = 0
        monster.attack = 5 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 3
        monster.health = 35 + random.randint(1, 5)
        monster.exp = 3
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A posionous fungus adapts dark woods environment"
        monster.skill = "poison cloud"
        monster.attack_name = "poison"

    if monster.name == "Naga warrior":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 1 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 2
        monster.health = 40 + random.randint(1, 5)
        monster.exp = 2
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A naga warrior adapts shoreline environment"
        monster.skill = "sword slash"
        monster.attack_name = "slash"

    if monster.name == "Naga caster":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 5 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 3
        monster.health = 30 + random.randint(1, 5)
        monster.exp = 3
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A naga caster adapts shoreline environment"
        monster.skill = "fireball"
        monster.attack_name = "fireball"

    if monster.name == "Naga Queen":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 5 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 6
        monster.health = 110 + random.randint(1, 5)
        monster.exp = 6
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A naga queen adapts shoreline environment"
        monster.skill = "screech"
        monster.attack_name = "eardrums blow"

if monster.name == "Red Crab":
        monster.DEFslash = 2
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 3 + random.randint(1, 10)
        monster.coin = 3
        monster.health = 70 + random.randint(1, 5)
        monster.exp = 3
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A red crab adapts shoreline environment"
        monster.skill = "pincer"
        monster.attack_name = "strong pinch"

if monster.name == "Pearl Clam":
        monster.DEFslash = 5
        monster.DEFbash = 5
        monster.DEFpierce = 5
        monster.attack = 1 + random.randint(1, 5)
        monster.coin = 10
        monster.health = 200 + random.randint(1, 20)
        monster.exp = 1
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "A pearl clam adapts deep water environment"
        monster.skill = "my precious"
        monster.attack_name = "splinter"
        
    return (monster)
