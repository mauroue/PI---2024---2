
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import RelatedField

from django.conf import settings

class Address(models.Model):
    address = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=7, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    state = models.CharField(max_length=2, null=False, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='addresses')
