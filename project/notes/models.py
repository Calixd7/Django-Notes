from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
class Note(models.Model):
    text = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)