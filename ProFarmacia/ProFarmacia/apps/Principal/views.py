from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
# Create your views here.
def Principal(request):
	return render_to_response('index.html',{},context_instance=RequestContext(request))
