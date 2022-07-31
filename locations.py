import random
import json

class room:
    def __init__(self, location):
        self.location = location
        self.description = ""
        self.monsters = []
        self.east = self.location
        self.west = self.location
        self.south = self.location
        self.north = self.location
        self.area_type = "Wild"


def locate(location):
    here = room(location)
    if here.location == 'Kingdom Street':
        here.description = "Location: Kingdom Street; This place is bustling with people. \nYou noticed following exits: east (East Kingdom Street), north (Tavern), south (Marketplace)"
        here.monsters = ['Cockroach']*10 + ['Mouse']*10 + ['City Guard']*1
        here.east = 'East Kingdom Street'
        here.north = 'Tavern'
        here.south = 'Marketplace'
        here.area_type = "City"

    if here.location == 'Tavern':
        here.description = "Location: Tavern. \nYou noticed following exits: south (Kingdom Street)"
        here.monsters = ['Cockroach']*14 + ['Mouse']*4 + ['Drunk Man']*2 + ['City Guard']*1
        here.south = 'Kingdom Street'
        here.area_type = "City"

    if here.location == 'Marketplace':
        here.description = "Location: Marketplace; This place is bustling with people. \nYou noticed following exits: north (Kingdom Street)"
        here.monsters = ['Cockroach']*10 + ['Mouse']*4 + ['Thief']*4 + ['Scum']*2 + ['City Guard']*1
        here.north = 'Kingdom Street'
        here.area_type = "City"

    if here.location == 'East Kingdom Street':
        here.description = "Location: East Kingdom Street; This place is bustling with people. \nYou noticed following exits: east (Gate of Viridis), west (Kingdom Street), north (Blacksmith Shop), south (Stable)"
        here.monsters = ['Cockroach']*8 + ['Mouse']*8 + ['Thief']*4 + ['City Guard']*1
        here.east = 'Gate of Viridis'
        here.west = 'Kingdom Street'
        here.north = 'Blacksmith Shop'
        here.south = 'Stable'
        here.area_type = "City"

    if here.location == 'Blacksmith Shop':
        here.description = "Location: Blacksmith Shop; Adventurers gathered here for equipments. \nYou noticed following exits: south (East Kingdom Street)"
        here.monsters = ['Mouse'] + ['City Guard']*1
        here.south = 'East Kingdom Street'
        here.area_type = "City"

    if here.location == 'Stable':
        here.description = "Location: Stable; Adventurers gathered here for mounts, such as deers. \nYou noticed following exits: north (East Kingdom Street)"
        here.monsters = ['Cockroach']*10 + ['Mouse']*10 + ['City Guard']*1
        here.north = 'East Kingdom Street'

    if here.location == 'Gate of Viridis':
        here.description = "Location: Gate of Viridis. \nYou noticed following exits: west (East Kingdom Street), east (Border of Slime Forest)"
        here.monsters = ['Cockroach']*5 + ['Mouse']*4 + ['City Guard']*1
        here.east = 'Border of Slime Forest'
        here.west = 'East Kingdom Street'

    if here.location == 'Border of Slime Forest':
        here.description = "Location: Border of Slime Forest; You entered the forest. \nYou noticed following exits: west (Gate of Viridis), east (Slime Forest)"
        here.monsters = ['Slime']*7 + ['Forest Slime']*3
        here.west = 'Gate of Viridis'
        here.east = 'Slime Forest'

    if here.location == 'Slime Forest':
        here.description = "Location: Slime Forest; You are surrounded by woods. \nYou noticed following exits: west (Border of Slime Forest), east (Deep Slime Forest), north (A Lake in Slime Forest)"
        here.monsters = ['Slime']*3 + ['Forest Slime']*7
        here.west = 'Border of Slime Forest'
        here.east = 'Deep Slime Forest'
        here.north = 'A Lake in Slime Forest'

    if here.location == 'A Lake in Slime Forest':
        here.description = "Location: A Lake in Slime Forest; You see a lake here. \nYou noticed following exits: south (Slime Forest)"
        here.monsters = ['Forest Slime']*2 + ['Aquatic Slime']*4 + ['Murloc Grunt']*4
        here.south = 'Slime Forest'

    if here.location == 'Deep Slime Forest':
        here.description = "Location: Deep Slime Forest; You are surrounded by woods. \nYou noticed following exits: west (Slime Forest)"
        here.monsters = ['Forest Slime']*7 + ['Bat']*1 + ['Hungry Wolf']*1 + ['Swamp Slime']*1
        here.west = 'Slime Forest'


    return here
