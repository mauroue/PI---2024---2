from django.db import models
from django.db.models.fields.related import RelatedField

from backend.cadastro.models.files import Files


class Documents(models.Model):
    crea = RelatedField(files, on_delete=models.SET_NULL)
    passport = RelatedField(Files, on_delete=models.SET_NULL)
    cpf = RelatedField(Files, on_delete=models.SET_NULL)
    rg = RelatedField(Files, on_delete=models.SET_NULL)

