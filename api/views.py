from MySQLdb import Timestamp
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from rest_framework import generics

from .models import Room
from .serializers import RoomSerializer


def main(request):
    return HttpResponse(datetime.datetime.now().timestamp())


class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
