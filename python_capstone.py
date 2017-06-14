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

Game Play:
1) Walk on.
2) Lie down a while.
3)

The characters will be in the inventory.
So a function should print the inventory items, perhaps not including the characters.
There should be a way to have things happen to all the characters in the inventory and to one of them.
"""


"""
Creates characters with their own names and health score.  
"""


class Character:
    def __init__(self, name, description=100):
        self.name = name
        self.description = description
    def __str__(self):
        return "{} is at {} health.".format(self.name, self.description)
    def __repr__(self):
        return str(self)
    def die(self):
        if self.health <= 0:
            print("{} has died.".format(self.name))
            #The character is not yet removed from the player inventory.

#There's probably a way to make the health/description print
#A great, good, fair, poor, bad according to the number.

class Inventory:
    def __init__(self):
        self.inventory = []


    def get_item(self, item):
        self.inventory.append(item)


    def pack_item(self, source, item):
        choice = source.inventory.index(item)
        source.inventory.pop(choice)
        self.get_item(item)


    def list_inventory(self):
        for each in self.inventory:
            print(each.name, each.description)

    def look(self):
        pass

    """
    There will be one player inventory.
    There will be place inventories.  
    There will be "random" inventories.  
    """


class Item:
    def __init__(self, name, description, type):
        self.name = name
        self.description = description
        self.type = type
    def __str__(self):
        return "{}: {}".format(self.name, self.description)
    def __repr__(self):
        return str(self)

class Food(Item):
    def __init__(self):
        self.nutrition = 20
        super().__init__(name="Food", description="A day's food for one person.", type="food")

#There might be a way to add the nutrition perameter to any
#item created that has the name "Food" and no others.





