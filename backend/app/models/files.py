from django.db import models

def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)

class Files(models.Model):
    upload_to = models.FileField(upload_to=user_directory_path)
    secure = models.BooleanField(default=False)
    lgpd = models.BooleanField(default=False)
