from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProFarmacia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('ProFarmacia.apps.Principal.urlsPri')),
    url(r'^',include('ProFarmacia.apps.regfarmacia.urlsReg')),
    url(r'^',include('ProFarmacia.apps.Farmacia.urlsFar')),
    url(r'^',include('ProFarmacia.apps.Busqueda.urlsBus'))
)
