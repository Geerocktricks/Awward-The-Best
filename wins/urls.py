from django.conf.urls import url,include
from . import views


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('signup/' , views.signup , name = 'signup'),
    url('accounts/' , include('django.contrib.auth.urls')),
    ]