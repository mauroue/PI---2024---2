from django.db import models

from app.models.user import AppUser


class Visa(models.Model):
    due_date = models.DateField()
    country = models.CharField(max_length=2)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
