from django.db import models

# Create your models here.
class Rules(models.Model):
    relationship_type = models.CharField(max_length=100)
    antecedents = models.CharField(max_length=200)
    consequents = models.CharField(max_length=200)
    coverage = models.FloatField()
    accuracy = models.FloatField()
    
    def __unicode__(self):
        return u'type: %s, %s => %s, cov=%s, acc=%s' % (self.relationship_type, self.antecedents, self.consequents, self.coverage, self.accuracy)