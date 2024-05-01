from django.urls import path

from . import views
from .views import home

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('talks/', views.talk_list, name='talk_list'),
    path('users/', views.user_list, name='user_list'),
    path('addRoom/', views.add_room, name='add_room'),
]