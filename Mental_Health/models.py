# models.py

from django.contrib.auth.models import User
from django.db import models


from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100,blank=True, null=True)
    contact_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.user.username




class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
