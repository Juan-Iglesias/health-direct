from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#This table will soon be distinguished per individual user.
#Each user will have their own User_Entries table.
    
class User_Tags(models.Model):
    user = models.ForeignKey(User)
    tagrelation = models.ForeignKey('Tagger.TagRelations')
        
class User_Input(models.Model):
    user = models.ForeignKey(User)
    input = models.ForeignKey('InputSubmitBackend.Input')
    
    def __unicode__(self):
        return u'%s %s' % (self.user, self.input)