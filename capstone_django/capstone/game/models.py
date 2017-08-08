from django.db import models
from random import randrange
from authentication.models import User

class Character(models.Model):

    name = models.CharField(max_length=100)
    description = models.IntegerField(default=100)
    inventory = models.ForeignKey("Inventory", related_name="characters")

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
    inventory = models.ForeignKey("Inventory", related_name="items", blank=True, null=True)
    landmark = models.ForeignKey("Landmark", related_name="landmark", blank=True, null=True)

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
An Inventory has an inventory list and a limit to the number of Items it can hold.
"""

#This one needs a lot of work

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    limit = models.IntegerField(blank=True, null=True)
    day_counter = models.IntegerField(default=0)
    mile_counter = models.IntegerField(default=0)
    last_milestone = models.CharField(max_length=200, default="start")

    def __str__(self):
        return "{}: {}".format(self.name, self.items.all())

    def __repr__(self):
        return self.name
        # return self.__str__()

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
    #This function might need to be made more random.
        for x in self.characters.all():
            if x.name == "You":
                print("{} are depressed".format(x.name))
                x.description -= 15
            else:
                print("{} is depressed.".format(x.name))
                x.description -= 15
            break

    def rain(self):
        print("A cold rain comes.")
        for x in self.characters.all():
            x.description -= 10

#Place are Inventories of Items with unique names.
# If the user chooses to take Items from the inventory, the Item's inventory = changes.

class Landmark(models.Model):
    name = models.CharField(max_length=100)

    """
    Landmarks will be systematically generated.  
    The will have a name based on the place.
    Items will be systematically generated and connected to Landmarks by FK.
    """

class Game(models.Model):
    user = models.ForeignKey(User, related_name="user")
    inventory = models.ForeignKey("Inventory", related_name="player_inv")
