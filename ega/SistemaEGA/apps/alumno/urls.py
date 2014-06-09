from django.conf.urls import patterns, include, url
from .views import IndexView, PerfilView

urlpatterns = patterns('',
    
    url(r'^$', IndexView.as_view()),
    url(r'^perfil/$', PerfilView.as_view(), name='perfil'),
    

    
)
