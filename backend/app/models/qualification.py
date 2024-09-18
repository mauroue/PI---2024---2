from django.db import models
from django.db.models.fields.related import RelatedField

from app.models.user import AppUser


class Qualification(models.Model):
    name = models.CharField(max_length=100)
    type = models.Choices()
    conclusion_date = models.DateField()
    due_date = models.DateField()
    organization = models.CharField(max_length=100)
    user = RelatedField(AppUser, on_delete=models.CASCADE)
