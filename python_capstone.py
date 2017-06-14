"""

The foundation for a parody of the Oregon Trail.

"""


class Character:
    """
    Creates characters with their own names and health score.
    """
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
        for each in self.inventory:
            print(each)

class Place:
    def __init__(self, name, inventory=Inventory()):
        places = {"camp": "a camp", "hotel": "a hotel", "pack": "a pack"}
        finds = {"camp": Food(), "hotel": Item("bible", "a Gideon Bible"), "pack": Item("cd", "a cd")}
        self.inventory = inventory
        self.name = name
        self.description = places[name]
        self.finds = finds[name]
        self.inventory.get_item(self.finds)


    def __str__(self):
        return "You come across a {} and find: \n{}".format(self.description, self.finds.description)
