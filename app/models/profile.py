from django.conf import settings
from django.db import models


class Profile(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="new")

    def __str__(self):
        return f"{self.user.username} Profile"
