from health_direct.InputSubmitBackend.models import Input
from health_direct.UserHandler.models import User_Input
import os
from django.shortcuts import render_to_response
from django.utils import importlib

def get_checkup(httprequest):
    
    nextInput = queuer(httprequest)
    render_to_response('tagtester.html',{'appName': nextInput['appName']})
    try:
        appModule = importlib.import_module('health_direct.'+ nextInput['appName'] + '.views')
    except ImportError, e:
        raise e
    appModule.display(nextInput['checkupId'])
    
    
    # calls program at location with the id of the particular checkup as the argument
    # Runs app within checkupiterator window.
    
    # When the app completes running it sends the result to User_Entries table
    
def queuer(httprequest, checkupSet=None):
    if checkupSet is None:
        #@todo: Replace this with a checkup populating function
        checkupSet = User_Input.objects.filter(user = httprequest.user, isCheckup = True).iterator()
    return checkupSet.next().value('appName','inputId')
    
    # if (request.session['member_id']) if it exists
    #     User_Input.objects.get(user=request.session['member_id'])
    #     select the most appropriate input (this will return an input primary key)
    #     of the most appropriate input, grab its app
    #     Input.objects.get(pk=selectedcheckup).answerapp
    # else
    #    display a different page, redirect to the register or login page
    