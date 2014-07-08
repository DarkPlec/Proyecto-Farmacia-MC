from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
	url(r'^Buscar_Mcercano',Buscar_Mcercano),
	url(r'^MostrarFyM',MostrarFyM),
)
