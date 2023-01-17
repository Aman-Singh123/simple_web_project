
from django.db import models
from django.contrib.auth.models import AbstractUser
class Create_User(AbstractUser):
    Age=models.IntegerField()
    Address=models.CharField( max_length=250)
    def __str__(self) :
        return self.username