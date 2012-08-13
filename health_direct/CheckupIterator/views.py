from health_direct.InputSubmitBackend.models import Input
from health_direct.UserHandler.models import User_Input
from django.contrib.auth.models import User
import os
from django.shortcuts import render_to_response
from django.utils import importlib
from django.contrib.auth import *

#def get_checkup(httprequest):
def get_checkup(): 
    
    #nextInput = queuer(httprequest)
    nextInput = queuer()
    #render_to_response('tagtester.html',{'AppName': nextInput['appName']})
    try:
        appModule = importlib.import_module('health_direct.'+ nextInput['appName'] + '.views')
    except ImportError:
        raise ImportError('Import Failed')
    dcontext = appModule.display(nextInput['CheckupId'])
    nextInput.update(dcontext)
    return nextInput
    # calls program at location with the id of the particular checkup as the argument
    # Runs app within checkupiterator window.
    
    # When the app completes running it sends the result to User_Entries table
    
#def queuer(httprequest, checkupSet=None):
def queuer(checkupSet=None):
    if checkupSet is None:
        #@todo: Replace this with a checkup populating function
        u = User.objects.get(pk=2)
        checkupSet = User_Input.objects.filter(user = u, input__isCheckup = True).iterator()
        current = checkupSet.next()
    return {'appName': current.input.appName, 'CheckupId': current.input.pk}
    # if (request.session['member_id']) if it exists
    #     User_Input.objects.get(user=request.session['member_id'])
    #     select the most appropriate input (this will return an input primary key)
    #     of the most appropriate input, grab its app
    #     Input.objects.get(pk=selectedcheckup).answerapp
    # else
    #    display a different page, redirect to the register or login page
    