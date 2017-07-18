from django.contrib import admin
from .models import Address, Order, Pizza, Toppings

admin.site.register(Address)
admin.site.register(Order)
admin.site.register(Pizza)
admin.site.register(Toppings)