from django.db import models

# Create your models here.
class Input(models.Model):
    name = models.CharField()
    isCheckup = models.BooleanField()
    app = models.CharField()