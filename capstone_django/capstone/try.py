import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'capstone.settings')
import django
django.setup()

from game.models import Item, Inventory, Character, Landmark

pi = Inventory.objects.create(name="pi")
eug = Landmark.objects.create(name="Eugene")

one = Item.objects.create(name="one", description="one", inventory=pi)
two = Item.objects.create(name="two", description="two", inventory=pi)
three = Item.objects.create(name="three", description="three", inventory=pi)
jim = Character.objects.create(name="jim", inventory=pi)
one.inventory = None
one.landmark = eug
print(one.landmark)
# print(one.inventory)
# pi.theft()
# pi.depression()
# pi.rain()
