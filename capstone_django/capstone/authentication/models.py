from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    game = models.CharField(max_length=2000)

    # def __str__(self):
    #     if self.last_name and self.first_name:
    #         return '{} {}'.format(self.first_name, self.last_name)
    #     else:
    #         return '{}'.format(self.username)