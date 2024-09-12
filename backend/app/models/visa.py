from django.db import models
from django.db.models.fields.related import RelatedField

from backend.cadastro.models.users import User


class Visa(models.Model):
    due_date = models.DateField()
    country = models.CharField(max_length=2)
    user = RelatedField(User, on_delete=models.CASCADE)
