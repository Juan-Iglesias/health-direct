from health_direct.Tagger.models import *

class Rule():
    def __init__(self, antecedent, consequent, tag_type):
        self.antecedent = antecedent
        self.consequent = consequent
        self.tag_type = tag_type
        self.confidence = 'Has not been set'
        
    def get_confidence(self):
        # calculate confidence
        return ''
        
class Association_Rule(Rule):
    #@todo: Change this function to accept Tag objects, not strings
    'Describes an association rule.'
    def get_support(self, itemset=None):
        'Returns the support of an itemset, or by default, self.antecedent'
        #Allows for more convenient get_support calling
        if itemset == None:
            itemset = self.antecedent
            
        #Prepares future calling to be more flexible, by determining the attribute
        if self.tag_type == UserTagRelations:
            t_attr = 'user'
        else:
            t_attr = 'input'
            
        #Grabbing all users or inputs with tags
        taggables = []
        all_records = self.tag_type.objects.all()
        for record in all_records:
            taggable = eval('record.' + t_attr)
            if not taggable in taggables:
                taggables.append(taggable)
        denominator = len(taggables)
        
        #Counting the number of times both items occur together
        numerator = 0
        for taggable in taggables:
            encountered_all = True
            for item in itemset:
                    
                # Makes sure each item is a valid tag
                #try:
                Tags.objects.get(name=item)
                #except:
                #   raise TagDoesNotExist('tag: ' + item + ' does not exist')
                    
                # Counts taggables that contain the itemset
                if t_attr == 'user':
                    if not UserTagRelations.objects.filter(user=taggable, tag=item):
                        encountered_all = False
                else:
                    if not self.tag_type.objects.filter(input=taggable, tag=item):
                        encountered_all = False
            if encountered_all:
                numerator += 1.0
            
            # calculate support
        return numerator / denominator
        
    def get_confidence_once(self):
        'Calculates the confidence of self, let associate call this function!'
        numerator = self.get_support(self.antecedent + self.consequent)
        denominator = self.get_support(self.antecedent)
        try:
            return numerator / denominator
        except ZeroDivisionError:
        # In this case, the antecedent never occurs in the db!
            return 0
        
            
    def associate(self):
        'Calculates and sets the confidence of self'
        if self.confidence == 'Has not been set':
            self.confidence = self.get_confidence_once()
        return self.confidence
    
    def get_confidence(self):
        'Returns the confidence of self'
        return self.confidence
    
    

class TagDoesNotExist(Exception):
    'Exception that indicates the absence of a dependent tag'
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return str(self.msg)
    
#def associate(assoc_rule):
    #if rule does not yet exist in the db:
        #place rule in db