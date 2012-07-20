from django.db import models

# Create your models here.
class Tags(models.Model):
    name = models.CharField()

class TagRelations(models.Model):
    inputfk = models.ForeignKey('health_direct.InputSubmitBackend.Input')
    userfk = models.ForeignKey('health_direct.Users.Users')
    tagfk = models.ForeignKey(Tags)
    magnitude = models.FloatField()
    
#class User_Tags(models.Model):
#    userfk = models.ForeignKey()
#    tagfk = models.ForeignKey()