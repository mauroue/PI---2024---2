
from django.contrib.auth.models import User
from django.db import models

class Address(models.Model):
    address = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=7, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    state = models.CharField(max_length=2, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
