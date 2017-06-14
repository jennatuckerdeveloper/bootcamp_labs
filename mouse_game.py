"""The character class creates characters for our group game."""

import random

aggression=random.randrange(1, 5)

class Character:
    def __init__(self, name, description, inventory, health=100):
        self.description = description
        self.name = name
        self.inventory = list(inventory)
        self.health = health

    def move(self):
        """Allows a user to choose to leave / enter rooms."""
        pass

    def auto_move(self):
        """Computer automatically chooses a move."""
        pass

class Mouse(Character):
    def __init__(self, name, description, inventory, health=100):
        super().__init__(name, description, inventory, health=100)

    def take_food(self, my_food):
        choice = input("Add to health(h) or inventory(i)?")
        if choice == "h":
            self.health += my_food.score
        elif choice == "i":
            self.inventory.append(name)
        print(self.health, self.inventory)


class Rat(Character):
    def __init__(self, description, inventory, aggression=random.randrange(1, 2)):
        super().__init__(self, description, inventory)
        aggression = self.agression

class Cat(Character):
    def __init__(self, description, aggression=random.randrange(2, 3)):
        super().__init__(self, description, inventory)
        aggression = self.agression

class Dog(Character):
    def __init__(self, description, aggression=random.randrange(1, 4)):
        super().__init__(self, description, inventory)
        aggression = self.agression

class Person(Character):
    def __init__(self, description, inventory, aggression=random.randrange(1, 5)):
        super().__init__(self, description, inventory)
        aggression = self.agression

class Item:
    def __init__(self, name):
        name = self.name
        value = self.value

class Food(Item):
    def __init__(self, name, score):
        self.name = name
        self.description = description
        self.score = score


class Spell(Item):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def take_spell(self):



    # elif name == "fish":
    # elif name == "scare":
    # elif name == "hide":
    # elif name == "befriend":

horace = Mouse("Rasputin", "A wise mouse.", ["befriend"])
horace.find_item("bread")
bread = Food("bread", 20)
print(horace.take_food(bread))
