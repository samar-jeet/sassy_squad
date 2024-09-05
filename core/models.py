from django.db import models

# Create your models here.
# models.py

from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200)
    details = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_approved = models.BooleanField(default=False)
#     image_url = models.URLField(max_length=200, blank=True, null=True)

#     def __str__(self):
#         return self.user.username





    

