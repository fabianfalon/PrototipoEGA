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
from .forms import UserForm, LoginForm, ContactForm, EditForm

#Vista de Login 
def index(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None: #si los datos son correctos
			if user.is_active and user.documentacion_completa == True: #preguntamos si el usuario esta activo y si presento la documentacion
				login(request,user) #se loguea
				return redirect('/index') #lo redirecciona al index
			else:
				return redirect('/documentacion')
		
		else:
			return redirect('/error')

	else:

		form = LoginForm()
		ctx = {'form':form}
		return render(request, 'alumno/login.html', ctx )

#Vista para Logout
@login_required(login_url='/')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')

class LoginView(TemplateView):
	
	template_name = 'alumno/login.html'


#Vista de Formulario de Preinscripcion
class PreinscripcionView(FormView):

	template_name = 'alumno/preinscripcion.html'
	form_class = UserForm
	success_url = '/'
	
	def form_valid(self, form):

		user = form.save() #asignamos a la variabe user el formulario
		user.set_password(form.cleaned_data['password']) #guardamos la clave encriptada
		user.save() #guardamos el formulario
		return super(PreinscripcionView, self).form_valid(form)

	def form_invalid(self, form):
		
		return super(PreinscripcionView, self).form_invalid(form)


class IndexView(LoginRequiredMixin, TemplateView):

	template_name = 'alumno/index.html'
	login_url = '/'
	model = User
	context_object_name = 'usuario'


class PerfilView(LoginRequiredMixin, TemplateView):
	
	template_name = 'alumno/perfil.html'
	login_url = '/'

#Vista para el Perfil de Usuario
class UserDetailView(DetailView):

	model = User
	context_object_name = 'usuario'
	slug_field = 'username'


#Vista para mandar Correo al Administrador
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

#Vista que muestra un error en el login si no presento la documentacion
class ErrorDocumentacionView(TemplateView):
	
	template_name = 'errores/documentacion_incompleta.html'

#Vista datos incorrectos en el form de login
class ErrorDatosView(TemplateView):

	template_name = 'errores/error_datos.html'

#vista para editar alumno
def edit_alumno(request, id_alumno):
	alumno = User.objects.get(id = id_alumno)
	if request.method == 'POST':
		form = EditForm(request.POST, request.FILES)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			nombre_apellido = form.cleaned_data['nombre_apellido']
			dni = form.cleaned_data['dni']
			lugar_nacimiento = form.cleaned_data['lugar_nacimiento']
			fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
			ciudad_actual = form.cleaned_data['ciudad_actual']
			domicilio_actual = form.cleaned_data['domicilio_actual']
			imagen = form.cleaned_data['imagen']
			alumno.username = username
			alumno.email = email
			alumno.nombre_apellido = nombre_apellido
			alumno.dni = dni
			alumno.lugar_nacimiento = lugar_nacimiento
			alumno.fecha_nacimiento = fecha_nacimiento
			alumno.ciudad_actual = ciudad_actual
			alumno.domicilio_actual = domicilio_actual
			alumno.imagen = imagen
			alumno.save()
			return redirect('/usuario/%s' %(alumno.username))
	if request.method == 'GET':
		form = EditForm(initial={
					'username' : alumno.username,
					'email' : alumno.email,
					'nombre_apellido': alumno.nombre_apellido,
					'dni': alumno.dni,
					'lugar_nacimiento': alumno.lugar_nacimiento,
					'fecha_nacimiento': alumno.fecha_nacimiento,
					'ciudad_actual': alumno.ciudad_actual,
					'domicilio_actual': alumno.domicilio_actual,
					'imagen': alumno.imagen,

			})
	ctx = {'form':form, 'alumno':alumno}
	return render_to_response('alumno/editar_datos.html', ctx, context_instance=RequestContext(request))		

#Visualizar el Historial Academico
class HistorialAcademicoView(TemplateView):
	
	template_name = 'alumno/historial_academico.html'
