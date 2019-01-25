from django.urls import path
from django.conf.urls import url
from .views import Homepageview,Game
from pages import views




urlpatterns=[
path('',Homepageview.as_view(),name='home'),
path('dhishnya/start/',Game.as_view(),name='beg_dhi'),
#path('dhishnya/start/',views.game,name='beg_dhi'),
# url(r'^authenticate/$', views.ver, name='homePage'),

path('dhishnya/authenticate/',views.ver),

]