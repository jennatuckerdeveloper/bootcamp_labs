from python_capstone import Character, Item, Food, Inventory, Place
from random import randrange, choice

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


"""
Creates an initial inventory to use in loading player inventory.
"""

print("Before you head out, choose what you will bring: ")

initial_inventory = Inventory()
food = Food()
initial_inventory.get_item(food)
initial_inventory.get_item(food)
initial_inventory.get_item(food)
initial_inventory.get_item(food)
initial_inventory.get_item(food)
initial_inventory.get_item(food)
initial_inventory.list_inventory()



player_inventory.pack_item(initial_inventory, food)
player_inventory.pack_item(initial_inventory, food)
player_inventory.pack_item(initial_inventory, food)
player_inventory.pack_item(initial_inventory, food)
player_inventory.pack_item(initial_inventory, food)
player_inventory.pack_item(initial_inventory, food)
player_inventory.list_inventory()
initial_inventory.list_inventory()

"""
How do I set a limit on a list to limit an inventory?  
It's probably just an if/else using len(list).
But then how do I make it unique for each version?  
"""

"""
Main game menu. 

So what happens in a segment of the game?
At stops, there are decisions and also larger inventories.
You get to restock on food.  

Game Play:
1) Walk on.
2) Take some rest.
3) Explore the area.
4) Search through packs.  
5) Look at the map.


number of miles covered, distance counter 
    start set, make random, make choice 

a day counter (turn counter) 

your food stores go down
    start set, make choice 

generate discoveries and other choices / paths 

generate random discoveries of inventories 
    this replaces hunting:  you forage and scavenge 
    make some foods poison 
    make different for different game plays 
"""

mile_counter = 0
day_counter = 0


while True:
    try:
        play = input("""
                What do you want to do? 
                1) Walk on.
                2) Take some rest.
                3) Explore the area.
                4) Search through packs.  
                5) Look at the map.
                6) Quit 
              
            """)
    except ValueError:
        continue

    if play == "1":
        mile_counter += randrange(12, 22)
        day_counter += 1
        print("{} days on the trail.  {} miles covered.".format(day_counter, mile_counter))
        for i in player_inventory.inventory:
            if i.type == "character":
                i.description -= 5

        # eaten = 5
        # if any(x.type == "food" for x in player_inventory.inventory):
        #     while eaten > 0:
        #         temp = []
        #         for i in player_inventory.inventory:
        #             if i.type == "food":
        #                 temp.append(i)
        #         for i in temp:
        #             player_inventory.inventory.remove(i)
        #         eaten -= 1

        for x in player_inventory.inventory:
            if x.type == "food":
                player_inventory.inventory.remove(x)
                break

        else:
            print("You have run out of food.")
            for i in player_inventory.inventory:
                if i.type == "character":
                    i.description -= 20
                    print(i.description)

        if any(x.type == "character" for x in player_inventory.inventory):
            temp = []
            for i in player_inventory.inventory:
                if i.type == "character":
                    temp.append(i)
            for i in temp:
                if i.description <= 0:
                    player_inventory.inventory.remove(i)
                    print("{} has died of hunger and exhaustion.".format(i.name))

        if not any(x.type == "character" for x in player_inventory.inventory):
                print("Your team has died.")
                quit()

        #add random experiences

    elif play == "2":
        days = input("How many days do you want to rest? ")
        day_counter += int(days)
        for i in player_inventory.inventory:
            if i.type == "character":
                if i.description < 100:
                    i.description += (20 * int(days))

    elif play == "3":
        places = ["camp", "hotel", "pack"]
        #The places list matches the places list in the Place class.
        find = Place(choice(places))
        print(find)

        decision = input("Do you want to take what you found? ")
        if decision == "y":
             player_inventory.pack_item(find.inventory, find.finds)
        else:
            continue

        #this should have a limit. How to do this?

    elif play == "4":
        player_inventory.list_inventory()

    elif play == "5":
        pass
        #map goes last along with other graphics

    elif play == "6":
         quit()


# noinspection PyUnreachableCode
""" 

Finish building out the initial inventory. 
Allow user to choose what to pack.  

Put limit on player_inventory.  
Build 3 versions of play with profiles. 

Build random experiences into days.
  one that affects one character
  one that affects all characters
  one that affects other items in inventory 
  check bags and auto-play outcomes 
For this, I could build a class called Loss with 3 sub-types.
    makes a list of characters, chooses random, affects
    affects all characters
    makes list of food items, deletes two 
    
Create "milestones" reached that trigger parts of gameplay.
Build any larger places / inventories.
"""