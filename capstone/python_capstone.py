"""

The foundation for a parody of the Oregon Trail.

"""

from random import randrange

class Character:
    """
    Creates characters with their own names and health score.
    """
    def __init__(self, name, description=100):
        self.name = name
        self.description = description
        self.type = "character"
    def __str__(self):
        if self.name == "You":
            if 0 < self.description <= 25:
                return "{} are in poor health.".format(self.name)
            elif 26 <= self.description <= 50:
                return "{} are in fair health.".format(self.name)
            elif 51 <= self.description <= 75:
                return "{} are in decent health.".format(self.name)
            elif 76 <= self.description <= 100:
                return "{} are in good health.".format(self.name)
        else:
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
        super().__init__(name="Food", description="A day's food for your group.", type="food")


class Inventory:
    def __init__(self, limit=None):
        self.inventory = []
        self.limit = limit

    def get_item(self, item):
        if self.limit is not None:
            if len(self.inventory) <= self.limit:
                self.inventory.append(item)
            elif len(self.inventory) > self.limit:
                print("You don't have enough room. ")
        else:
            self.inventory.append(item)

    def pack_item(self, source, item):
        for x in source.inventory:
            if x.name == item:
                self.get_item(x)
                source.inventory.remove(x)
                break

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

class Occurrence:
    def __init__(self, supplies):
        self.supplies = supplies


    def theft(self):
        loss = []
        luck = randrange(1, 3)
        while luck > 0:
            for x in self.supplies.inventory:
                if x.type != "character":
                    if luck > 0:
                        loss.append(x)
                        self.supplies.inventory.remove(x)
                    luck -= 1
        print("A thief comes in the night and steals the following: ")
        for i in loss:
            print("{}".format(i))


    def depression(self):
        for x in self.supplies.inventory:
            if x.type == "character":
                if x.name == "You":
                    print("{} are depressed".format(x.name))
                    x.description -= 15
                else:
                    print("{} is depressed.".format(x.name))
                    x.description -= 15
                break

    def rain(self):
        print("A cold rain comes.")
        for x in self.supplies.inventory:
            if x.type == "character":
                x.desciption -= 10

