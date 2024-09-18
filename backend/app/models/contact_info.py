from django.contrib.auth.models import User
from django.db import models


class ContactInfo(models.Model):
    phone = models.CharField(max_length=13)
    phone_alt = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
