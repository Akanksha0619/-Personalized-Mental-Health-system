
from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100,blank=True, null=True)
    contact_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"




class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
    



class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    search_statement = models.CharField(max_length=255)
    search_result = models.TextField()
    search_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.search_statement} - {self.search_date}"
