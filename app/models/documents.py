from django.db import models
from django.conf import settings
from app.models.files import Files


class Documents(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    crea = models.ForeignKey(
        Files, on_delete=models.SET_NULL, null=True, related_name="crea_document"
    )
    crea_number = models.CharField(max_length=20, blank=True, null=True)

    passport = models.ForeignKey(
        Files, on_delete=models.SET_NULL, null=True, related_name="passport_document"
    )
    passport_number = models.CharField(max_length=20, blank=True, null=True)

    cpf = models.ForeignKey(
        Files, on_delete=models.SET_NULL, null=True, related_name="cpf_document"
    )
    cpf_number = models.CharField(max_length=11, blank=True, null=True)

    rg = models.ForeignKey(
        Files, on_delete=models.SET_NULL, null=True, related_name="rg_document"
    )
    rg_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Documents for {self.user.username}"
