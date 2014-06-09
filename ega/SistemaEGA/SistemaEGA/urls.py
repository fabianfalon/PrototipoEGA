from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SistemaEGA.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('apps.alumno.urls')),
    #url(r'^', include('apps.bedel.urls')),
    #url para trabajar con imagenes
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}),
    url(r'^admin/', include(admin.site.urls)),
)
