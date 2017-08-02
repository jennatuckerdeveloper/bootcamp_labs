from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, Inventory, Character, Landmark

# places = {"camp": "a camp", "hotel": "a hotel", "pack": "a pack"}
# #this dictionary will become code to systematically create places
# finds = {"camp": Food(), "hotel": Item("bible", "a Gideon Bible"), "pack": Item("cd", "a cd")}
#this dictionary will become code to systematically create items connected to those places


# landmarks = {"Oregon Border":
#                  {"story": "You make camp on ",
#                   "pack": "food",
#                   "gain": Food(),
#                   "loss": Food(),
#                   "story_loss": "You lose one day's food.",
#                   "story_gain": "After finding the Bible in your packs, the group allows you to rest on their land and offers you a gift of food to help you on your way."
#                   },
#              "Eugene":
#                  {"story": "You have reached Eugene.",
#                   "pack": "",
#                   "gain": Item("cd", "a cd"),
#                   "loss": Food(),
#                   "story_loss": "You lose one day's food.",
#                   "story_gain": "You receive a CD.",
#                   },
#              "Salem":
#                  {"story": "You have reached Salem.",
#                   "pack": "",
#                   "gain": Item("book", "a book"),
#                   "loss": Food(),
#                   "story_loss": "You lose a day's food.",
#                   "story_gain": "You receive a book.",
#                   },
#              }

#Figure out how to systematically create Landmark experiences


# def outcome(self):
#     for x in self.inventory.items.all():
#         if x.name == key:
#             have = True
#
#     if have == True:
#         self.items.inventory = player_inventory
#         print(story_gain)
#
#     else:
#         self.supplies.inventory.remove(self.loss)
#         print(story_loss)
#
#
# def arrive(self):
#     print(self.story)
#     self.outcome()

#use if/else statements to check the number of items in the inventory on the pack screen and in places


def gameplay(request):
    return render(request, 'game/gameplay.html', {})

    #The form on this page needs to create a limit for the number of items allowed in player_inventory at the end of hte packs screen.
    #The form also needs to allow the user to go on to the names screen.

def names(request):
    return render(request, 'game/gameplay.html', {})

    #The form on this page needs to instantiate Character models with the entered names.
    #The form also needs to allow the user to go on to the packing screen.

def packing(request):
    # Turn most of this into a helper function that systematically creates an initial inventory
    initial_inv = Inventory.objects.create()
    food = Item.objects.create(name="Food", description="A day's food for your team.", inventory=initial_inv)
    food = Item.objects.create(name="Food", description="A day's food for your team.", inventory=initial_inv)
    cd = Item.objects.create(name="cd", description="a cd", inventory=initial_inv)
    initial_inventory = initial_inv.items.all()
    return render(request, 'game/packing.html', {"initial_inventory": initial_inventory})

    #The form on this page needs to change the entered item's inventory to player_inventory.
    #The form on this page also needs to allow the user to go to the depart screen.

def depart(request):
    player_inv = Inventory.objects.create()
    food = Item.objects.create(name="Food", description="A day's food for your team.", inventory=player_inv)
    food = Item.objects.create(name="Food", description="A day's food for your team.", inventory=player_inv)
    cd = Item.objects.create(name="cd", description="a cd", inventory=player_inv)
    player_inventory = player_inv.items.all()
    return render(request, 'game/depart.html', {"player_inventory": player_inventory})

    #The form on this page needs to allow the user to:
        #  remove items from the pack and return them to initial_inv
        #  go back to the pack screen
        #  go on to the play screen

def play(request):
    return render(request, 'game/play.html', {})

def win(request):
    return render(request, 'game/win.html', {})