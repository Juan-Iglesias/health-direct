from django.db import models

# Create your models here.
class User_Entries(models.Model):
    input = models.ForeignKey('InputSubmitBackend.Input')
    result = models.CharField(maxlength=60)
    timestamp = models.DateTimeField()
    
    class Meta:
        abstract = True
    
class User_Tags(models.Model):
    tagrelation = models.ForeignKey('Tagger.TagRelations')

    class Meta:
        abstract = True
        
class User_Input(models.Model):
    input = models.ForeignKey('InputSubmitBackend.Input')
    isCheckup = models.BooleanField()
    
    class Meta:
        abstract = True