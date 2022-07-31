import random
import json
from pprint import pprint

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
    with open('rudolf/locations_data.json') as file:
        data = json.load(file)
        #print(type(data))
    if location in data['locations']:
        #print(data['locations'][location])
        ldat=data['locations'][location]
        here = room(location)
        here.description = ldat['description']
        #TODO should be able to write this shorter. iterate through all simple strings ['east','north','area_type'] and so on
        if "east" in ldat:
            here.east = ldat['east']
        if "north" in ldat:
            here.north = ldat['north']
        if "south" in ldat:
            here.south = ldat['south']
        if "west" in ldat:
            here.west = ldat['west']
        if "area_type" in ldat:
            here.area_type = ldat['area_type']
        if "monsters" in ldat:
            for monster in ldat['monsters']:
                for i in range(monster['count']):
                    here.monsters.append(monster['name'])
    return here

        
        

    
