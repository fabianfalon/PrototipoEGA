from django.conf.urls import patterns, include, url
from .views import IndexView, PerfilView, LoginView, PreinscripcionView 
from .views import ErrorDocumentacionView, UserDetailView, ErrorDatosView, HistorialAcademicoView

urlpatterns = patterns('',
    
    url(r'^index/$', IndexView.as_view(), name='index'),
    url(r'^$', LoginView.as_view()),
    url(r'^documentacion/$', ErrorDocumentacionView.as_view(), name='documentacion'),
    url(r'^error/$', ErrorDatosView.as_view(), name='error'),
    url(r'^preinscripcion/$', PreinscripcionView.as_view()	, name='preinscripcion'),
    url(r'^perfil/$', PerfilView.as_view(), name='perfil'),
  	url(r'^usuario/(?P<slug>[-\w]+)/$', UserDetailView.as_view(), name='user_detail'),
  	url(r'^historial-academico/$', HistorialAcademicoView.as_view(), name='historial'),

  	url(r'^edit/(?P<id_alumno>\d+)/$', 'apps.alumno.views.edit_alumno', name='edit'),
  	url(r'^contacto/$', 'apps.alumno.views.contacto_view', name='contacto'),
    
)
