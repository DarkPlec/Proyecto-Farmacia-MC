from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.core.context_processors import csrf
from django.template import RequestContext
from formularios import *
from models import *
# Create your views here.

def registroFar(request):
	if request.method == 'POST':
		form1=Fregistro(request.POST)
		if form1.is_valid():
			usuario=form1.cleaned_data['usuario']
			verificar=Farmacias.objects.all()
			for i in verificar:
				if usuario == i.ID_Usuario:
					error1="Usuario registrado por favor intente otro"
					return render_to_response("Registros/regFarmacia.html",{'formRF':form1,'Error1':error1},context_instance=RequestContext(request))
				else:
					#usuario=form1.cleaned_data['usuario']
					farmacia=form1.cleaned_data['farmacia']
					ubicacion=form1.cleaned_data['ubicacion']
					email=form1.cleaned_data['email']
					password=form1.cleaned_data['password1']
					InsertarF=Farmacias(ID_Usuario=usuario,Name_Farmacia=farmacia,Ubicacion=ubicacion,Email=email,Password=password)
					InsertarF.save()
					exito="Farmacia Registrada con exito"
					return render_to_response("Registros/regFarmacia.html",{'formRF':form1,'Exito':exito},context_instance=RequestContext(request))
	else:
		form1 = Fregistro()
	return render_to_response("Registros/regFarmacia.html",{'formRF':form1},context_instance=RequestContext(request))


