from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, Inventory, Character, Landmark
from django.http import JsonResponse

beginning_inventory = {
    "food": "A day's food for your team.",
    "cd": "A cd",
    "Bible": "A Gideon Bible",

}

place_list = {
    "camp": "a camp",
    "hotel": "a hotel",
    "pack": "a pack"}

landmarks = {"Oregon Border":
                 {"story": "You make camp on ",
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

initial_inv = Inventory.objects.create(name="initial_inv")
player_inv = Inventory.objects.create(name="player_inv")
place_inventory = Inventory.objects.create(name="place_inv")


"""This help function instantiates characters and connects them to the player inventory."""


def create_characters(name1, name2, name3, name4):
    character1 = Character.objects.create(name=name1, inventory=player_inv)
    character2 = Character.objects.create(name=name2, inventory=player_inv)
    character3 = Character.objects.create(name=name3, inventory=player_inv)
    character4 = Character.objects.create(name=name4, inventory=player_inv)


"""This helper function creates the initial inventory in packing view. """


def create_initial_inventory():
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


"""This helper function creates all the place inventories and found items in play view."""

def create_place_inventories():
    places = place_list.keys()
    for place in places:
        find = Item.objects.create(name=place, description=place_list[place],
                                       inventory=place_inventory)


def landmark_outcomes(name):
    milestone = landmarks[name]
    ldmk = Landmark.objects.create(name=name)
    find = Item.objects.create(name=milestone["gain"], description=milestone["gain"], landmark=ldmk, inventory=place_inventory)
    player_inventory = player_inv.items.all()
    has_key = None
    for item in player_inventory:
        if item.name == milestone["key"]:
            has_key = True
            break
        else:
            has_key = False
    if has_key == True:
        find.landmark = None
        find.inventory = player_inv
        find.save()
    if has_key == False:
        for item in player_inventory:
            if item.name == milestone["loss"]:
                item.inventory = place_inventory
                item.save()


def gameplay(request):
    return render(request, 'game/gameplay.html', {})

    #Choice is returned in gameplay_entry view.


def gameplay_entry(request):
    if request.method == 'POST':
        choice = request.POST.get("choice", None)
    return JsonResponse({"choice": choice})


def names(request):
    # create_characters() # add variables for name1 through name4
     return render(request, 'game/names.html', {})


def names_entry(request):
    if request.method == 'POST':
        name2 = request.POST.get("name2", None)
        name3 = request.POST.get("name2", None)
        name4 = request.POST.get("name2", None)
        name5 = request.POST.get("name2", None)
    return JsonResponse({"name2": name2,
                         "name3": name3,
                         'name4': name4,
                         'name5': name5,
                         })

    #The form on this page needs to instantiate Character models with the entered names.
    #The form also needs to allow the user to go on to the packing screen.


def packing(request):
    # Turn most of this into a helper function that systematically creates an initial inventory
    create_initial_inventory()
    initial_inventory = initial_inv.items.all()
    return render(request, 'game/packing.html', {"initial_inventory": initial_inventory})

    #The form on this page needs to change the entered item's inventory to player_inventory.
    #The form on this page also needs to allow the user to go to the depart screen.


def packing_entry(request):
    if request.method == 'POST':
        pack = request.POST.get("pack_item", None)
    return JsonResponse({"pack_item)": pack})


def depart(request):
    player_inv = Inventory.objects.create()
    player_inventory = player_inv.items.all()
    return render(request, 'game/depart.html', {"player_inventory": player_inventory})

    #The form on this page needs to allow the user to:
        #  remove items from the pack and return them to initial_inv
        #  go back to the pack screen
        #  go on to the play screen

def depart_entry(request):
    if request.method == 'POST':
        unpack = request.POST.get("unpack", None)
    return JsonResponse({"unpack": unpack})


def play(request):
    create_place_inventories()
    return render(request, 'game/play.html', {})


def play_entry(request):
    if request.method == 'POST':
        move = request.POST.get("move", None)
    return JsonResponse({"move": move})


def win(request):
    return render(request, 'game/win.html', {})