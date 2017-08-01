from django.shortcuts import render
from django.http import HttpResponse

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


def game(request):
    return render(request, 'game/game.html', {})


