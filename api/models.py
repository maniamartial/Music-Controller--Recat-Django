from email.policy import default
from tokenize import String
from django.db import models
import random
import string


# Create your models here.
def generate_unique_code():
    length = 6
    while True:
        code = '  '.join(random.choices(string.ascii_uppercase, l=length))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code


class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=64, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
