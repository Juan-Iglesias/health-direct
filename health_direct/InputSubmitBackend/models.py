from django.db import models

# Create your models here.
class Input(models.Model):
    name = models.CharField(max_length=30)
    isCheckup = models.BooleanField()
    tags = models.ManyToManyField('Tagger.Tags')
    #The app described in the next field will handle the type of input in the record.
    app = models.CharField(max_length=30)
