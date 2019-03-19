from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from pyuploadcare.dj.models import ImageField
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

    avatar = models.ImageField(upload_to='photos/',null=True)
    fullname = models.CharField(max_length=255,null=True)
    username = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = HTMLField(null=True)
    email = models.EmailField(null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
       if created:
           Profile.objects.create(username=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
       instance.profile.save()

    def __str__(self):
        return self.username.username

    @classmethod
    def search_profile(cls,search_term):
        profiles = cls.objects.filter(Q(username__username=search_term) | Q(fullname__icontains=search_term))
        return profiles

class Image(models.Model):
    image = ImageField(blank=True, manual_crop="")    
    title = models.CharField(max_length = 31, blank = True)
    posted_by = models.CharField(max_length = 50, blank = True)
    # likes = models.ManyToManyField(User, related_name = "likes", blank = True)
    user = models.ForeignKey(User,null = True , blank = True , on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True, blank = True)
    description = models.TextField(blank=True)
    technologies = models.CharField(max_length=200, blank=True)
    link = models.CharField(max_length=200,)

    def save_image(self):
        self.save()

    def delete_image(self):
        cls.objects.get(id = self.id).delete()

    def update_posted_by(self,new_posted_by):
        self.posted_by = new_caption
        self.save()