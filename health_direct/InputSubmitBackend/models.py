from django.db import models

# Create your models here.
class Input(models.Model):
    name = models.CharField()
    isCheckup = models.BooleanField()
    tags = models.ManyToManyField('Tagger.Tags')
    app = models.CharField()
    class Answers(models.Model):
        responses = models.CharField(max_length=60)
