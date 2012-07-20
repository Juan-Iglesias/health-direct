from django.db import models

# Create your models here.
class Rules(models.Model):
    antecedents = models.CharField()
    consequents = models.CharField()