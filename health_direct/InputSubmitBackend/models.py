from django.db import models

# Create your models here.
class Input(models.Model):
    name = models.CharField()
    isCheckup = models.BooleanField()
    tags = models.ManyToManyField('Tagger.Tags')
    #The app described in the next field will handle the type of input in the record.
    app = models.CharField()
