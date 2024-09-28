from django.conf import settings
from django.db import models


class ContactInfo(models.Model):
    phone = models.CharField(max_length=13)
    phone_alt = models.CharField(max_length=13)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
