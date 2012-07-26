from django.db import models

# Create your models here.
class Rules(models.Model):
    antecedents = models.CharField(max_length=40)
    consequents = models.CharField(max_length=40)