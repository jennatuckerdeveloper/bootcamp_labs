import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'capstone.settings')
import django
django.setup()

from game.models import Item, Inventory

pi = Inventory.objects.create(name="pi")

one = Item.objects.create(name="one", description="one", inventory=pi)
two = Item.objects.create(name="two", description="two", inventory=pi)
three = Item.objects.create(name="three", description="three", inventory=pi)

pi.theft()
pi.depression()