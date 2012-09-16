# Create your views here.
from health_direct.AssociationRules.views import Itemset
from health_direct.Tagger.models import *
import itertools
import copy

def get_itemsets(relationship_type, min_coverage, include_single_itemsets=False):
    'Finds all itemsets whose coverage is equal to or above the min_coverage'
    
    r_qset = relationship_type.objects.all()
    
    taggables = []
    for rec in r_qset:
        if not rec.taggable in taggables:
            taggables.append(rec.taggable)
            
    taggables_length = len(taggables)
    
    itemset_hash = {}
    itemset_hash_keys = []
    for query in r_qset:
        # Find all unique tags
        tag = query.tag
        if not tag in itemset_hash_keys:
            # Determine if it has the minimum coverage or more
            coverage = Itemset([tag]).get_support(taggables, taggables_length, r_qset)
            if coverage >= min_coverage:
                #Add tag to the tag_hash
                itemset_hash[(tag,)] = coverage
                itemset_hash_keys = itemset_hash.keys()
    
    #Making the tuple objects in itemset_hash_keys readable for get_support
    itemset_key_vals = []
    for item_key in itemset_hash.keys():
        itemset_key_vals.append(item_key[0])
    
    #At this point itemset_hash is filled with all qualified one-itemsets

    multi_itemsets_hash = {}
    i = 2
    itemset_is_filled = True
    while i < len(itemset_hash_keys) and itemset_is_filled:
        newitemset_hash = {}
        newitemsets = itertools.combinations(itemset_key_vals, i)
        for newitemset in newitemsets:
            coverage = Itemset(list(newitemset)).get_support(taggables, taggables_length, r_qset)
            if coverage >= min_coverage:
                newitemset_hash[newitemset] = coverage
                      
        if len(newitemset_hash) == 0:
            itemset_is_filled = False
                    
        i += 1
        multi_itemsets_hash.update(newitemset_hash)
         
    if not include_single_itemsets:
        return multi_itemsets_hash
        
    multi_itemsets_hash.update(itemset_hash)
    return multi_itemsets_hash

        #Optimization tips:
        # Only look through tags which are known to be included in the relationship-type
        # Only check the coverage of tags which have been admitted to taglist


def get_rules(relationship_type, min_coverage, min_accuracy):
    'Finds all rules whose coverage and accuracy is equal to or above the min_coverage and min_accuracy'
    
    #We give get_itemsets a True to avoid calculating the coverage of one itemsets again
    itemset_hash = get_itemsets(relationship_type, min_coverage, True)
    
    #This statement creates an itemset hash with multiple items only
    multi_itemset_hash = copy.copy(itemset_hash)
    for itemset_key in multi_itemset_hash.keys():
        if len(itemset_key) < 2:
            del multi_itemset_hash[itemset_key] 
            
    #Generate single-consequent rules
    one_con_rule_hash = {}
    for itemset in multi_itemset_hash:
        numerator = multi_itemset_hash[itemset]
        for item in itemset:
            # denominator is the coverage of the itemset without item, otherwise known as the coverage of the antecedent
            itemset_list = list(itemset)
            item_index = itemset_list.index(item)
            itemset_list.pop(item_index)
            antecedent = tuple(itemset_list)
            denominator = itemset_hash[antecedent]
            try:
                accuracy = numerator / denominator
            except ZeroDivisionError:
                accuracy = 0
            if accuracy >= min_accuracy:
                one_con_rule_hash[(antecedent, (item,))] = (numerator, accuracy)
                
    #one_con_rule_hash now contains all valid single consequent rules
    # Now to generate double consequent rules

    new_con_list = []
    newrules = itertools.combinations(one_con_rule_hash, 2)

    for rule in newrules:
        # Pick rules with common antecedents
        rule1 = rule[0]
        rule2 = rule[1]
        antecedent1 = rule1[0]
        antecedent2 = rule2[0]
        
        
        #Combine consequents
        new_consequent = []
        for tag in rule1[1]:
            new_consequent.append(tag)
        for tag in rule2[1]:
            new_consequent.append(tag)
            
        #Make new antecedent
        new_antecedent = []
        for tag in antecedent1:
            if tag in antecedent2:
                new_antecedent.append(tag)
            else:
                new_consequent.append(tag)

        if new_antecedent != []:
            diff_consequents = set(antecedent2).difference(new_antecedent)
            for consequent in diff_consequents:
                new_consequent.append(consequent)
    
            new_rule = (tuple(set(new_antecedent)), tuple(set(new_consequent)))
            new_con_list.append(new_rule)
                    
            #print('Original: ', rule)
            #print('New: ', new_rule)
    
    new_con_set = set(new_con_list)  

    rule_hash = {}
    for new_rule in new_con_set:
        # combine consequent and antecedent to form itemset
        itemset = []
        antecedent = new_rule[0]
        consequent = new_rule[1]
        for tag in antecedent:
            itemset.append(tag)
        for tag in consequent:
            itemset.append(tag)
            
        itemset = tuple(itemset)
            
        try:
            numerator = multi_itemset_hash[itemset]
            denominator = itemset_hash[antecedent]
            try:
                accuracy = numerator / denominator
            except ZeroDivisionError:
                accuracy = 0
                
            if accuracy >= min_accuracy:
                rule_hash[new_rule] = (numerator, accuracy)
        except KeyError:
            pass
    
    rule_hash.update(one_con_rule_hash)
    
    return rule_hash

        
    # Look for commonalities in the antecedents. 
    # For all rules with common antecedents, combine antecedents and remove distinguishing tags
    # Place distinguishing tags into the consequent
     
'''
def tag_combinations():
    ret_list = []
    tags = Tags.objects.all()
    for i in range(1, len(tags)):
        ret_list.append(itertools.combinations(tags, i))
    result = reduce(lambda x,y: itertools.chain(x,y), ret_list)
    ret_list = []
    done = False
    while not done:
        try:
            next = result.next()
            ret_list.append(next)
        except:
            done = True
    return ret_list
            

def find_rules(min_support, min_confidence, relationship_type):
    tag_combos = tag_combinations()
    possible_rule_list = []
    rule_combos = itertools.product(tag_combos, tag_combos)
    #Now remove rules where the consequent contains the antecedent
    
    done = False
    while not done:
        try:
            rule = rule_combos.next()
            invalid = False
            for tag in rule[0]:
                #If the tag is in the consequent this is a bunk rule
                if tag in rule[1]:
                    invalid = True
            if not invalid:
                possible_rule_list.append(rule)
                print(rule)
        except StopIteration:
            done = True
    
    #At this point we now have a list of almost every conceivable rule
    rule_list = []
    str = 'Rules above min_support %s and min_confidence %s:' % (min_support, min_confidence)
    print(str)
    for rule in possible_rule_list:
        arule = Association_Rule(rule[0], rule[1], relationship_type)
        stats = arule.associate()
        if stats[0] >= min_support and stats[1] >= min_confidence:
            rule_list.append(arule)
            print rule, stats[0], stats[1]
    return rule_list
'''

    


