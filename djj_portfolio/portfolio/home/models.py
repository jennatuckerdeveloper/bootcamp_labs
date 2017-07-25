from django.db import models

class Project(models.Model):
    url = models.CharField(max_length=2000)

    def __str__(self):
        return "{}".format(self.url)
