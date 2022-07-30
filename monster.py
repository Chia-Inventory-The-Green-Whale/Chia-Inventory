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
        monster.description = "A murloc adapts aquatic environment. Lives on the Continent of Aquarum"
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
        monster.description = "A murloc adapts aquatic environment. Lives on the Continent of Aquarum"
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
        monster.description = "A murloc king adapts aquatic environment. Lives on the Continent of Aquarum"
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
        monster.description = "A skeleton warrior adapts graveyard environment. Lives on the Continent of Aquarum"
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
        monster.description = "A hungry wolf adapts dark woods environment. Lives in the black Forest"
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
        monster.description = "A thief adapts dark woods environment. Lives in the black Forest and in Western Woods"
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

    #Continent - Harenae Desert
    #Fire creature - would be weak to water / ice attack strong against fire
    if monster.name == "Scorpion":
        monster.DEFslash = 2
        monster.DEFbash = 1
        monster.DEFpierce = 2
        monster.attack = 5 + random.randint(1, 5)
        monster.coin = 4
        monster.health = 40 + random.randint(1, 5)
        monster.exp = 4
        monster.author = "Da8erRul85#2286 xch1fvk9fn4jlvpgsyy7sz0akyuqyvvefcltnhzmrkxkukzrckd3fdmq08lgy0"
        monster.description = "A oversized Scorpion. Living in the deserts of Harenae"
        monster.skill = "poison"
        monster.attack_name = "pierce"

    if monster.name == "Rabid Hyena":
        monster.DEFslash = 0
        monster.DEFbash = 1
        monster.DEFpierce = 0
        monster.attack = 6 + random.randint(2, 7)
        monster.coin = 6
        monster.health = 60 + random.randint(1, 5)
        monster.exp = 5
        monster.author = "Da8erRul85#2286 xch1fvk9fn4jlvpgsyy7sz0akyuqyvvefcltnhzmrkxkukzrckd3fdmq08lgy0"
        monster.description = "A Rabid Hyena laughs madly at the adventurers. Living in the deserts of Harenae"
        monster.skill = "rush"
        monster.attack_name = "bite"

    #Earth Creature
    #Would be weak to fire magic
    if monster.name == "Living Cactus":
        monster.DEFslash = 0
        monster.DEFbash = 2
        monster.DEFpierce = 1
        monster.attack = 0 + random.randint(1, 20)
        monster.coin = 6
        monster.health = 40 + random.randint(1, 5)
        monster.exp = 7
        monster.author = "Da8erRul85#2286 xch1fvk9fn4jlvpgsyy7sz0akyuqyvvefcltnhzmrkxkukzrckd3fdmq08lgy0"
        monster.description = "A haunted cactus came to life by imbalance of nature. Living in the deserts of Harenae"
        monster.skill = "shoot needles"
        monster.attack_name = "pierce"

    # If Elementary mage system is implemented
    # Would have strong def against fire
    # Would be weak against water
    # Other magic would be neutral
    # Has strong physical defense
    if monster.name == "Fire Elemental":
        monster.DEFslash = 3
        monster.DEFbash = 3
        monster.DEFpierce = 3
        monster.attack = 5 + random.randint(3, 15)
        monster.coin = 20
        monster.health = 60 + random.randint(1, 20)
        monster.exp = 10
        monster.author = "Da8erRul85#2286 xch1fvk9fn4jlvpgsyy7sz0akyuqyvvefcltnhzmrkxkukzrckd3fdmq08lgy0"
        monster.description = "Elements of fire are out of control. This monster glides on a flame over the lands. It has two montrous arms and a head. Living in the deserts of Harenae and at hot and volcaneous places."
        monster.skill = "fireball"
        monster.attack_name = "burn"

    #Would be extremely weak against fire
    if monster.name == "Earth Elemental":
        monster.DEFslash = 3
        monster.DEFbash = 3
        monster.DEFpierce = 3
        monster.attack = 15 + random.randint(3, 5)
        monster.coin = 20
        monster.health = 80 + random.randint(1, 10)
        monster.exp = 10
        monster.author = "Da8erRul85#2286 xch1fvk9fn4jlvpgsyy7sz0akyuqyvvefcltnhzmrkxkukzrckd3fdmq08lgy0"
        monster.description = "Elements of earth are out of control. This monster is made out of rock. Every step of it make the earth shake. It throws rocks with it monstrous arms. Living in the deepest nature of Salvia Continent."
        monster.skill = "throw rocks"
        monster.attack_name = "bash"

    #Would be extremely weak against earth
    if monster.name == "Air Elemental":
        monster.DEFslash = 3
        monster.DEFbash = 3
        monster.DEFpierce = 3
        monster.attack = 5 + random.randint(3, 15)
        monster.coin = 20
        monster.health = 60 + random.randint(1, 20)
        monster.exp = 10
        monster.author = "Da8erRul85#2286 xch1fvk9fn4jlvpgsyy7sz0akyuqyvvefcltnhzmrkxkukzrckd3fdmq08lgy0"
        monster.description = "Elements of air are out of control. This monster glides on a tornado out of dust. Electric lighning flashes through the body of this monster. Unprepared adventurers will be zapped to death. Living in the deepest nature of Salvia Continent."
        monster.skill = "tornado"
        monster.attack_name = "zap"

    #Would be extremely weak against air / electro
    if monster.name == "Water Elemental":
        monster.DEFslash = 3
        monster.DEFbash = 3
        monster.DEFpierce = 3
        monster.attack = 8 + random.randint(1, 5)
        monster.coin = 20
        monster.health = 60 + random.randint(1, 20)
        monster.exp = 10
        monster.author = "Da8erRul85#2286 xch1fvk9fn4jlvpgsyy7sz0akyuqyvvefcltnhzmrkxkukzrckd3fdmq08lgy0"
        monster.description = "Elements of water are out of control. This monster is a gigantic gliding water drop with ice crystals circling above it's head. Weak adventurers will be drowned or frozen"
        monster.skill = "freeze"
        monster.attack_name = "splash"

    # Air Creature
    # Would be weak against Earth attacks
    # High possibility to dodge
    if monster.name == "Griffin":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 0
        monster.attack = 3 + random.randint(2, 10)
        monster.coin = 5
        monster.health = 40 + random.randint(1, 5)
        monster.exp = 4
        monster.author = "Da8erRul85#2286 xch1fvk9fn4jlvpgsyy7sz0akyuqyvvefcltnhzmrkxkukzrckd3fdmq08lgy0"
        monster.description = "A mythical creature with the head and wings of an eagle. Living in Mountain areas"
        monster.skill = "dash"
        monster.attack_name = "claw"


    #Glacies - the ice lands
    # Ice / Water Creature
    # Would be weak against air / electro
    if monster.name == "Ice Wolf":
        monster.DEFslash = 1
        monster.DEFbash = 2
        monster.DEFpierce = 1
        monster.attack = 6 + random.randint(1, 8)
        monster.coin = 6
        monster.health = 60 + random.randint(1, 5)
        monster.exp = 6
        monster.author = "Da8erRul85#2286 xch1fvk9fn4jlvpgsyy7sz0akyuqyvvefcltnhzmrkxkukzrckd3fdmq08lgy0"
        monster.description = "A mystical wolf living in the cold ice of Glacies"
        monster.skill = "ice breath"
        monster.attack_name = "bite"

    #Would be weak against Air (electro)
    if monster.name == "Yeti":
        monster.DEFslash = 1
        monster.DEFbash = 3
        monster.DEFpierce = 1
        monster.attack = 8 + random.randint(1, 10)
        monster.coin = 6
        monster.health = 100 + random.randint(1, 20)
        monster.exp = 15
        monster.author = "Da8erRul85#2286 xch1fvk9fn4jlvpgsyy7sz0akyuqyvvefcltnhzmrkxkukzrckd3fdmq08lgy0"
        monster.description = "A big yeti lifing in the cold ice of Glacies"
        monster.skill = "throw chunks of ice"
        monster.attack_name = "bash"

    #Would be weak against Air (electro)
    if monster.name == "Ice Crab":
        monster.DEFslash = 3
        monster.DEFbash = 1
        monster.DEFpierce = 2
        monster.attack = 5 + random.randint(1, 8)
        monster.coin = 3
        monster.health = 70 + random.randint(1, 10)
        monster.exp = 5
        monster.author = "Da8erRul85#2286 xch1fvk9fn4jlvpgsyy7sz0akyuqyvvefcltnhzmrkxkukzrckd3fdmq08lgy0"
        monster.description = "A ice crab living on icy shores"
        monster.skill = "icy jet of water"
        monster.attack_name = "pinch"

    if monster.name == "Mimic Chest":
        monster.DEFslash = 2
        monster.DEFbash = 0
        monster.DEFpierce = 2
        monster.attack = 0 + random.randint(1, 15)
        monster.coin = 1 + random.randint(1, 20)
        monster.health = 50 + random.randint(1, 10)
        monster.exp = 6
        monster.author = "Da8erRul85#2286 xch1fvk9fn4jlvpgsyy7sz0akyuqyvvefcltnhzmrkxkukzrckd3fdmq08lgy0"
        monster.description = "Looks like an ordinary treasure chest, but has teeth as sharp as a shark. Snaps unsuspecting adventurers. Lives at haunted places"
        monster.skill = "sleeping gas" #Character cannot attack for one round
        monster.attack_name = "snap shut"


    #Would be weak against fire
    if monster.name == "Mimic Book":
        monster.DEFslash = 0
        monster.DEFbash = 2
        monster.DEFpierce = 1
        monster.attack = 5 + random.randint(1, 10)
        monster.coin = 1 + random.randint(1, 20)
        monster.health = 40 + random.randint(1, 10)
        monster.exp = 6
        monster.author = "Da8erRul85#2286 xch1fvk9fn4jlvpgsyy7sz0akyuqyvvefcltnhzmrkxkukzrckd3fdmq08lgy0"
        monster.description = "Looks like an ordinary book, but spells magic against unsuspecting adventurers."
        monster.skill = "fireball" #Character cannot attack for one round
        monster.attack_name = "lightning spell"

            
    return (monster)
