from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def welcome(request):
    '''
    Function to display the index page
    '''
    return render(request ,'index.html')

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