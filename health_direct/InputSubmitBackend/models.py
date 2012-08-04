from django.db import models

# Create your models here.
class Apps(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)

class Input(models.Model):
    name = models.CharField(max_length=30)
    app_input_code = models.CharField(max_length=70)
    isCheckup = models.BooleanField()
    tags = models.ManyToManyField('Tagger.Tags')
    #The app described in the next field will handle the type of input in the record.
    app = models.ForeignKey(Apps)
