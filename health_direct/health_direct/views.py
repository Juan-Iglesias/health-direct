from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
	return render_to_response('testinter.html', {'question':"This emplacement worked! Congratz!"})

def testsearch(request):
	return render_to_response('testselect.html')

def testgenerate(request):
	return render_to_response('testgenerator.html')
