from django.db import models

# Create your models here.
class Questions(models.Model):
    questiontext = models.CharField(max_length=120)
    
#This next model should have automated creation.
#One of these tables should be created with each entry in the "Questions" table.
#The naming convention is as follows: 'TheQuestionEntryID'_Responses'
class QuestionID_Responses(models.Model):
    response = models.CharField(max_lenght=50)
    