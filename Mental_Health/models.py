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


from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100,blank=True, null=True)
    contact_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.user.username
<<<<<<< HEAD




class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
=======
>>>>>>> 350f9ad34db95c79f8eae526011254450f6b977c
>>>>>>> 967c7b562581d0740427a4c0ebeb0e57d51fd579
