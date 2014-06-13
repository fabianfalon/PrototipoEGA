from django.contrib import messages
from django.core.mail import  EmailMessage, EmailMultiAlternatives
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render, RequestContext
from django.views.generic import TemplateView, FormView, DetailView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from braces.views import LoginRequiredMixin
from apps.alumno.models import User
from .forms import UserForm, LoginForm, ContactForm


def index(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None and user.is_active and user.documentacion_completa == True:
			login(request,user)
			return redirect('/index')
		else:
			return redirect('/documentacion')
	
			#return HttpResponse('El formulario no es valido')
	else:
		form = LoginForm()
		ctx = {'form':form}
		return render(request, 'alumno/login.html', ctx )

@login_required(login_url='/')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')


class ErrorDocumentacionView(TemplateView):
	
	template_name = 'errores/documentacion_incompleta.html'

class LoginView(TemplateView):
	
	template_name = 'alumno/login.html'

class PreinscripcionView(FormView):

	template_name = 'alumno/preinscripcion.html'
	form_class = UserForm
	success_url = '/'
	
	def form_valid(self, form):

		user = form.save()
		user.set_password(form.cleaned_data['password'])
		user.save()
		return super(PreinscripcionView, self).form_valid(form)

	def form_invalid(self, form):
		
		return super(PreinscripcionView, self).form_invalid(form)


class IndexView(LoginRequiredMixin, TemplateView):

	template_name = 'alumno/index.html'
	login_url = '/'


class PerfilView(LoginRequiredMixin, TemplateView):
	
	template_name = 'alumno/perfil.html'
	login_url = '/'

class UserDetailView(DetailView):

	model = User
	context_object_name = 'usuario'

@login_required(login_url='/')

def contacto_view(request):
	form_class = ContactForm
	email = ""
	titulo = ""
	texto = ""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']
			message = "Mensaje de : [%s]<br> Texto : [%s]"%(email,texto)
			msg = EmailMessage( subject= titulo, 
							    body = message,
							    from_email= email,
							    to = ['fabian.falon@gmail.com'])
		     
			msg.send()
			return redirect('/index')
	else: 
		formulario = ContactForm()
		ctx = {'form':formulario, 'email':email, 'titulo':titulo, 'texto':texto}
		return render_to_response('alumno/contacto.html',ctx,context_instance=RequestContext(request))


	