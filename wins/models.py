from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
# from pyuploadcare.dj.models import ImageField
from django import forms

# Create your models here.


class User(models.Model):
    '''
    Method to create users profile
    '''
    is_authenticated = True
    username = models.CharField(max_length =50)
    useremail = models.CharField(max_length = 140)
    userpassword = models.CharField(max_length = 100)
    last_login = models.DateField(auto_now=True)
    profilepic = models.CharField(max_length = 225, default = "")


class Profile(models.Model):
    '''
    Method to create profile table
    '''

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    pic = ImageField(blank=True, manual_crop="")
    bio = models.CharField(default="Hi!", max_length = 30)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    @classmethod
    def search_user(cls,name):
        return User.objects.filter(username__icontains = name)