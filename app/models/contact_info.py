from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import RelatedField



class ContactInfo(models.Model):
    phone = models.CharField(max_length=13)
    phone_alt = models.CharField(max_length=13)
    user = RelatedField(User, on_delete=models.CASCADE)
