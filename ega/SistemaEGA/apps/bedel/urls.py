from django.conf.urls import patterns, include, url
from apps.bedel.views import  BedelView, CarreraView, CarrerasListaView, CarreraDeleteView, CarreraUpdateView
from apps.bedel.views import MateriasView, MateriasListaView, MateriaDeleteView, MateriaUpdateView
from apps.bedel.views import AlumnosListaView, AlumnoUpdateView, HistorialAcademicoView
from apps.bedel.views import ListaMateriasActaView, AlumnosListaActaDetailView
from apps.bedel.views import MesaFinalListaView, MesaFinalDeleteView, MesaFinalUpdateView, MesaFinalAddView
from apps.bedel.views import InscripcionMateriaAddView, InscripcionMateriaListaView, InscripcionMateriaUpdateView

urlpatterns = patterns('',

	 url(r'^index-bedel/$', BedelView.as_view()  , name='bedel'),

    #Operaciones con Carreras
    url(r'^index-bedel/agregar-carrera/$', CarreraView.as_view(), name='agregar_carrera'),
    url(r'^index-bedel/lista-carreras/$', CarrerasListaView.as_view(), name='lista_carrera'),
    url(r'^index-bedel/lista_carrera/eliminar/(?P<pk>\d+)/$', CarreraDeleteView.as_view(), name='carrera_confirm_delete'),
    url(r'^index-bedel/lista_carrera/editar/(?P<pk>\d+)/$', CarreraUpdateView.as_view(), name='editar_carrera'),

   #Operaciones con Materias
    url(r'^index-bedel/agregar-materias/$', MateriasView.as_view(), name='agregar_materia'), 
    url(r'^index-bedel/lista-materias/$', MateriasListaView.as_view(), name='lista_materia'), 
    url(r'^index-bedel/lista-materias/eliminar/(?P<pk>\d+)/$', MateriaDeleteView.as_view(), name='materia_confirm_delete'),
    url(r'^index-bedel/lista-materias/editar/(?P<pk>\d+)/$', MateriaUpdateView.as_view(), name='editar_materia'),

   #Operaciones con Alumnos 
   url(r'^index-bedel/lista-alumnos/$', AlumnosListaView.as_view(), name='lista_alumnos'),
   url(r'^index-bedel/lista_alumnos/editar/(?P<slug>[-\w]+)/edit/$', AlumnoUpdateView.as_view(), name='user_update'),

   #Historial Academico
   url(r'^index-bedel/agregar-Historial/$', HistorialAcademicoView.as_view(), name='agregar-historial'),

   #Operaciones con Examenes finales
   url(r'^index-bedel/lista-materias-acta/$', ListaMateriasActaView.as_view(), name='acta'),
   url(r'^index-bedel/lista-materias-acta/materia/(?P<pk>\d+)/$', AlumnosListaActaDetailView.as_view(), name='alumnos_generar_acta'),

   #Operaciones con Mesas de Examenes finales
   url(r'^index-bedel/agregar-lista-mesa-finales/$', MesaFinalAddView.as_view(), name='agregar_mesa_finales'), 
   url(r'^index-bedel/lista-mesa-finales/$', MesaFinalListaView.as_view(), name='lista_mesas_finales'), 
   url(r'^index-bedel/lista-mesa-finales/eliminar/(?P<pk>\d+)/$', MesaFinalDeleteView.as_view(), name='mesa_confirm_delete'),
   url(r'^index-bedel/lista-mesa-finales/editar/(?P<pk>\d+)/$', MesaFinalUpdateView.as_view(), name='editar_mesa'),

   #Inscripcion Materia
    url(r'^index-bedel/agregar-inscripcion-materia/$', InscripcionMateriaAddView.as_view(), name='agregar_inscripcion_materia'),
    url(r'^index-bedel/lista-inscripcion-materias/$', InscripcionMateriaListaView.as_view(), name='lista_inscripcion_materia'),
    url(r'^index-bedel/lista-inscripcion-materias/editar/(?P<pk>\d+)/$', InscripcionMateriaUpdateView.as_view(), name='editar_inscripcion_materia'),

   #Probando Ajax
   url(r'^ajax/url/$', 'apps.bedel.views.search', name='search'),
   
)
