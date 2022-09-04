from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload


class User_profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True)
    name=models.CharField(max_length=20, blank=True)
    lastname=models.CharField(max_length=20, blank=True)
    adress = models.CharField(max_length=200, blank=True)
    profile_image = models.ImageField(upload_to='profile_image/', blank=True, null=True)

    def __str__(self):
        return self.user.username + ' - profile'