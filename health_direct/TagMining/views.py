# Create your views here.
from health_direct.AssociationRules.views import Association_Rule
from health_direct.Tagger.models import *
import itertools

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
            

def find_rules(min_support, min_confidence, tag_type):
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
        arule = Association_Rule(rule[0], rule[1], tag_type)
        stats = arule.associate()
        if stats[0] >= min_support and stats[1] >= min_confidence:
            rule_list.append(arule)
            print rule, stats[0], stats[1]
    return rule_list

    


