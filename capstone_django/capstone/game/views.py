from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, Inventory, Character, Landmark, Game
from authentication.models import User
from django.http import JsonResponse
from random import randrange, choice, randint


"""
TO DO:

How do I get the mile_count and day_count to appear on the play screen?  
Same question for:  
    Place finds
    Landmarks 
*There may be more information that needs to go into the database.  
*Does it go into the database?  Or can info be generated in the view, put into the 
    context dictionary, and brought into to the template?  
*Essentially, these "print" functions should mostly be going to a single place on the play screen.  

How do I end the game when "You" dies?  
How do I create a quit() option?  

Create an inventory view screen with character health and what's in the pack.

How do I limit what the user can viably enter?  Try/except?  
How do I limit viable item names to select list?
How do I limit the number of items in the pack?  
How do I let the user unpack an item?  

"""

beginning_inventory = {
    "food": "A day's food for your team.",
    "cd": "A cd",
    "Bible": "A Gideon Bible",

}

place_list = {
    "camp":
        {"description": "a camp",
         "find": "food"
         },
    "hotel":
        {"description": "a hotel",
         "find": "Bible",
         },
    "pack":
        {"description": "a pack",
         "find": "cd"
         }
            }

landmarks = {"Oregon Border":
                 {"story": "You have reached the Oregon Border.  You make camp on... ",
                  "key": "Bible",
                  "gain": "cd",
                  "loss": "food",
                  "story_loss": "You lose one day's food.",
                  "story_gain": "After finding the Bible in your packs, the group allows you to rest on their land and offers you a gift of food to help you on your way."
                  },
             "Eugene":
                 {"story": "You have reached Eugene.",
                  "key": "Bible",
                  "gain": "cd",
                  "loss": "food",
                  "story_loss": "You lose one day's food.",
                  "story_gain": "You receive a CD.",
                  },
             "Salem":
                 {"story": "You have reached Salem.",
                  "key": "Bible",
                  "gain": "cd",
                  "loss": "food",
                  "story_loss": "You lose a day's food.",
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
    print(player_inventory)
    milestone = landmarks[name]
    ldmk = Landmark.objects.create(name=name)
    find = Item.objects.create(name=milestone["gain"], description=milestone["gain"], landmark=ldmk, inventory=None)
    has_key = None
    for item in player_inventory.items.all():
        if item.name == milestone["key"]:
            has_key = True
            print(True)
            break
        else:
            has_key = False
            print(False)
    if has_key == True:
        find.landmark = None
        find.inventory = player_inventory
        find.save()
        print(player_inventory)
    if has_key == False:
        for item in player_inventory.items.all():
            if item.name == milestone["loss"]:
                item.inventory = None
                item.save()
                print(player_inventory)


def gameplay(request):
    return render(request, 'game/gameplay.html', {})


def gameplay_entry(request):
    if request.method == 'POST':
        print(request.user.username)
        user = User.objects.get(username=request.user.username)
        limit = 0
        if request.POST.get("choice", None) == str(1):
            limit = 15
            print("1")
        if request.POST.get("choice", None) == str(2):
            limit = 10
            print("2")
        if request.POST.get("choice", None) == str(3):
            limit = 5
            print("3")
        print(limit)
        inv = Inventory(name="player_inv", limit=limit)
        inv.save()
        user.game = inv
        user.save()
        return JsonResponse({'message': 'success'})
    return JsonResponse({'message': 'fail'})

#This needs a try/except to ensure it's one of these three.

def names(request):
    # create_characters() # add variables for name1 through name4
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
        print(inv.characters.all)
        return JsonResponse({'message': 'success'})
    return JsonResponse({'message': 'fail'})

#This one doesn't print to the console properly.  Not sure why.

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
    # i_inv = create_initial_inventory()
    # return render(request, 'game/packing.html', {"initial_inventory": i_inv})

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

        # user = User.objects.get(username=request.user.username)
        # player_inventory = user.game
        # to_pack = Item.objects.get(name=request.POST.get('choice', None))
        # to_pack.inventory = player_inventory
        # print(player_inventory)


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
    play_message = player_inventory.play_message

    return render(request, 'game/play.html', {"mile_counter": mile_counter, "day_counter": day_counter, "play_message": play_message})


def play_entry(request):
    user = User.objects.get(username=request.user.username)
    player_inventory = user.game
    mile_counter = player_inventory.mile_counter
    day_counter = player_inventory.day_counter
    play_message = player_inventory.play_message
    player_inventory.play_message = ""
    player_inventory.save()
    if request.method == 'POST':
        if request.POST.get("move", None) == str(1):
            player_inventory.mile_counter += randint(12, 22)
            player_inventory.day_counter += 1
            player_inventory.save()
            for i in player_inventory.characters.all():
                    i.description -= 5
                    i.save()
            for i in player_inventory.items.all():
                if i.name == "food":
                    i.inventory = None
                    i.save()
                    break
    #What's up with the indentation on this if/else statement???
            else:
                warning = "You have run out of food."
                player_inventory.play_message = warning
                player_inventory.save()
                for i in player_inventory.characters.all():
                    i.description -= 20
                    i.save()
                    print(i.description)

            for i in player_inventory.characters.all():
                dead = []
                if i.description <= 0:
                    if i.name != "You":
                        i.inventory = None
                        i.save()
                        notice = "{} has died of hunger and exhaustion.".format(i.name)
                        dead.append(notice)
                    if i.name == "You":
                        notice = "You have died of hunger and exhaustion."
                        dead.append(notice)
                message = ""
                for notice in dead:
                    message = message + notice + "\n"
                player_inventory.play_message = message
                player_inventory.save()
                        #How do I add an exit to end the game here???

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
                    print(landmarks[milestones[x][1]]["story"])
                    player_inventory.last_milestone = milestones[x][1]
                    player_inventory.save()
                    landmark_outcomes(milestones[x][1], player_inventory)
                    # Will likely error at the end of the game without another line of code.

        if request.POST.get("move", None) == str(2):
            player_inventory.day_counter += 1
            for i in player_inventory.characters.all():
                if i.description <= 100:
                    i.description += 20
                if i.description > 100:
                    i.description = 100

        if request.POST.get("move", None) == str(3):
            places = []
            for i in place_list.keys():
                places.append(i)
            find = choice(places)
            print(place_list[find]["description"])
            print(place_list[find]["find"])

            #Add decision
            #Add ability to unpack item

        return JsonResponse({'message': 'success', "mile_counter": mile_counter, "day_counter": day_counter, "play_message": play_message})
    else:
        print("No")
        return JsonResponse({'message': 'fail'})


def win(request):
    return render(request, 'game/win.html', {})