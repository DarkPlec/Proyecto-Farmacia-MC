from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.template import RequestContext
from formularios import *
from ProFarmacia.apps.regfarmacia import models
from ProFarmacia.apps.regfarmacia.models import Farmacias,Inventarios,ContadorBusq
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
def Buscar_Mcercano(request):
    if request.method=="POST":
        formBG=B_Global(request.POST)
        if formBG.is_valid():
          medicamento=formBG.cleaned_data['N_Medicamento']
          med=Inventarios.objects.filter(Q(Name_med=medicamento)).exclude(Cantidad=0)
          ###########################################################################
          CB=ContadorBusq.objects.filter(Name_med=medicamento)
          if len(CB)==0:
            IMB=Inventarios.objects.filter(Name_med=medicamento)
            cont=1
            for i in IMB:
              nombre_med=i.Name_med
              MB=ContadorBusq(Name_med=nombre_med,Contador=cont)
              MB.save()
          else:
            for m in CB:
              medi=m.Name_med
              cont=m.Contador
            Ncont=cont+1
            BM=ContadorBusq.objects.filter(Name_med=medi)
            BM.delete()
            NBM=ContadorBusq(Name_med=medi,Contador=Ncont)
            NBM.save()
          #MostrarMs=ContadorBusq.objects.all()
          #return render_to_response("Busqueda/MasBuscado.html",{'Buscados':MostrarMs},context_instance=RequestContext(request))
          ###########################################################################
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
