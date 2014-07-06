from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
	url(r'^$','ProFarmacia.apps.Principal.views.Principal')
)