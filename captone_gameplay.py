from python_capstone import Character, Inventory, Item, Food

"""
Game play:
"""

print("Welcome to PDX Trail!")

name1 = Character(input("Choose a character name: "))
name2 = Character(input("Choose a second character name: "))
name3 = Character(input("Choose a third character name: "))
name4 = Character(input("Choose a fourth character name: "))
name5 = Character(input("Choose a fifth character name: "))

"""
Instantiates an inventory for the player.
Loads the 5 characters into the inventory.
"""

player_inventory = Inventory()

player_inventory.get_item(name1)
player_inventory.get_item(name2)
player_inventory.get_item(name3)
player_inventory.get_item(name4)
player_inventory.get_item(name5)

#The player's initial inventory should have a limit on items.
#Choose 3 different limits based on 3 character profiles to create levels of difficulty.
#The food items in the inventory should add up to a score.

"""
Creates an initial inventory to use in loading player inventory.
"""

print("Before you head out, choose what you will bring: ")

initial_inventory = Inventory()
food = Food()
initial_inventory.get_item(food)
initial_inventory.list_inventory()



player_inventory.pack_item(initial_inventory, food)
player_inventory.list_inventory()
initial_inventory.list_inventory()

"""
Main game menu.  Each run through creates a turn or a day.  
"""
