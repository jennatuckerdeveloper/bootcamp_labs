from django.db import models
from random import randrange


class Character(models.Model):

    name = models.CharField(max_length=100)
    description = models.IntegerField(default=100)
    type = models.CharField(max_length=100, default="character")

    """
    The __str__ function prints a readable description of characters' health status.
    """

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

    """
    The __repr__ function shows characters printed in a list as their names.
    """

    def __repr__(self):
        return str(self.name)

        # The character is not yet removed from the player inventory.


"""
The Item class creates Items with unique names and descriptions and a default type.
"""

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    type = models.CharField(max_length=100, default="item")
    inventory = models.ForeignKey("Inventory", related_name="items")


    """
    Prints a readable version of the Item's name: description.  
    """
    def __str__(self):
        return "{}: {}".format(self.name, self.description)

    """
    Prints the item's name when the Item is printed in a list.  
    """
    def __repr__(self):
        return self.name
        # return self.__str__()

"""
Food Items have a default name, description, and type.  
"""


class Food(models.Model):
    name = models.CharField(max_length=100, default="Food")
    description = models.CharField(max_length=300, default="A day's food for your group.")
    type = models.CharField(max_length=100, default="food")


"""
An Inventory has an inventory list and a limit to the number of Items it can hold.
"""

#This one needs a lot of work

class Inventory(models.Model):
    name = models.CharField(max_length=100)

    """
    The list_inventory function prints each Item in the Inventory.  
    Kept for testing.  Should be unncessary after Django refactoring.
    """

    def list_inventory(self):
        for each in self.items.all():
            print(each)

    def theft(self):
        luck = randrange(1, 3)
        loss = []
        while luck > 0:
            for x in self.items.all():
                if x.type != "character":
                    if luck > 0:
                        loss.append(x)
                        x.inventory = None
                        luck -= 1
        print("A thief comes in the night and steals: ")
        for x in loss:
            print(x.name)


    def depression(self):
        for x in self.items.all():
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
                x.description -= 10


#Place are Inventories.  If the user chooses to take Items from the inventory, the Item's inventory = changes.

class Landmark:
    def __init__(self, name, supplies):
        self.name = name
        self.supplies = supplies

        landmarks = {"Oregon Border":
                         {"story": "You make camp on ",
                          "pack": "food",
                          "gain": Food(),
                          "loss": Food(),
                          "story_loss": "You lose one day's food.",
                          "story_gain": "After finding the Bible in your packs, the group allows you to rest on their land and offers you a gift of food to help you on your way."
                          },
                     "Eugene":
                         {"story": "You have reached Eugene.",
                          "pack": "",
                          "gain": Item("cd", "a cd"),
                          "loss": Food(),
                          "story_loss": "You lose one day's food.",
                          "story_gain": "You receive a CD.",
                          },
                     "Salem":
                         {"story": "You have reached Salem.",
                          "pack": "",
                          "gain": Item("book", "a book"),
                          "loss": Food(),
                          "story_loss": "You lose a day's food.",
                          "story_gain": "You receive a book.",
                          },
                     }
        self.story = landmarks[name]["story"]
        self.gain = landmarks[name]["gain"]
        self.loss = landmarks[name]["loss"]
        self.story_loss = landmarks[name]["story_loss"]
        self.story_gain = landmarks[name]["story_gain"]
        self.pack = landmarks[name]['pack']

    def outcome(self):
        """ The outcome function checks a character's inventory for the key associated with a Landmark
        Whehther the key is present in the inventory then calls a loss or a gain to the inventory.
        Do I need three functions to affect inventories, characters, etc like with luck?
        """
        have = []
        for x in self.supplies.inventory:
            if x.type == self.pack:
                have.append(x)

        if len(have) > 0:
            self.supplies.get_item(self.gain)
            print(self.story_gain)

        else:
            try:
                self.supplies.inventory.remove(self.loss)
                print(self.story_loss)
            except ValueError:
                pass

    def arrive(self):
        print(self.story)
        self.outcome()