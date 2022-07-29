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


def locate(location):
    here = room(location)
    if here.location == 'Kingdom Street':
        here.description = "Location: Kingdom Street; This place is bustling with people. \nYou noticed that there is an obvious exit: East (Slime Forest)"
        here.monsters = ['Cockroach', 'Cockroach', 'Cockroach', 'Cockroach', 'Cockroach',
                         'Cockroach', 'Cockroach', 'Mouse', 'Mouse', 'Mouse']
        here.east = 'Slime Forest'


    if here.location == 'Slime Forest':
        here.description = "Location: Slime Forest; You are surrounded by woods. \nYou noticed that there is an obvious exit: West (Kingdom Street)"
        here.monsters = ['Forest Slime', 'Forest Slime', 'Forest Slime', 'Forest Slime', 'Forest Slime',
                         'Aquatic Slime', 'Forest Slime', 'Forest Slime', 'Aquatic Slime',
                         'Swamp Slime']
        here.west = 'Kingdom Street'

    return here
