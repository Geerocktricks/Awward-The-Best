from django.test import TestCase
from .models import User, Profile , Image
from django.contrib.auth.models import User

# Create your tests here.
class UserTestClass(TestCase):
    '''
    Funtion to test all user functionalities
    '''
    def setUp(self):
        self.