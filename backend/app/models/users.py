from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields.related import RelatedField


class User(AbstractUser):
    name = models.CharField(max_length=100, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.Choices()
    crea = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)
    passport_due = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=False, null=False, unique=True)
    rg = models.CharField(max_length=20, null=False, blank=False, unique=True)
    visa = RelatedField(null=True, blank=True)
    address = RelatedField(null=True, blank=True)

    def user_directory_path(self, filename):
        return "user_{0}/{1}".format(self.pk, filename)

    def __str__(self):
        return self.name
