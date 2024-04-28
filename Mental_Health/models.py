<<<<<<< HEAD
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"Profile of {self.user.username}"
=======
# models.py

from django.contrib.auth.models import User
from django.db import models
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields as needed

    def __str__(self):
        return self.user.username
>>>>>>> 350f9ad34db95c79f8eae526011254450f6b977c
