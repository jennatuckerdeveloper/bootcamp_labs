"""

The foundation for a parody of the Oregon Trail.

Character Object:
5 characters in a dictionary with names as keys and health as value
can individually die - removed when drops beneath 100
    randomized methods that affect one character's health
    decisions that affect all characters' health
five names as inputs
health begins at default (interacts with moves / days / segments)


Inventory Object:
1 character inventory
    chosen from initial stores
1 limit to inventory

Stopping point stores:  place inventories / npc inventories

Trades:  limited exchanges between character inventory and stopping points inventories

Places:

Trail segements
Stopping points / intermediate destinations / places with inventories

Movement - pace and days in segments

Crossings / major decision points

Map



The characters will be in the inventory.
So a function should print the inventory items, perhaps not including the characters.
There should be a way to have things happen to all the characters in the inventory and to one of them.
"""


"""
Creates characters with their own names and health score.  
"""

from random import choice

class Character:
    def __init__(self, name, description=100):
        self.name = name
        self.description = description
        self.type = "character"
    def __str__(self):
        if 0 < self.description <= 25:
            return "{} is in poor health.".format(self.name)
        elif 26 <= self.description <= 50:
            return "{} is in fair health.".format(self.name)
        elif 51 <= self.description <= 75:
            return "{} is in decent health.".format(self.name)
        elif 76 <= self.description <= 100:
            return "{} is in good health.".format(self.name)
    def __repr__(self):
        return str(self.name)
    def die(self):
        if self.health <= 0:
            print("{} has died.".format(self.name))
            #The character is not yet removed from the player inventory.

class Item:
    def __init__(self, name, description, type="item"):
        self.name = name
        self.description = description
        self.type = type
    def __str__(self):
        return "{}: {}".format(self.name, self.description)
    def __repr__(self):
        return str(self.name)
        #return self.__str__()

class Food(Item):
    def __init__(self):
        # self.nutrition = 20
        super().__init__(name="Food", description="A day's food for one person.", type="food")


class Inventory:
    def __init__(self, limit=None):
        self.inventory = []
        self.limit = limit

    def get_item(self, item):
        self.inventory.append(item)


    def pack_item(self, source, item):
        choice = source.inventory.index(item)
        source.inventory.pop(choice)
        self.get_item(item)

    def list_inventory(self):
        print(self.inventory)
        for each in self.inventory:
            print(each)


    # def random_find(self):
    #     finds = {"camp": Food(), "empty hotel": Item("Gideon Bible"), "backpack": Item("cd")}
    #     find = choice(finds)
    #     return find

    """
    There will be one player inventory.
    There will be a handful of larger place inventories.  
    There will be many small "random" inventories.  
    """
class Place:
    def __init__(self, name):
        places = {"camp": "a camp", "hotel": "a hotel", "pack": "a pack"}
        finds = {"camp": Food(), "hotel": Item("bible", "a Gideon Bible"), "pack": Item("cd", "a cd")}
        self.name = name
        self.description = places[name]
        self.finds = finds[name]

    def __str__(self):
        return "You come across a {} and find: \n{}".format(self.description, self.finds.description)