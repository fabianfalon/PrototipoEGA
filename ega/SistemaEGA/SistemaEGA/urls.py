from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
from apps.alumno.views import ImprimirHistorial
#importamos lo que necesitamos para imprimir
from wkhtmltopdf.views import PDFTemplateView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SistemaEGA.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'apps.alumno.views.index'),
    url(r'^cerrar/$', 'apps.alumno.views.cerrar'),

    url(r'^', include('apps.alumno.urls', namespace='alumnos')),
    url(r'^', include('apps.home.urls', namespace='home')),
   	
    #url para trabajar con imagenes
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}),
    url(r'^admin/', include(admin.site.urls)),

# url para imprimir

   url(r'^imprimir-historial/$',ImprimirHistorial.as_view(),name= 'imprimir-historial'),

 )

from django.conf.urls.static import static

# for dev static files serving
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

