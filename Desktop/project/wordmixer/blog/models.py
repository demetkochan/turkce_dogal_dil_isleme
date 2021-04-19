
from djongo import models
from django.contrib.auth.models import User

class FileUpload(models.Model):
    file = models.FileField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)