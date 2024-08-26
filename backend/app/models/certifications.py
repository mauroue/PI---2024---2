from django.db import models
from django.db.models.fields.related import RelatedField

from backend.cadastro.models.users import User


class Certification(models.Model):
    name = models.CharField(max_length=100)
    type = models.Choices()
    conclusion_date = models.DateField()
    due_date = models.DateField()
    organization = models.CharField(max_length=100)
    user = RelatedField(User, on_delete=models.CASCADE)
