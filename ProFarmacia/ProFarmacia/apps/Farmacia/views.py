
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.template import RequestContext
from formulario import *
from ProFarmacia.apps.regfarmacia.models import Farmacias,Inventarios,ReporteVentas
#from ProFarmacia.apps.regfarmacia.formularios import *
from ProFarmacia.apps.regfarmacia import models
from django.contrib.auth import logout
from django.contrib.sessions.models import Session
from ProFarmacia.apps.Principal.views import Principal
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives
import os
import StringIO
from xhtml2pdf import pisa
from django.template.loader import render_to_string
import datetime

# Create your views here.
def login(request):
    if request.method=='POST':
        user=request.POST['usr']
        p=request.POST['pas']
        try:
            u = Farmacias.objects.get(ID_Usuario=user)
            if u.Password == p:
                request.session['usuario'] = u.ID_Usuario
            else:
                formulario=loginF()
                Error="El Usuario no exite"
                return render_to_response("Farmacia/login.html",{'formulario':formulario,'Error':Error},context_instance=RequestContext(request))
                #return HttpResponse("el usuario no exite")
            #return render_to_response('Farmacia/Ventas.html', {},RequestContext(request))
            return HttpResponseRedirect("/Ventas/")
        except Farmacias.DoesNotExist:
            formulario=loginF()
            Error2="El Usuario es incoreccto"
            return render_to_response("Farmacia/login.html",{'formulario':formulario,'Error2':Error2},context_instance=RequestContext(request))
            #return HttpResponse('El usuario es incoreccto')
    else:
        formulario=loginF()
    return render_to_response("Farmacia/login.html",{'formulario':formulario},context_instance=RequestContext(request))

def cerrar(request):
    logout(request)
    #return HttpResponse('El usuario desconectado')
    return HttpResponseRedirect("/Principal/")

def Rginventario(request):
    #user=login()#quiero aqui rescatar mi usuario logeado para poder poner a ID_Usuario=user
    if request.method == 'POST':
        form2=RInventario(request.POST)
        if form2.is_valid():
            medicamento=form2.cleaned_data['Name_med']
            cantidad=form2.cleaned_data['Cantidad']
            presio=form2.cleaned_data['Presio']
            categoria=form2.cleaned_data['CategoriaM']
            #recuperas el user de las variables de session
            if "usuario" in request.session:
                user=request.session['usuario']
            else:
                return HttpResponse("noexiste_el_usuario")
            #Id_usuario=formL.cleaned_data['usr']
            insertarM=Inventarios(Name_med=medicamento,Cantidad=cantidad,Costo=presio,ID_Usuario=user,Categoria=categoria)
            insertarM.save()
            
            return HttpResponseRedirect('/Minventario/')
            #return HttpResponse('Medicamento Registrado')
    else:
        form2 = RInventario()
    return render_to_response("Farmacia/reginventario.html",{'formRM':form2},context_instance=RequestContext(request))

def Minventario(request):
    
    if "usuario" in request.session:
        user=request.session['usuario']
    else:
        return HttpResponse("noexiste_el_usuario")
    Minv = Inventarios.objects.filter(ID_Usuario=user)
    return render_to_response('Farmacia/inventario.html',{'Minventario': Minv,'usuario':user},context_instance=RequestContext(request))

def CategoriaP(request):
    if "usuario" in request.session:
        user=request.session['usuario']
    else:
        return HttpResponse("noexiste_el_usuario")
    Minv = Inventarios.objects.filter(Q(ID_Usuario=user) & Q(Categoria='prescripcion'))
    return render_to_response('Farmacia/inventario.html',{'Minventario': Minv},context_instance=RequestContext(request))

def CategoriaOral(request):
    if "usuario" in request.session:
        user=request.session['usuario']
    else:
        return HttpResponse("noexiste_el_usuario")
    Minv = Inventarios.objects.filter(Q(ID_Usuario=user) & Q(Categoria='Oral'))
    return render_to_response('Farmacia/inventario.html',{'Minventario': Minv},context_instance=RequestContext(request))

def CategoriaTl(request):
    if "usuario" in request.session:
        user=request.session['usuario']
    else:
        return HttpResponse("noexiste_el_usuario")
    Minv = Inventarios.objects.filter(Q(ID_Usuario=user) & Q(Categoria='Parenteral'))
    return render_to_response('Farmacia/inventario.html',{'Minventario': Minv},context_instance=RequestContext(request))

def CategoriaTopica(request):
    if "usuario" in request.session:
        user=request.session['usuario']
    else:
        return HttpResponse("noexiste_el_usuario")
    Minv = Inventarios.objects.filter(Q(ID_Usuario=user) & Q(Categoria='Topica'))
    return render_to_response('Farmacia/inventario.html',{'Minventario': Minv},context_instance=RequestContext(request))

def CategoriaInyeccion(request):
    if "usuario" in request.session:
        user=request.session['usuario']
    else:
        return HttpResponse("noexiste_el_usuario")
    Minv = Inventarios.objects.filter(Q(ID_Usuario=user) & Q(Categoria='Inyeccion'))
    return render_to_response('Farmacia/inventario.html',{'Minventario': Minv},context_instance=RequestContext(request))

def CategoriaSublingual(request):
    if "usuario" in request.session:
        user=request.session['usuario']
    else:
        return HttpResponse("noexiste_el_usuario")
    Minv = Inventarios.objects.filter(Q(ID_Usuario=user) & Q(Categoria='Sublingual'))
    return render_to_response('Farmacia/inventario.html',{'Minventario': Minv},context_instance=RequestContext(request))

def CategoriaRectal(request):
    if "usuario" in request.session:
        user=request.session['usuario']
    else:
        return HttpResponse("noexiste_el_usuario")
    Minv = Inventarios.objects.filter(Q(ID_Usuario=user) & Q(Categoria='Rectal'))
    return render_to_response('Farmacia/inventario.html',{'Minventario': Minv},context_instance=RequestContext(request))

def Categoriatransdermica(request):
    if "usuario" in request.session:
        user=request.session['usuario']
    else:
        return HttpResponse("noexiste_el_usuario")
    Minv = Inventarios.objects.filter(Q(ID_Usuario=user) & Q(Categoria='transdermica'))
    return render_to_response('Farmacia/inventario.html',{'Minventario': Minv},context_instance=RequestContext(request))

def CategoriaInhalada(request):
    if "usuario" in request.session:
        user=request.session['usuario']
    else:
        return HttpResponse("noexiste_el_usuario")
    Minv = Inventarios.objects.filter(Q(ID_Usuario=user) & Q(Categoria='Inhalada'))
    return render_to_response('Farmacia/inventario.html',{'Minventario': Minv},context_instance=RequestContext(request))

#def ApliVentBuscar(request):
    ###########################
#    if "usuario" in request.session:
#        u=request.session['usuario']
#    else:
#        u="Anonimo"
#    if request.method=="POST":
#        formB=BusInvFarm(request.POST)
#        if(formB.is_valid()):
#            MedInventario=request.POST["B_med"]
#            lis_M=Inventarios.objects.filter(Name_med=MedInventario)
#            formB=BusInvFarm()
#            #Usuario = Fs.objects.filter(Q(ID_Usuario=user) & Q(Categoria='Topica'))
#            return render_to_response("Farmacia/Farmacia.html",{"lis_M":lis_M,"formB":formB,"usuario":u},RequestContext(request))

#    formB=BusInvFarm()
#    return render_to_response("Farmacia/Farmacia.html",{"formB":formB,"usuario":u},RequestContext(request))


def Editar(request,id):
    p=Inventarios.objects.get(id=id)
    if request.method == "POST":
        form = RInventario(request.POST,request.FILES)
        if form.is_valid():
            nombre= form.cleaned_data['Name_med']
            cantidad= form.cleaned_data['Cantidad']
            presio= form.cleaned_data['Presio']
            categoria= form.cleaned_data['CategoriaM']
            p.Name_med=nombre
            p.Cantidad=cantidad
            p.Costo=presio
            p.Categoria=categoria
            p.save()
            #return render_to_response("Farmacia/inventario.html",{},context_instance=RequestContext(request))
            #return HttpResponse('se edito correctamente')
            return HttpResponseRedirect('/Minventario/')
        else:
            return HttpResponse('esta mal')

      
    if request.method == "GET":
        form = RInventario(initial={
                'Name_med':p.Name_med,
                'Cantidad':p.Cantidad,
                'Presio':p.Costo,
                'CategoriaM':p.Categoria,
            })
    ctx={'form':form,'Inventarios':p}
    return render_to_response('Farmacia/Editar_inventario.html',ctx,context_instance=RequestContext(request))

def Eliminar(request,id):
    est=Inventarios.objects.get(id=id)
    est.delete()
    return HttpResponseRedirect('/Minventario/')

############################### Ventas
def Ventas(request):
    if "usuario" in request.session:
        u=request.session['usuario']
    else:
        u="Anonimo"

    if request.method == 'POST':
        formV=VentaMedicamento(request.POST)
        if  formV.is_valid():
            ###############
            formB=BusInvFarm()
            ####################
            nombre=formV.cleaned_data['N_medicamento']
            cantingre=int(formV.cleaned_data['Cant'])
            #presio=formV.cleaned_data['presio']
            #recuperas el user de las variables de session
            if "usuario" in request.session:
                user=request.session['usuario']
            else:
                return HttpResponse("noexiste_el_usuario")
            m=Inventarios.objects.filter(Q(Name_med=nombre) & Q(ID_Usuario=user))
            vm=len(m)
            cantidad=0
            Total=0
            if vm != 0:
                for i in m:
                    nombreM=i.Name_med
                    cantidad=i.Cantidad
                    categoria=i.Categoria
                    presio=i.Costo
                    cantidad=cantidad-cantingre
                    if cantidad < 0:
                        ErrorS="No exite Suficiente Stock"
                        return render_to_response("Farmacia/Ventas.html",{'ErrorS':ErrorS,'formV':formV,"formB":formB,"usuario":u},context_instance=RequestContext(request))
                    i.Cantidad=cantidad
                    i.save()
                    Total=presio*cantingre
                    #########################Poner en modelo Reportes ventas aki
                    IRV=ReporteVentas(ID_Usuario=u,Name_med=nombreM,CantidadV=cantingre,Total=Total)
                    IRV.save()
                    ########################
                    return render_to_response("Farmacia/Ventas.html",{'formV':formV,"formB":formB,'presio':presio,'categoria':categoria,'nombre':i.Name_med,'cantidad':cantidad,'Total':Total,"usuario":u},context_instance=RequestContext(request))
            else:
                error="El medicamento no existe"
                return render_to_response("Farmacia/Ventas.html",{'formV':formV,"formB":formB,'Error':error,"usuario":u},context_instance=RequestContext(request))
            formV=VentaMedicamento()
        ##########################################
        formB=BusInvFarm(request.POST)
        if(formB.is_valid()):
            MedInventario=request.POST["B_med"]
            lis_M=Inventarios.objects.filter(Q(Name_med=MedInventario) & Q(ID_Usuario=u))
            VM=len(lis_M)
            formB=BusInvFarm()
            if VM != 0:
                #Usuario = Fs.objects.filter(Q(ID_Usuario=user) & Q(Categoria='Topica'))
                return render_to_response("Farmacia/Ventas.html",{"lis_M":lis_M,"formB":formB,'formV':formV,"usuario":u},RequestContext(request))
            else:
                ErrorM="El medicamento no existe"
                return render_to_response("Farmacia/Ventas.html",{"lis_M":lis_M,"formB":formB,'formV':formV,"usuario":u,"ErrorM":ErrorM},RequestContext(request))

    
    else:
        formV = VentaMedicamento()
        formB=BusInvFarm()
        return render_to_response("Farmacia/Ventas.html",{"formB":formB,'formV':formV,"usuario":u},RequestContext(request))
    return render_to_response("Farmacia/Ventas.html",{'formV':formV,"formB":formB,"usuario":u},context_instance=RequestContext(request))


###############################

def Imprimir_Inventario(request):
    if "usuario" in request.session:
        user=request.session['usuario']
    else:
        return HttpResponse("noexiste_el_usuario")
    imprimir=Inventarios.objects.filter(ID_Usuario=user)
    html=render_to_string("Farmacia/imprimir.html",{'pagesize':'A4','Minventario':imprimir},context_instance=RequestContext(request))
    return generar_pdf(html)

def Imprimir_reportes(request):
    if "usuario" in request.session:
        user=request.session['usuario']
    else:
        return HttpResponse("noexiste_el_usuario")
    Reportes=ReporteVentas.objects.filter(ID_Usuario=user)
    SumTotal=0
    for t in Reportes:
        SumTotal=SumTotal + t.Total
    html=render_to_string("Farmacia/Reportes_ventas.html",{'pagesize':'A4','Mreporte':Reportes,'TotalVentas':SumTotal},context_instance=RequestContext(request))
    return generar_pdf(html)

def generar_pdf(html):
    resultado=StringIO.StringIO()
    pdf=pisa.pisaDocument(StringIO.StringIO(html.encode("UTF:8")),resultado)
    if not pdf.err:
        return HttpResponse(resultado.getvalue(),mimetype='application/pdf')
    return HttpResponse("Error en generar el pdf")

def formMapas(request):
    form=RInventario()
    return render_to_response("mapas/form.html",{"form":form},RequestContext(request))

def EditarUsuario(request):
    if "usuario" in request.session:
        u=request.session['usuario']
    else:
        u="Anonimo"
    p=Farmacias.objects.get(ID_Usuario=u)


    if request.method == "POST":
        form = EditarU(request.POST,request.FILES)
        if form.is_valid():
            nombre= form.cleaned_data['farmacia']
            ubicacion= form.cleaned_data['ubicacion']
            email= form.cleaned_data['email']
            #categoria= form.cleaned_data['CategoriaM']
            p.Name_Farmacia=nombre
            p.Ubicacion=ubicacion
            p.Email=email
            #p.Categoria=categoria
            p.save()
            #return render_to_response("Farmacia/inventario.html",{},context_instance=RequestContext(request))
            #return HttpResponse('se edito correctamente')
            Exito="El cambio se realizo Exitosamente"
            return render_to_response('Farmacia/Editar_informacion.html',{"Exito":Exito,'form':form},context_instance=RequestContext(request))
        else:
            Error="El cambio no se realizo correctamente"
            return render_to_response('Farmacia/Editar_informacion.html',{"Error":Error,'form':form},context_instance=RequestContext(request))

      
    if request.method == "GET":
        form = EditarU(initial={
                'farmacia':p.Name_Farmacia,
                'ubicacion':p.Ubicacion,
                'email':p.Email,

            })

    ctx={'form':form,'Farmacias':p}
    return render_to_response('Farmacia/Editar_informacion.html',ctx,context_instance=RequestContext(request))

def RecuperarPassword(request):
    info_enviado=False
    if request.method=="POST":
        formRP=RescatarPassword(request.POST)
        if formRP.is_valid():
            info_enviado=True
            usuario=formRP.cleaned_data['usuario']
            email=formRP.cleaned_data['email']
            #convertimos a minuscula para comparar

            #usuario=usuario.lower()
            #email= email.lower()
            #verificamos si existe usuario y password
            U=Farmacias.objects.filter(ID_Usuario=usuario)
            Vu=len(U)
            if Vu==0:
                ErrorU="El usuario no existe"
                return render_to_response('Farmacia/RescatarPassword.html',{"formRP":formRP,"ErrorU":ErrorU},context_instance=RequestContext(request))
            else:
                for i in U:
                    Veu=Farmacias.objects.filter(Q(ID_Usuario=i.ID_Usuario) & Q(Email=email))
                    if len(Veu)==0:
                        ErrorEU="El Email no pertenece a este Usuario"
                        return render_to_response('Farmacia/RescatarPassword.html',{"formRP":formRP,"ErrorEU":ErrorEU},context_instance=RequestContext(request))
                    else:
                        Exito="Su Password fue enviado a su Correo Electronico"
                        #return render_to_response('Farmacia/RescatarPassword.html',{"formRP":formRP,"Exito":Exito},context_instance=RequestContext(request))
                        #configuracion enviando mensaje via Gmail
                        for i in Veu:
                            email_user=i.Email
                            psw=i.Password
                            us=i.ID_Usuario
                        texto="Luego de recuperar Su Password le recomendamos cambiarlo"
                        para_usuario = email
                        html_contenido="Sr(a) Cliente Usted solicito su password por olvido<br>Su Id de Usuario: %s<br>Este es su Password: %s<br>***IMPORTANTE***<br><br>%s"%(us,psw,texto)
                        msg=EmailMultiAlternatives('Correo de Contacto',html_contenido,'from@server.com',[para_usuario])
                        msg.attach_alternative(html_contenido,'text/html')#convertimos el contenido a html
                        msg.send()#enviamos
                        return render_to_response('Farmacia/RescatarPassword.html',{"formRP":formRP,"Exito":Exito},context_instance=RequestContext(request))
    else:   
        formRP=RescatarPassword()
    ctx={'formRP':formRP}
    return render_to_response('Farmacia/RescatarPassword.html',ctx,context_instance=RequestContext(request))

