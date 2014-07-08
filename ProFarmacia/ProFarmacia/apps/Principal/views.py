from django.shortcuts import render, render_to_response
from ProFarmacia.apps.regfarmacia.models import ContadorBusq
from django.template import RequestContext
from django.http import HttpResponse
# Create your views here.
def Principal(request):
	MmB = ContadorBusq.objects.all().order_by('-Contador')[:9]
	return render_to_response('index.html',{'Medicamentos':MmB},context_instance=RequestContext(request))

