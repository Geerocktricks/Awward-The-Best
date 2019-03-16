from django.shortcuts import render

# Create your views here.

def welcome(request):
    '''
    Function to display the index page
    '''
    return render('index.html')