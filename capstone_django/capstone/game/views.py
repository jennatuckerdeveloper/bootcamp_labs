from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, Inventory, Character, Landmark, Game
from authentication.models import User
from django.http import JsonResponse
from random import randrange, choice, randint


"""

To do;
Need to end game when "You" dies.
Try/Excepts to limit options on all screens.  
Win condition.

Packing limits.  
Unpack screen.  

Inventory view screen:  characters and items 


*Does all info go into the database?  Or can info be generated in the view, put into the 
    context dictionary, and brought into to the template?  

"""

beginning_inventory = {
    "food": "A day's food for your team.",
    "cd": "A cd",
    "Bible": "A Gideon Bible",

}

place_list = {
    "camp":
        {"description": "a camp",
         "find_name": "food",
         "find_description": "a day's food",
         },
    "hotel":
        {"description": "a hotel",
         "find_name": "Bible",
         "find_description": "a Gideon Bible"
         },
    "pack":
        {"description": "a pack",
         "find_name": "cd",
         "find_description": "a cd"
         }
            }

landmarks = {"Oregon Border":
                 {"story": "You have reached the Oregon Border.  You make camp on... ",
                  "key": "Bible",
                  "gain": "food",
                  "loss": "food",
                  "story_loss": "You lose one day's food.",
                  "story_gain": "After finding the Bible in your packs, the group allows you to rest on their land and offers you a gift of food to help you on your way."
                  },
             "Eugene":
                 {"story": "You have reached Eugene.  You run into another party of campers...",
                  "key": "Bible",
                  "gain": "cd",
                  "loss": "food",
                  "story_loss": "You give them one day's food.",
                  "story_gain": "You receive a CD.",
                  },
             "Salem":
                 {"story": "You have reached Salem.  A homesteader gives your party beer...",
                  "key": "Bible",
                  "gain": "book",
                  "loss": "food",
                  "story_loss": "You lose a day's food throwing up.",
                  "story_gain": "You receive a book.",
                  },
             }


"""This helper function creates the initial inventory in packing view. """


def create_initial_inventory():
    initial_inv = Inventory.objects.create(name="initial_inv")
    items = []
    for x in beginning_inventory.keys():
        items.append(x)
    for x in range(len(beginning_inventory)):
        if items[x] != "food":
            name = Item.objects.create(name=items[x], description=beginning_inventory[items[x]], inventory=initial_inv)
        if items[x] == "food":
            y = 0
            while y < 5:
                name = Item.objects.create(name=items[x], description=beginning_inventory[items[x]],
                                           inventory=initial_inv)
                y += 1
    return initial_inv

"""This helper function creates all the place inventories and found items in play view."""

def create_place_inventories(place_inventory):
    places = place_list.keys()
    for place in places:
        find = Item.objects.create(name=place, description=place_list[place],
                                       inventory=place_inventory)


def landmark_outcomes(name, player_inventory):
    milestone = landmarks[name]
    ldmk = Landmark.objects.create(name=name)
    find = Item.objects.create(name=milestone["gain"], description=milestone["gain"], landmark=ldmk, inventory=None)
    has_key = None
    for item in player_inventory.items.all():
        if item.name == milestone["key"]:
            has_key = True
            break
        else:
            has_key = False
    if has_key == True:
        find.landmark = None
        find.inventory = player_inventory
        find.save()
        player_inventory.play_message = milestone["story_gain"]
    if has_key == False:
        for item in player_inventory.items.all():
            if item.name == milestone["loss"]:
                item.inventory = None
                item.save()
                break
        player_inventory.play_message = milestone["story_loss"]



def gameplay(request):
    return render(request, 'game/gameplay.html', {})


def gameplay_entry(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        limit = 0
        if request.POST.get("choice", None) == str(1):
            limit = 15
        if request.POST.get("choice", None) == str(2):
            limit = 10
        if request.POST.get("choice", None) == str(3):
            limit = 5
        inv = Inventory(name="player_inv", limit=limit)
        inv.save()
        user.game = inv
        user.save()
        return JsonResponse({'message': 'success'})
    return JsonResponse({'message': 'fail'})

#This needs a try/except to ensure it's one of these three.

def names(request):
     return render(request, 'game/names.html', {})


def names_entry(request):

    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        inv = user.game
        Character.objects.create(name="You", inventory=inv)
        Character.objects.create(name=request.POST.get('choice2', None), inventory=inv)
        Character.objects.create(name=request.POST.get('choice3', None), inventory=inv)
        Character.objects.create(name=request.POST.get('choice4', None), inventory=inv)
        Character.objects.create(name=request.POST.get('choice5', None), inventory=inv)
        user.save()
        inv.save()
        return JsonResponse({'message': 'success'})
    return JsonResponse({'message': 'fail'})


def show_game(request):
    user = User.objects.get(username=request.user.username)
    return render(request, 'pages/show_game.html', {'user': user})

#What is this function for?  Testing?



"""
The first version of packing and packing_entry created an initial inventory and changed inv to player inv.
"""

def packing(request):

    """
    This second version of the function needs a dictionary to print out the names of the items.
    """

    return render(request, 'game/packing.html', {})


def packing_entry(request):

    """
    This second version of the view function will need a dictionary to fill out descriptions.
    This or the next two functions need to set limit on player_inventory items.
    """
    if request.method == 'POST':

        user = User.objects.get(username=request.user.username)
        inv = user.game
        Item.objects.create(name=request.POST.get('choice', None), inventory=inv)
        print(inv)

        return JsonResponse({'message': 'success'})
    return JsonResponse({'message': 'fail'})


def depart(request):
    player_inv = Inventory.objects.create()
    player_inventory = player_inv.items.all()
    return render(request, 'game/depart.html', {"player_inventory": player_inventory})

    #The form on this page needs to allow the user to:
        #  remove items from the pack and return them to initial_inv.

def depart_entry(request):
    if request.method == 'POST':
        unpack = request.POST.get("unpack", None)
    return JsonResponse({"unpack": unpack})


def play(request):

    """This one is the heart of the game.
    Template:
        display mile_counter and day_counter (Do they need to be in the database to show in template?
        User needs to be able to:
            Walk
            Random events
            Forage / Scavenge (places)
            Landmarks
        This needs to allow the user to die / lose the game.
        This needs to allow the user to win.
    """

    place_inventory = Inventory.objects.create(name="place_inv")
    create_place_inventories(place_inventory)

    user = User.objects.get(username=request.user.username)
    player_inventory = user.game
    mile_counter = player_inventory.mile_counter
    day_counter = player_inventory.day_counter

    return render(request, 'game/play.html', {
        "mile_counter": mile_counter,
        "day_counter": day_counter,
    })


def play_entry(request):

    user = User.objects.get(username=request.user.username)
    player_inventory = user.game
    player_inventory.play_message = ""
    player_inventory.food_warning = ""
    player_inventory.death = ""
    player_inventory.happening = ""
    player_inventory.landmark = ""
    player_inventory.find = ""
    player_inventory.save()

    """
    The day_counter and mile_counter track each play and a day's food is lost.  
    """

    if request.method == 'POST':
        if request.POST.get("move", None) == str(1):
            player_inventory.mile_counter += randint(12, 22)
            player_inventory.day_counter += 1
            player_inventory.save()
            walkers = []

            for i in player_inventory.characters.all():
                i.description -= 5
                i.save()

            for i in player_inventory.items.all():
                if i.name == "food":
                    i.inventory = None
                    i.save()
                    break
            else:
                player_inventory.food_warning = "You have run out of food."
                player_inventory.save()
                for i in player_inventory.characters.all():
                    i.description -= 20
                    i.save()

            deaths = []
            for i in player_inventory.characters.all():
                if i.description <= 0:
                    deaths.append(i)
            print(deaths)
            if len(deaths) > 0:
                person = choice(deaths)
                if person.name != "You":
                    person.inventory = None
                    person.save()
                    player_inventory.death = "{} has died of hunger and exhaustion.".format(person.name)
                    player_inventory.save()
                    deaths.remove(person)
                if person.name == "You":
                    person.inventory = None
                    person.save()
                    player_inventory.death = "You have died of hunger and exhaustion."
                    player_inventory.save()
                    deaths.remove(person)
                for i in deaths:
                    i.description = 5
                    i.save()
                    print(i)



            """ The luck portion of play function creates random losses to inventory or individual or group health."""
            luck = randint(1, 3)

            if luck == 1:
                player_inventory.theft()
                player_inventory.save()

            if luck == 2:
                player_inventory.depression()
                player_inventory.save()

            if luck == 3:
                player_inventory.rain()
                player_inventory.save()

            """ The landmark section of the play function creates a unique storyline based on player inv."""

            milestones = [[50, "Salem"], [37, "Eugene"], [23, "Oregon Border"], [0, "start"]]

            for x in range(len(milestones) - 1):
                if player_inventory.mile_counter >= milestones[x][0] and player_inventory.last_milestone == milestones[x + 1][1]:
                    ms = Landmark(milestones[x][1], player_inventory)
                    player_inventory.landmark = (landmarks[milestones[x][1]]["story"])
                    player_inventory.save()
                    print(player_inventory.landmark)
                    player_inventory.last_milestone = milestones[x][1]
                    player_inventory.save()
                    landmark_outcomes(milestones[x][1], player_inventory)

        if request.POST.get("move", None) == str(2):
            player_inventory.day_counter += 1
            player_inventory.save()
            for i in player_inventory.characters.all():
                if i.description <= 100:
                    i.description += 20
                    i.save()
                if i.description > 100:
                    i.description = 100
                    i.save()

        if request.POST.get("move", None) == str(3):
            places = []
            for i in place_list.keys():
                places.append(i)
            find = choice(places)
            player_inventory.find = ("You find " + place_list[find]["description"] + " with " + place_list[find]["find_description"] + ".")
            player_inventory.save()
            gain = Item.objects.create(name=place_list[find]["find_name"], inventory=player_inventory)

            #Add decision
            #Add ability to unpack item

        return JsonResponse({
            'message': 'success',
            "mile_counter": player_inventory.mile_counter,
            "day_counter": player_inventory.day_counter,
            "play_message": player_inventory.play_message,
            "food_warning": player_inventory.food_warning,
            "death": player_inventory.death,
            "happening": player_inventory.happening,
            "find": player_inventory.find,
            "landmark": player_inventory.landmark,
        })
    else:
        return JsonResponse({'message': 'fail'})


def win(request):
    return render(request, 'game/win.html', {})