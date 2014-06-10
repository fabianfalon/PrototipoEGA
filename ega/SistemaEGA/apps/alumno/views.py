from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.views.generic import TemplateView, FormView

from .forms import AlumnoForm



class LoginView(TemplateView):
	
	template_name = 'alumno/login.html'

class PreinscripcionView(FormView):

	template_name = 'alumno/preinscripcion.html'
	form_class = AlumnoForm
	success_url = '/'
	

	def form_valid(self, form):
		
		form.save()
		return super(PreinscripcionView, self).form_valid(form)

	def form_invalid(self, form):
		print "invalido"
		return super(PreinscripcionView, self).form_invalid(form)



class IndexView(TemplateView):

	template_name = 'alumno/index.html'

class PerfilView(TemplateView):
	
	template_name = 'alumno/perfil.html'