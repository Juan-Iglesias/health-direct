from django.db import models

# Create your models here.

#This table will soon be distinguished per individual user.
#Each user will have their own User_Entries table.
class User_Entries(models.Model):
    user = models.ForeignKey('Users.user')
    input = models.ForeignKey('InputSubmitBackend.Input')
    result = models.CharField(maxlength=60)
    timestamp = models.DateTimeField()
    
class User_Tags(models.Model):
    user = models.ForeignKey('User.user')
    tagrelation = models.ForeignKey('Tagger.TagRelations')
        
class User_Input(models.Model):
    user = models.ForeignKey('User.user')
    input = models.ForeignKey('InputSubmitBackend.Input')