from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    copies = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.title)