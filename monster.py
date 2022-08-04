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
    # Urban Residents
    if monster.name == "Cockroach":
        monster.attack = 1 + random.randint(1, 3)
        monster.health = 5 + random.randint(1, 3)
        monster.author = "Chia Inventory#9520"  #
        monster.description = "A house pest common in urban area"
        monster.skill = "rush"
        monster.attack_name = "bite"

    if monster.name == "Mouse":
        monster.attack = 1 + random.randint(1, 3)
        monster.health = 10 + random.randint(1, 5)
        monster.exp = 1
        monster.author = "Chia Inventory#9520"
        monster.description = "A house pest common in urban area"
        monster.skill = "rush"
        monster.attack_name = "bite"

    if monster.name == "Drunk Man":
        monster.attack = 1 + random.randint(1, 3)
        monster.health = 20 + random.randint(1, 5)
        monster.exp = 1
        monster.coin = 1
        monster.author = "Chia Inventory#9520"
        monster.description = "Drunk men can always be observed in the tavern"
        monster.skill = "broken wine bottle"
        monster.attack_name = "punch"

    if monster.name == "Thief":
        monster.attack = 3 + random.randint(1, 3)
        monster.health = 10 + random.randint(1, 5)
        monster.exp = 1
        monster.coin = 1
        monster.author = "Chia Inventory#9520"
        monster.description = "Thieves can always be observed in the market"
        monster.skill = "dagger"
        monster.attack_name = "punch"

    if monster.name == "Scum":
        monster.attack = 2 + random.randint(1, 3)
        monster.health = 15 + random.randint(1, 5)
        monster.exp = 1
        monster.coin = 1
        monster.author = "Chia Inventory#9520"
        monster.description = "Scums can always be found in the city"
        monster.skill = "dagger"
        monster.attack_name = "punch"

    if monster.name == "City Guard":
        monster.attack = 5 + random.randint(1, 3)
        monster.health = 120 + random.randint(1, 5)
        monster.exp = 1
        monster.coin = 3
        monster.author = "Chia Inventory#9520"
        monster.description = "The guard is stationed here, he said: hunting is not permitted!"
        monster.skill = "sword"
        monster.attack_name = "punch"

    # Slimes
    if monster.name == "Slime":
        monster.DEFpierce = 1
        monster.attack = 1 + random.randint(1, 5)
        monster.coin = 1
        monster.health = 15 + random.randint(1, 5)
        monster.exp = 1
        monster.author = "Chia Inventory#9520"
        monster.description = "A normal slime"
        monster.skill = "rush"
        monster.attack_name = "bump"

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
     
    # Cave Residents
     if monster.name == "Rock Slime":
        monster.DEFslash = 0
        monster.DEFbash = 3
        monster.DEFpierce = 0
        monster.attack = 2 + random.randint(1, 5)
        monster.coin = 2
        monster.health = 65 + random.randint(1, 10)
        monster.exp = 3
        monster.author = "chiaslimes#0354 xch1l4h559qkc284tc4rf0wp4umdxr8mk6jqymwwtjg0psmk4wmqracs632kmv"
        monster.description = "A slime adapts cave environment"
        monster.skill = "rock spikes"
        monster.attack_name = "bump"
        
    if monster.name == "Cave Bear":
        monster.DEFslash = 1
        monster.DEFbash = 2
        monster.DEFpierce = 0
        monster.attack = 2 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 3
        monster.health = 100 + random.randint(1, 10)
        monster.exp = 3
        monster.author = "chiaslimes#0354 xch1l4h559qkc284tc4rf0wp4umdxr8mk6jqymwwtjg0psmk4wmqracs632kmv"
        monster.description = "While smaller then his brothers in the forest, his roar is amplfied by it's cove habitat and strikes fear in any who challege."
        monster.skill = "roar"
        monster.attack_name = "demoralizing roar"
        
    if monster.name == "Cave Troll":
        monster.DEFslash = 2
        monster.DEFbash = 2
        monster.DEFpierce = 0
        monster.attack = 4 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 5
        monster.health = 200 + random.randint(1, 10)
        monster.exp = 5
        monster.author = "chiaslimes#0354 xch1l4h559qkc284tc4rf0wp4umdxr8mk6jqymwwtjg0psmk4wmqracs632kmv"
        monster.description = "The caves are a Trolls home turf - take care when challenging them."
        monster.skill = "club bash"
        monster.attack_name = "club bash"
        
    if monster.name == "Cave Imp Warrior":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 0
        monster.attack = 1 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 2
        monster.health = 75 + random.randint(1, 10)
        monster.exp = 2
        monster.author = "chiaslimes#0354 xch1l4h559qkc284tc4rf0wp4umdxr8mk6jqymwwtjg0psmk4wmqracs632kmv"
        monster.description = "Imps are rarely seen outdoors, they enjoy the silence and solitude of caves."
        monster.skill = "spear attack"
        monster.attack_name = "imp poke"
        
    if monster.name == "Cave Imp Mage":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 0
        monster.attack = 2 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 2
        monster.health = 55 + random.randint(1, 10)
        monster.exp = 2
        monster.author = "chiaslimes#0354 xch1l4h559qkc284tc4rf0wp4umdxr8mk6jqymwwtjg0psmk4wmqracs632kmv"
        monster.description = "Some Imps dable in the magic arts...but they are not very reliable at it..."
        monster.skill = "rock throw"
        monster.attack_name = "rock throw"
                
    # Murloc
    if monster.name == "Murloc Grunt":
        monster.DEFslash = 1
        monster.DEFbash = 0
        monster.DEFpierce = 0
        monster.attack = 1 + random.randint(1, 5)
        monster.coin = 1
        monster.health = 20 + random.randint(1, 5)
        monster.exp = 1
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "They are known for their odd sound mrglwglwlg, which translates to I kill you human stinker or I love you, translators still have problems understanding them, maybe because most of them died trying. Murlocs have fishlike skin, body consists of two legs and two arms. Don't be afraid, they are stupid warriors lurking in shallow water near lakes and shoreline."
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
        monster.description = "Whenever you meet her, it means there are lots of murlocs around protecting their queen. She is known for trying to seduce everyone she meets in order to increase population of her army. Murloc King doesn't like that, so you better keep your hands off her. If she tries to seduce you, it is better for you to close eyes and sing lala for the next 3minutes, or not .. whichever you prefer ^^."
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
        monster.description = "He is always busy looking at his queen and making sure she isn't cheating. But even a king has to sleep from time to time, and each time he wakes up, population of murlocs somehow increases. He might not be the best husband but don't underestimate him, he is the strongest among murlocs, heavy crown on his head is enchanted and makes any murloc wearing it very strong .... hold your horses I said it is only for murlocs, so unless you are one forget about taking it. If you manage to kill him, there are plenty other murlocs to take his place, king is dead long live the king or mrglwglwlg as murlocs say."
        monster.skill = "trident fury"
        monster.attack_name = "flesh slash mrglwglwlg"

    # Graveyard Residents
    if monster.name == "Skeleton Warrior":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 4 + random.randint(1, 5)
        monster.coin = 3
        monster.health = 50 + random.randint(1, 10)
        monster.exp = 3
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "You take some body, preferably a dead one, add a sword and a shield, throw them in a grave. And years later ask some nice smiling necromancer to help you raise an army. They are not the fastets warrior around but boy they don't feel pain either."
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
        monster.description = "They are basicly same as skeleton warriors with one but, they still have some brain leftover in their skulls making them smart enough to use some simple magic like fire. Their magic fireballs can really hurt, but they are weak enough to be killed quickly. Some necromancers use them as a lighter that is always there."
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
        monster.description = "Some necromancers are in a hurry and can't wait for flesh to rot, so instead of skeletons they make zombies. Zombies have some cons, they are slower, they make too much noise and they are too stiff to hold weapons so they only bite. On the pros side a zombie is sturdy as a tank, still plenty of hp left in those rotten corpses that just walk in search for ... BRAINS."
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
        monster.description = "This is just a normal slime but soaked with dark magic, making it more ressistant to physical attacks. Remember to wash off the smell after defeating one of them, who knows where they have been."
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
        monster.description = "They are mostly lost souls that can't find their way, wil you help them ... with your sword ? Oh and always make sure your weapon have some iron in it, you can also try to steal some salt from Tavern just in case you need protection from ghosts, but stealing in tavern might be worse than fighting a ghost. Anyway in case you are unarmed and you see a ghost, then who you gonna call ? Noone you marshmallow, there are no phones in this game, just run."
        monster.skill = "fear"
        monster.attack_name = "scare"

    if monster.name == "Bat":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 2 + random.randint(1, 5)
        monster.coin = 2
        monster.health = 40 + random.randint(1, 10)
        monster.exp = 2
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "Creature of night, so untill you light your torch it will have all the advantage it needs. Some adventurers report that they lost blood and didn't even knew when. Most of bats lives in dark caves or very dark woods."
        monster.skill = "echo"
        monster.attack_name = "bloodsuck"

    # Dark Forest Residents
    if monster.name == "Sleepy Bear":
        monster.DEFslash = 1
        monster.DEFbash = 2
        monster.DEFpierce = 1
        monster.attack = 3 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 5
        monster.health = 120 + random.randint(1, 10)
        monster.exp = 5
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "Why, oh why did someone have to wake it up ? Don't we already have full hands of fighting with everything around ? It is just a bear, an angry and strong one. Next time just let him sleep."
        monster.skill = "Honey hunger"
        monster.attack_name = "big angry bite"

    if monster.name == "Hungry Wolf":
        monster.DEFslash = 0
        monster.DEFbash = 1
        monster.DEFpierce = 0
        monster.attack = 3 + random.randint(1, 5)
        monster.coin = 2
        monster.health = 45 + random.randint(1, 5)
        monster.exp = 2
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "Have you ever been so hungry that You would eat anything ? Even if the meal is wearing metal armor and has a sword ? If yes then you were a wolf in your previous life. They don't mind you being strong, they are hungry and forest is their playground, you are their cheewing toy on two legs."
        monster.skill = "howl"
        monster.attack_name = "hungry bite"

    if monster.name == "Forest Thief":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 0
        monster.attack = 5 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 4
        monster.health = 35 + random.randint(1, 5)
        monster.exp = 4
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "Everyone knows a guy that didn't give them their money back. He is hidding in shadows of dark woods, running away from people that are mad at him. Lucky for him noone is that stupid to look in dark woods, or is there someone ? Well meeting a forest thief might be last thing you do, with his backstab from shadows your life usually ends quickly. "
        monster.skill = "sneaky"
        monster.attack_name = "backstab"

    if monster.name == "Corrupted Living Tree":
        monster.DEFslash = 0
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 1 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 3
        monster.health = 100 + random.randint(1, 5)
        monster.exp = 3
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "Grandparents usually tell their grandchildren stories of times past. Well this isn't this story, it involves a drunk necromancer that was cursed by heartbroken witch. He was so drunk that he had to take a piss, he did that near a tree. Seconds after his relief, tree became alive and pissed off by someone naked in front of it, killed the pure yet still drunk necromancer. Now corrupted tree is wandering the woods in search of a dry towel. Be careful of what you do in the woods."
        monster.skill = "grab"
        monster.attack_name = "squeeze"

    if monster.name == "Crazy Witch":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 4 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 5
        monster.health = 60 + random.randint(1, 5)
        monster.exp = 5
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "Maybe you heard stories about a necromancer, who fell in love with a witch. Well he's the one. Long story short, he dumped her, she went mental and now everyone is calling her crazy. Ofcourse behind her back, noone is brave enough to face her in combat. Broken heart made her magic stronger."
        monster.skill = "witchcraft"
        monster.attack_name = "curse"

    if monster.name == "Poisonous Fungus":
        monster.DEFslash = 0
        monster.DEFbash = 0
        monster.DEFpierce = 0
        monster.attack = 6 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 3
        monster.health = 30 + random.randint(1, 5)
        monster.exp = 3
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "It looks like a normal fungus untill it tries to poison you. You die or hold breath long enough to kill it. End of story."
        monster.skill = "poison cloud"
        monster.attack_name = "poison"

    # Naga
    if monster.name == "Naga Warrior":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 1 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 2
        monster.health = 40 + random.randint(1, 5)
        monster.exp = 2
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "Remember murlocs ? Now imagine a bigger stronger murloc without legs but with snakelike body, with scales instead of skin, with some brain instead of a peanut, that is naga. They are great warriors so watch out."
        monster.skill = "sword slash"
        monster.attack_name = "slash"

    if monster.name == "Naga Caster":
        monster.DEFslash = 1
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 5 + random.randint(1, 5) + random.randint(1, 5)
        monster.coin = 3
        monster.health = 30 + random.randint(1, 5)
        monster.exp = 3
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "Fish and snake like creature that is often protected by their warriors counterparts. It can control element of water, I hope you can swim in case it tries to drown you in a magic water bubble."
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
        monster.description = "She is a hell of a singer. She knows how to motivate her soldiers, for other nagas sounds she makes are beautiful. For you dear adventurer they are terrible, like nails on a chalkboard."
        monster.skill = "screech"
        monster.attack_name = "eardrums blow"

    # Beach Residents
    if monster.name == "Red Crab":
        monster.DEFslash = 2
        monster.DEFbash = 1
        monster.DEFpierce = 1
        monster.attack = 3 + random.randint(1, 10)
        monster.coin = 4
        monster.health = 70 + random.randint(1, 5)
        monster.exp = 4
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "It is a crab, it walks sideways. It can pinch you like you have never been pinched before. Oh and it is red ... or green, We are not sure, because our adventurer was a daltonist untill he died from eating wrong mushrooms."
        monster.skill = "pincer"
        monster.attack_name = "strong pinch"

    if monster.name == "Pearl Clam":
        monster.DEFslash = 5
        monster.DEFbash = 5
        monster.DEFpierce = 5
        monster.attack = 1 + random.randint(1, 5)
        monster.coin = 10 + random.randint(1, 10)
        monster.health = 200 + random.randint(1, 20) + random.randint(1, 20)
        monster.exp = 0
        monster.author = "Aquankh#0309 xch1htsukhsh2yrp5mqa344qya3xpqgenad9xcmfyaj3drl0hadgu80qw9q3yv"
        monster.description = "Every adventurer dreams about a treasure. Well here is it, inside a clam, and that clam is somewhere deep. Not very precise but we really don't know where exactly it is right now. Maybe there is more than one. All we know is that fighting with it is like hitting a wall, just watch out for splinters they are painfull."
        monster.skill = "my precious"
        monster.attack_name = "splinter"

    # Continent - Harenae Desert
    # Fire creature - would be weak to water / ice attack strong against fire
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

    # Earth Creature
    # Would be weak to fire magic
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

    # Would be extremely weak against fire
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

    # Would be extremely weak against earth
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

    # Would be extremely weak against air / electro
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

    # Glacies - the ice lands
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

    # Would be weak against Air (electro)
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

    # Would be weak against Air (electro)
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
        monster.skill = "sleeping gas"  # Character cannot attack for one round
        monster.attack_name = "snap shut"

    # Would be weak against fire
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
        monster.skill = "fireball"  # Character cannot attack for one round
        monster.attack_name = "lightning spell"

    # exp and coin formula
    monster.exp = int(monster.health / 6) + int((monster.DEFslash + monster.DEFbash + monster.DEFpierce) / 2) + int(
        monster.attack / 5)
    monster.coin = int(monster.exp/4) + random.randint(0, monster.exp)

    return (monster)
