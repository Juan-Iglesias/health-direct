from health_direct.InputSubmitBackend.models import Input
from health_direct.UserHandler.models import User_Input
from django.contrib.auth.models import User
import os
from django.shortcuts import render_to_response
from django.utils import importlib
from django.contrib.auth import *
from django.views.generic.base import TemplateView

def make_dict(qset):
    rlist = []
    for q in qset:
        #@todo: place error handling here, what if appName of inputId is not found
        rlist.append({ 'appName': q.input.appName, 'CheckupId':int(q.input.inputId) })
    return rlist

#def queuer(httprequest, checkupSet=None):
def queuer(checkupSet=None):
    'Returns a iterator of the relevant questions, given a user'
    if checkupSet is None:
        #@todo: Replace this with a checkup populating function
        u = User.objects.get(pk=2)
        # select_related allows us to follow foreign key relationships
        checkupSet = User_Input.objects.filter(user = u, input__isCheckup = True).select_related()
        inputDict = make_dict(checkupSet)
    return inputDict.__iter__()

# This variable is global so its state can be stored with every iteration
class CheckupIterator(TemplateView):
    template_name='testinter.html'
    
    def __init__(self):
        self.iterator = queuer()
        self.current = self.iterator.next()
        
    def ret_current(self):
        return self.current
    
    def ret_next(self):
        self.current = self.iterator.next()
        return self.current
    
    def get_checkup(self, httprequest): 
    #def get_checkup(self):
        try:
            currentInput = self.ret_next()
            try:
                appModule = importlib.import_module('health_direct.'+ currentInput['appName'] + '.views')
            except ImportError:
                raise ImportError('Import Failed')
            dcontext = appModule.display(currentInput['CheckupId'])
            currentInput.update(dcontext)
        except StopIteration:
            currentInput = {'no_checkups': True}
        # Right now this function just returns a dictionary that will be made into a context
        return self.render_to_response(currentInput)
        #return currentInput
    # Runs app within checkupiterator window.
    
    # When the app completes running it sends the result to User_Entries table
    


    # return {'appName': current.input.appName, 'CheckupId': current.input.pk}
    # if (request.session['member_id']) if it exists
    #     User_Input.objects.get(user=request.session['member_id'])
    #     select the most appropriate input (this will return an input primary key)
    #     of the most appropriate input, grab its app
    #     Input.objects.get(pk=selectedcheckup).answerapp
    # else
    #    display a different page, redirect to the register or login page
    