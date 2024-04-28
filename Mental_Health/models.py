from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"Profile of {self.user.username}"
