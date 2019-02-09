from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class User1(User):
    contact_Number_1 = models.CharField(max_length=10, default='')

        

