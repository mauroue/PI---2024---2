from app.models.address import Address
from app.models.visa import Visa
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=100, blank=True)
    dob = models.DateField(null=True, blank=True)
    crea = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)
    passport_due = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=False, null=False, unique=True)
    rg = models.CharField(max_length=20, null=False, blank=False)
    visa = models.ForeignKey('Visa', on_delete=models.SET_NULL, null=True, related_name='users')
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, related_name='users')

    USERNAME_FIELD = "cpf"
    REQUIRED_FIELDS = ["username"]

    def user_directory_path(self, filename):
        return f"user_{self.pk}/{filename}"

    def __str__(self):
        return self.name or self.username
