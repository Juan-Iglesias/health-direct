from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=20)

class TagRelations(models.Model):
    inputfk = models.ForeignKey('InputSubmitBackend.Input')
    userfk = models.ForeignKey(User)
    tagfk = models.ForeignKey(Tags)
    magnitude = models.FloatField()
    
#class User_Tags(models.Model):
#    userfk = models.ForeignKey()
#    tagfk = models.ForeignKey()