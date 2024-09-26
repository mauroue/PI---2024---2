from django.conf import settings
from django.db import models


class Visa(models.Model):
    due_date = models.DateField()
    country = models.CharField(max_length=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='visas')
