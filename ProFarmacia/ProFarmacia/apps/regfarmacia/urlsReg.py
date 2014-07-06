from django.conf.urls import patterns, include, url
from .views import registroFar
urlpatterns = patterns('',
	url(r'^registroFar',registroFar)
)
