from django.conf.urls import patterns, include, url
from .views import  FinalCreateView, FinalDetailView, MateriaCreateView, MateriaDetailView, BedelView, FinalDeleteView

urlpatterns = patterns('',
    #Operaciones con finales (Alumno)
    url(r'^inscripcion-finales/$', FinalCreateView.as_view(), name='final_create'),
    url(r'^inscripcion-finales/(?P<pk>\d+)/$', FinalDetailView.as_view(), name='create_final'),
    #url(r'^inscripcion-finales/(?P<pk>\d+)/$', FinalDetailView.as_view(), name='final_detail'),


    #Operaciones con Materias (Alumno)
    url(r'^inscripcion-materias/$', MateriaCreateView.as_view(), name='create_materia'),
    url(r'^inscripcion-materias/materia/(?P<pk>\d+)/$',MateriaDetailView.as_view(), name='materia_detail'),
    
    #Operaciones del Bedel (Alumno)
    url(r'^eliminar-finales/(?P<pk>\d+)/$', FinalDeleteView.as_view(), name='final_confirm_delete'),
  
)
