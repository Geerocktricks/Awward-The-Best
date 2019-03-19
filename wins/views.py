from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User
from .models import Image,Profile,User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponseRedirect
from .forms import *


# Create your views here.

def welcome(request):
    '''
    Function to display the index page
    '''
    user = request.user
    all_images = []
    if request.method == "POST":
        form = ImageForm(request.POST)
        if form.is_valid():
            image = form.save(commit=False)
            image.save()
    else:
        form = ImageForm()

    try:
        images = Image.objects.all()
    except Image.DoesNotExist:
        images = None
    return render(request ,'index.html' , { 'images': images , 'form': form})

def signup(request):
    '''
    Function to return the signup page
    '''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request , 'registration/signup.html', {
        "form":form
    })

def profile(request):
    '''
    Function to return the profile page
    '''
    user = request.user
    all_images = []
    if request.method == "POST":
        form = ImageForm(request.POST)
        if form.is_valid():
            image = form.save(commit=False)
            image.save()
    else:
        form = ImageForm()

    try:
        images = Image.objects.all()
    except Image.DoesNotExist:
        images = None
    return render(request , 'profile.html' , { 'images': images, 'form': form })
