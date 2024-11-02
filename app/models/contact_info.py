from django.db import models
from django.conf import settings


class ContactInfo(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contact_info"
    )
    phone = models.CharField(max_length=13, blank=True, null=True)
    phone_alt = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return f"{self.user.name}'s contact info"
