from django.conf.urls import patterns, include, url
from .views import MateriasView, FinalCreateView, MateriaCreateView

urlpatterns = patterns('',
    
    #url(r'^inscripcion-finales/$', MateriasView.as_view(), name='inscripcion-finales'),
  #  url(r'^final/$', FinalView.as_view(), name='final'),
    url(r'^inscripcion-finales/$', FinalCreateView.as_view(), name='final_create'),
    url(r'^inscripcion-materias/$', MateriaCreateView.as_view(), name='create_materia'),



)
