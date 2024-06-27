from django.urls import path

from . import views
from room.views import enter_room,create_room,search_rooms

urlpatterns = [
    path('', views.join_room, name='rooms'),
    path('enter_room/',enter_room, name='enter_room'),
    path('create_room/',create_room, name='create_room'),
    path('search_rooms/', search_rooms, name='search_rooms'),
    path('open_rooms/',views.open_rooms,name = 'open_rooms'),
    path('create_open_room/',views.create_open_room, name='create_open_room'),
    path('enter_open_room/', views.enter_open_room, name='enter_open_room'),
    path('my_rooms/', views.my_rooms, name='my_rooms'),
    path('invite_users/', views.invite_users, name='invite_users'),
    path('manage_join_requests/',views.manage_join_requests,name='manage_join_requests'),
]
