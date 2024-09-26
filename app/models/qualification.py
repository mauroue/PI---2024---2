from django.db import models


class Qualification(models.Model):
    name = models.CharField(max_length=100)
    type = models.Choices()
    conclusion_date = models.DateField()
    due_date = models.DateField()
    organization = models.CharField(max_length=100)
    user = models.ForeignField("User", on_delete=models.CASCADE)
