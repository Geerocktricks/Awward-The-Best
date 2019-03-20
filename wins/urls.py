from django.conf.urls import url,include
from . import views


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('signup/' , views.signup , name = 'signup'),
    url('accounts/' , include('django.contrib.auth.urls')),
    url(r'profile/' , views.profile , name='profile'),
    url(r"^profile/update/$", views.update_profile, name = "update_profile"),
    ]