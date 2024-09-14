from django.db import models
from django.db.models.fields.related import RelatedField

class documentos(models.Model):
    crea = RelatedField()



