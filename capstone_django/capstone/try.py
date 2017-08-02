import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'capstone.settings')
import django

django.setup()

from game.models import Item, Inventory, Character, Landmark, Place



# Find an example of a url tag (in a template?) that takes the user to another page.
# Create links so that form entries go somewhere and send to next screen.
# Create links so that form entries run functions.
