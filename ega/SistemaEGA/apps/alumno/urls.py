from django.conf.urls import patterns, include, url
from .views import IndexView, PerfilView, LoginView, PreinscripcionView, AlumnoUpdateView, ListaMateriasView
from .views import ErrorDocumentacionView, UserDetailView, ErrorDatosView, HistorialAcademicoView, ListaFinalView
from apps.home.views import BedelView

urlpatterns = patterns('',
    
    url(r'^index/$', IndexView.as_view(), name='index'),
    url(r'^$', LoginView.as_view()),
    url(r'^documentacion/$', ErrorDocumentacionView.as_view(), name='documentacion'),
    url(r'^error/$', ErrorDatosView.as_view(), name='error'),
    url(r'^preinscripcion/$', PreinscripcionView.as_view()	, name='preinscripcion'),
    url(r'^perfil/$', PerfilView.as_view(), name='perfil'),

  	url(r'^usuario/(?P<slug>[-\w]+)/$', UserDetailView.as_view(), name='user_detail'),
    url(r'^usuario/(?P<slug>[-\w]+)/edit/$', AlumnoUpdateView.as_view(), name='user_update'),
  
  	url(r'^historial-academico/$', HistorialAcademicoView.as_view(), name='historial'),
    url(r'^consulta-materias/$', ListaMateriasView.as_view(), name='materias-cursar'),
    url(r'^consulta-finales/$', ListaFinalView.as_view(), name='materias-final'),
    #url(r'^eliminar-finales/(?P<pk>\d+)/$', FinalDelete.as_view(), name='final_confirm_delete'),

  	#url(r'^edit/(?P<id_alumno>\d+)/$', 'apps.alumno.views.edit_alumno', name='edit'),
  	url(r'^contacto/$', 'apps.alumno.views.contacto_view', name='contacto'),

    #operaciones del bedel
    url(r'^index-bedel/$', BedelView.as_view()  , name='bedel'),
)
