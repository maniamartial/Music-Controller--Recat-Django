from importlib.resources import path
from django.urls import path
from .import views
urlpatterns = [
    path('', views.RoomView.as_view(), name='room'),
    path('createroom', views.CreateRoomSerializer.as_view(), name='createroom')
]
