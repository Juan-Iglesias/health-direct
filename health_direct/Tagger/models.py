from django.db import models
from django.contrib.auth.models import User
from health_direct.InputSubmitBackend.models import Input, Response

# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name

class UserTagRelations(models.Model):
    user = models.ForeignKey(User)
    tag = models.ForeignKey(Tags)
    magnitude = models.FloatField()
    
    def __unicode__(self):
        return u'%s %s' % (self.user, self.tag)
    
class InputTagRelations(models.Model):
    input = models.ForeignKey(Input)
    tag = models.ForeignKey(Tags)
    magnitude = models.FloatField()
    
    def __unicode__(self):
        return u'%s %s' % (self.input, self.tag)
  

class ResponseTagRelations(models.Model):
    response = models.ForeignKey(Response)
    tag = models.ForeignKey(Tags)
    magnitude = models.FloatField()
    
    def __unicode__(self):
        return u'%s %s' % (self.response, self.tag)
