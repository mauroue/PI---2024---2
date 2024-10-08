from django.db import models
from django.conf import settings


class Documents(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    crea = models.ForeignKey(
        "Files", on_delete=models.SET_NULL, null=True, related_name="crea_document"
    )
    passport = models.ForeignKey(
        "Files", on_delete=models.SET_NULL, null=True, related_name="passport_document"
    )
    cpf = models.ForeignKey(
        "Files", on_delete=models.SET_NULL, null=True, related_name="cpf_document"
    )
    rg = models.ForeignKey(
        "Files", on_delete=models.SET_NULL, null=True, related_name="rg_document"
    )
