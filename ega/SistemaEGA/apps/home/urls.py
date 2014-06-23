from django.conf.urls import patterns, include, url
from .views import  FinalCreateView, MateriaCreateView, MateriaDetailView

urlpatterns = patterns('',
    
    url(r'^inscripcion-finales/$', FinalCreateView.as_view(), name='final_create'),
    url(r'^inscripcion-materias/$', MateriaCreateView.as_view(), name='create_materia'),
    #url(r'^guardar-inscripcion-materias/$', 'apps.home.views.guardar_inscripcion', name='guardar_materia'),
    url(r'^inscripcion-materias/materia/(?P<pk>\d+)/$',MateriaDetailView.as_view(), name='materia_detail'),
   # url(r'^inscripcion-materias1/$', 'apps.home.views.materias_view', name='materia')
)
