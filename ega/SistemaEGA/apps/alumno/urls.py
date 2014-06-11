from django.conf.urls import patterns, include, url
from .views import IndexView, PerfilView, LoginView, PreinscripcionView

urlpatterns = patterns('',
    
    url(r'^index/$', IndexView.as_view(), name='index'),

    url(r'^$', LoginView.as_view()),
    url(r'^preinscripcion/$', PreinscripcionView.as_view(), name='preinscripcion'),
    url(r'^perfil/$', PerfilView.as_view(), name='perfil'),
    

    
)
