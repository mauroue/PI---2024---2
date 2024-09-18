from django.db import models

from app.models.files import Files


class Documents(models.Model):
    crea = models.ForeignKey(Files, on_delete=models.SET_NULL)
    passport = models.ForeignKey(Files, on_delete=models.SET_NULL)
    cpf = models.ForeignKey(Files, on_delete=models.SET_NULL)
    rg = models.ForeignKey(Files, on_delete=models.SET_NULL)

