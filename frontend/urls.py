from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='home'),
    path('join', views.index),
    path('create', views.index)

]
