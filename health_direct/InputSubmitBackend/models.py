from django.db import models

# Create your models here.
class Input(models.Model):
    inputId = models.CharField(max_length=70)
    isCheckup = models.BooleanField()
    #The app described in the next field will handle the type of input in the record.
    appName = models.CharField(max_length = 50)

    def __unicode__(self):
        return u'%s %s' % (self.appName, self.inputId)