from django.conf.urls import patterns, include, url
from .views import IndexView, PerfilView, LoginView, PreinscripcionView, ErrorDocumentacionView, UserDetailView

urlpatterns = patterns('',
    
    url(r'^index/$', IndexView.as_view(), name='index'),
    url(r'^$', LoginView.as_view()),
    url(r'^documentacion/$', ErrorDocumentacionView.as_view(), name='documentacion'),
    url(r'^preinscripcion/$', PreinscripcionView.as_view()	, name='preinscripcion'),
    url(r'^perfil/$', PerfilView.as_view(), name='perfil'),
  	url(r'^usuario/(?P<pk>\d+)/$', UserDetailView.as_view(), name='user_detail'),
  	url(r'^contacto/$', 'apps.alumno.views.contacto_view', name='contacto'),
    
)
