from health_direct.Tagger.models import UserTagRelations, Tags

class Itemset():
    'Represents a set of items being considered as grounds for a potential rule'
    def __init__(self, itemset):
        self.itemset = itemset
        
    def get_support(self, taggables, itemsetsize, qset):
        'Calculates the support of an itemset, the support is returned as a ratio'
        support = 0
        for taggable in taggables:
            encountered_all = True
            for item in self.itemset:
                if not qset.filter(taggable=taggable, tag=item):
                    encountered_all = False
                    break
            if encountered_all:
                support += 1.0
                
        return support / itemsetsize
