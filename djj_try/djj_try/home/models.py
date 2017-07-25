from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=200)
    info = models.TextField()
    num = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)

