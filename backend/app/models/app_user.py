from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    name = models.CharField(max_length=100, blank=True)
    dob = models.DateField(null=True, blank=True)
    crea = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)
    passport_due = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=False, null=False, unique=True)
    rg = models.CharField(max_length=20, null=False, blank=False, unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='appuser_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='appuser_permissions',  # Add this to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def user_directory_path(self, filename):
        return "user_{0}/{1}".format(self.pk, filename)

    def __str__(self):
        return self.name
