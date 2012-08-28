from django.db import models
from health_direct.Tagger.models import Tags

# Create your models here.
class Questions(models.Model):
    questiontext = models.TextField()
    
    def __unicode__(self):
        return self.questiontext

#This next model should have automated creation.
#One of these tables should be created with each entry in the "Questions" table.
#The naming convention is as follows: 'TheQuestionEntryID'_Responses'
class Question_Responses(models.Model):
    response = models.CharField(max_length=50)
    question = models.ForeignKey(Questions)
    
    def __unicode__(self):
        return u'%s %s' % (self.question, self.response)
    
    def disp(self):
        return self.response