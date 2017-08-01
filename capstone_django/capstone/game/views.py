from django.shortcuts import render
from django.http import HttpResponse

# places = {"camp": "a camp", "hotel": "a hotel", "pack": "a pack"}
# #this dictionary will become code to systematically create places
# finds = {"camp": Food(), "hotel": Item("bible", "a Gideon Bible"), "pack": Item("cd", "a cd")}
#this dictionary will become code to systematically create items connected to those places

def game(request):
    return render(request, 'game/game.html', {})


