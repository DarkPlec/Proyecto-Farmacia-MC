from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.template import RequestContext
from formularios import *
from ProFarmacia.apps.regfarmacia import models
from ProFarmacia.apps.regfarmacia.models import Farmacias,Inventarios
from ProFarmacia.apps.Principal.views import Principal
from django.db.models import Q
import datetime
#from django.contrib.auth import logout
#from django.contrib.sessions.models import Session
#from django.core.mail import EmailMultiAlternatives
#import os
#import StringIO
#from xhtml2pdf import pisa
#from django.template.loader import render_to_string
# Create your views here.
def Buscar_Global(request):
    if request.method=="POST":
        formBG=B_Global(request.POST)
        if formBG.is_valid():
          medicamento=formBG.cleaned_data['N_Medicamento']
          if medicamento == "":
            return False
          #med=Inventarios.objects.filter(Name_med=medicamento)
          med=Inventarios.objects.filter(Q(Name_med=medicamento)).exclude(Cantidad=0)
          #for v in med:
           # if v.Cantidad==0:
            #  c=0
              #m=Inventarios.objects.filter(nombre__like="%medicamento%").filter(cantidad>0)
             # M=Inventarios.objects.filter(Q(Name_med=medicamento)).exclude(Cantidad=0)
              #l_md=Inventarios.objects.filter(Q(Name_med=medicamento) & Q(Cantidad>c))
              #return HttpResponse(len(M))
          if len(med)==0:
        		Error="El Medicamento No Exite "
        		return render_to_response("Busqueda/Buq_Global.html",{'formBG':formBG,'Error':Error},context_instance=RequestContext(request))
          vector=[]
          F=[]
          U=[]
          for i in med:
            vector.append(i.ID_Usuario)
          for u in vector:
            usuario=u
            far=Farmacias.objects.filter(ID_Usuario=u)
            for h in far:
              F.append(h.Name_Farmacia)
              U.append(h.Ubicacion)

       		#return HttpResponse(F)
          return render_to_response("Busqueda/Buq_Global.html",{'formBG':formBG,'med':med,'F':F,'U':U},context_instance=RequestContext(request))
    else:
        formBG=B_Global()
    return render_to_response("Busqueda/Buq_Global.html",{'formBG':formBG},context_instance=RequestContext(request))


def Buscar_Mcercano(request):
    if request.method=="POST":
        formBG=B_Global(request.POST)
        if formBG.is_valid():
          medicamento=formBG.cleaned_data['N_Medicamento']
          med=Inventarios.objects.filter(Q(Name_med=medicamento)).exclude(Cantidad=0)
          
          if len(med)==0:
            Error="El Medicamento No Exite "
            return render_to_response("Busqueda/Buq_Med_Cercano.html",{'formBG':formBG,'Error':Error,},context_instance=RequestContext(request))
          vector=[]
          F=[]
          U=[]
          for i in med:
            vector.append(i.ID_Usuario)
          for u in vector:
            usuario=u
            far=Farmacias.objects.filter(ID_Usuario=u)
            for h in far:
              F.append(h.Name_Farmacia)
              U.append(h.Ubicacion)

        
          return render_to_response("Busqueda/Buq_Med_Cercano.html",{'formBG':formBG,'med':med,'F':F,'U':U},context_instance=RequestContext(request))
    else:
        formBG=B_Global()
    return render_to_response("Busqueda/Buq_Med_Cercano.html",{'formBG':formBG},context_instance=RequestContext(request))

def MostrarFyM(request):
  if request.method=="POST":
    formBF=BFarmacia(request.POST)
    if formBF.is_valid():
      farmacia=formBF.cleaned_data['N_Farmacia']
      far=Farmacias.objects.filter(Name_Farmacia=farmacia)

      if len(far)==0:
        Error="La Farmacia buscada aun no se encuentra Registrada"
        return render_to_response("Busqueda/FarmaciasGen.html",{'formBF':formBF,'Error':Error,},context_instance=RequestContext(request))
      for i in far:
        usuario= i.ID_Usuario
        Med = Inventarios.objects.filter(ID_Usuario=usuario)
        if len(Med) == 0:
          Error2="La farmacia No Cuenta con Stock en este Momento"
          return render_to_response("Busqueda/FarmaciasGen.html",{'formBF':formBF,'Error2':Error2,},context_instance=RequestContext(request))
      return render_to_response("Busqueda/FarmaciasGen.html",{'formBF':formBF,'Farmacias':far,'Medicamentos':Med},context_instance=RequestContext(request))
  
  else:
    formBF=BFarmacia()
  return render_to_response("Busqueda/FarmaciasGen.html",{'formBF':formBF},context_instance=RequestContext(request))