import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'capstone.settings')
import django

django.setup()

from game.models import Item, Inventory, Character, Landmark


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

player_inv = Inventory.objects.create(name="player_inv")

def landmark_outcomes(name):
    milestone = landmarks[name]
    ldmk = Landmark.objects.create(name=name)
    find = Item.objects.create(name=milestone["gain"], description=milestone["gain"], landmark=ldmk, inventory=None)
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
        print(find.inventory)
    #It prints the correct inventory.  But it does not print itself among the items.  WHAT?
    if has_key == False:
        print("Loss is:" + milestone["loss"])


one = Item.objects.create(name="Bible", description="a Gideon Bible", inventory=player_inv)

landmark_outcomes("Oregon Border")



#Fix weird bug in function called landmark_outcomes.  See comment there.
# Find an example of a url tag (in a template?) that takes the user to another page.
# Create links so that form entries go somewhere and send to next screen.
# Create links so that form entries run functions.
