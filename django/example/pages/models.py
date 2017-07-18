from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    name = models.CharField(max_length=255)
    streets = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    #anything that is optional should get blank and null = True

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return '{} - {}'.format(self.name, self.streets)

    def get_full_address(self):
        return "{}, {}. {}".format(self.streets, self.city, self.zip)

class Order(models.Model):
    address = models.ForeignKey('Address')
    total = models.FloatField(default=0)
    entered_by = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
       return self.address.get_full_address()

#This is a Django Query

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        pies = Pizza.objects.filter(order__pk=self.pk)
        total = 0
        for p in pies:
            total += p.price
        self.total = total
        super().save(*args, **kwargs)

class Pizza(models.Model):
    order = models.ForeignKey('Order')
    size = models.CharField(max_length=255)
    toppings = models.ManyToManyField('Toppings')
    price = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.order.pk, self.order.address.name)

    def save(self, *args, **kwargs):
        if self.pk:
            super().save(*args, **kwargs)
        else:
            self.order.total += self.price
            super().save(*args, **kwargs)

class Toppings(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Toppings"
