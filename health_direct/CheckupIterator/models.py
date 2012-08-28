from django.db import models
from django.contrib.auth.models import User
from health_direct.InputSubmitBackend.models import Input, Response
class Entry(models.Model):
    user = models.ForeignKey(User)
    input = models.ForeignKey(Input)
    response = models.ForeignKey(Response)
    value = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    
# Create your models here.
