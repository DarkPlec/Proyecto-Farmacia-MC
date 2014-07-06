from django.conf.urls import patterns, include, url
from .views import *
from ProFarmacia.apps.Principal.views import Principal
urlpatterns = patterns('',
	url(r'^login',login),
	url(r'^cerrar',cerrar),
	url(r'^Rginventario',Rginventario),
	url(r'^Minventario',Minventario),
	url(r'^Principal',Principal),
	#url(r'^ApliVentBuscar',ApliVentBuscar),
	url(r'^Editar/(?P<id>.*)/',Editar),
	url(r'^Eliminar/(?P<id>.*)/',Eliminar),
	url(r'^CategoriaP',CategoriaP),
	url(r'^CategoriaTl',CategoriaTl),
	url(r'^CategoriaTopica',CategoriaTopica),
	url(r'^CategoriaInyeccion',CategoriaInyeccion),
	url(r'^CategoriaOral',CategoriaOral),
	url(r'^CategoriaSublingual',CategoriaSublingual),
	url(r'^CategoriaRectal',CategoriaRectal),
	url(r'^Categoriatransdermica',Categoriatransdermica),
	url(r'^CategoriaInhalada',CategoriaInhalada),
	url(r'^Imprimir_Inventario',Imprimir_Inventario),
	url(r'^Ventas',Ventas),
 	url(r'^mapas/$',formMapas),
 	url(r'^EditarUsuario',EditarUsuario),
 	url(r'^RecuperarPassword',RecuperarPassword),
 	url(r'^Imprimir_reportes',Imprimir_reportes),

)
