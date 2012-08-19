from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from forms import QuestionForm
from django.core.context_processors import csrf
from django.contrib import auth



def home(request):
	return render_to_response('testinter.html')

def my_login(request):
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(user)
			return HttpResponseRedirect('/home/',)
		else:
			return render_to_response('login.html', {'invalid': True}, context_instance=RequestContext(request))
	else:
		return render_to_response('login.html', context_instance=RequestContext(request))

def inputsearch(request):
	if 'q' in request.GET:
		q = request.GET['q']
		if q:
			message1 = 'You searched for: %r' % q 
			return render_to_response('testselect.html', { 'message': message1 })
		else:
			return render_to_response('testselect.html',)
	else:
		return render_to_response('testselect.html',) 

def build(request):
	print('called')
	if request.method == 'POST':
		r = { 'post' : 'Posted'}
	elif request.method == 'GET':
		r = {'post' : 'Get'}
	else:
		r = {}
	return render_to_response('testgenerator.html', r, context_instance=RequestContext(request))

def success(request):
	return render_to_response('testgenerator.html', {'post': 'success'})

def questionbuilder(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			#Add tag section to form.
			#The tag section will be parsed, and the question will be tagged with the tags recognized.
			#Any unrecognized tags will be created and put into the tag table. Then the question will 
			#tagged with these.
			return HttpResponseRedirect('/questionbuilder/successful/')
	else:
		form = QuestionForm()
	return render_to_response('testgenerator.html', { 'form': form }, context_instance=RequestContext(request))

def questionbuilt(request):
	return render_to_response('questionbuilt.html')
	