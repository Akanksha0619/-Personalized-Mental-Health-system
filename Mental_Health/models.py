# models.py

from django.contrib.auth.models import User
from django.db import models
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields as needed

    def __str__(self):
        return self.user.username
