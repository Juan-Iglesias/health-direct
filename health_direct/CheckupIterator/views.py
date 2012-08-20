from health_direct.UserHandler.models import User_Input
from django.contrib.auth.models import User
from django.utils import importlib
from django.views.generic.base import TemplateView
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def make_dict(qset):
    rlist = []
    for q in qset:
        #@todo: place error handling here, what if appName of inputId is not found
        rlist.append({ 'appName': q.input.appName, 'CheckupId':int(q.input.inputId) })
    return rlist

#def queuer(httprequest, checkupSet=None):
def queuer(request, checkupSet=None):
    'Returns a iterator of the relevant questions, given a user'
    #First, we grab the logged-in User: request.user
    #Then, make sure the user is authentic: request.user.is_authenitcated
    if checkupSet is None:
        #@todo: Replace this with a checkup populating function
        #u = User.objects.get(pk=1)
        if request.user.is_authenticated():
            u = request.user
        else:
            return HttpResponseRedirect('/login/', {'passed': True})
        # select_related allows us to follow foreign key relationships
        checkupSet = User_Input.objects.filter(user = u, input__isCheckup = True).select_related()
        inputDict = make_dict(checkupSet)
    return inputDict.__iter__()


#class CheckupIterator(TemplateView):
class CheckupIterator():
    #template_name='testinter.html'
    
    #def __init__(self):
    #    self.iterator = queuer()
    #    self.current = self.iterator.next()
    #    self.is_completed = False
    
    def __init__(self):
        self.iterator = None
        self.current = None
        self.is_completed = False  
            
    def ret_current(self):
        return self.current
    
    def ret_next(self):
        self.current = self.iterator.next()
        return self.current
    
    def create_iter(self, request):
        self.iterator = queuer(request)
        self.current = self.iterator.next()
    
    #def post(self, request):
    #    try:
    #        r = RequestContext(request, self.get_checkup(self.ret_current()))
    #    except StopIteration:
    #        r = RequestContext(request, {'no_checkups': True})
    #    return self.render_to_response(r)
    
    def get_checkup(self, request): 
    #def get_checkup(self):
        #Setting currentInput
        if self.iterator is None:
            self.create_iter(request)
        ret_checkup = {}
        if request.method == "POST":
            # Capture response selected
            
            # Store response in db
            try:
                currentInput = self.ret_next()
            except StopIteration:
                # set no_checkup to True and don't try to import
                self.is_completed = True
            #Consider issuing a HttpResponseRedirect here to avoid refreshing errors
            return HttpResponseRedirect('/home/')
        else:
            currentInput = self.ret_current()
            ret_checkup = self.importer(currentInput)
            # Right now this function just returns a dictionary that will be made into a context
        ret_checkup.update({'no_checkups': self.is_completed})
        return render_to_response('testinter.html', ret_checkup, context_instance=RequestContext(request))
            #return currentInput
            
    def importer(self, checkup_key):
        try:
            appModule = importlib.import_module('health_direct.'+ checkup_key['appName'] + '.views')
        except ImportError:
            raise ImportError('App Import Failed')
        dcontext = appModule.display(checkup_key['CheckupId'])
        checkup_key.update(dcontext)
        return checkup_key
    
    #def get_context_data(self):
    #    return self.get_checkup(self.ret_next())
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
    