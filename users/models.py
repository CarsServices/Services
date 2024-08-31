from django.db import models
# from email.policy import default
from django.contrib.auth.models import User
from .utils import user_directory_path

class Location(models.Model):
    Address_1 = models.CharField(max_length=120)
    Address_1 = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=110)
    state = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return f'Location {self.id}'


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to =user_directory_path, null=True)  # the upload to will help us upload the profile images to a folder we will create
    # i then set a function called user_directory_path to get user's directory path which was created in the  utils.py file in the users folder but first import it at the top //line 4
    bio = models.CharField(max_length=300, blank=True)
    phone_number = models.CharField(max_length=19, blank=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'
