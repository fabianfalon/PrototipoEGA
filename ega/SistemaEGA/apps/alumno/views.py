from django.contrib import messages
from django.core.mail import  EmailMessage, EmailMultiAlternatives
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render, RequestContext
from django.views.generic import TemplateView, FormView, DetailView, UpdateView, DeleteView 
from wkhtmltopdf.views import PDFTemplateView, PDFTemplateResponse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from braces.views import LoginRequiredMixin
from apps.alumno.models import User
from apps.home.models import HistorialAcademico, InscripcionMateria, InscripcionFinal
from .forms import UserForm, LoginForm, ContactForm, EditForm


#Vista de Login 
def index(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None: #si los datos son correctos
			if user.is_active and user.documentacion_completa == True and user.tipo_usuario == True: #preguntamos si el usuario esta activo y si presento la documentacion
				login(request,user) #se loguea como bedel
				return redirect('/index-bedel') #lo redirecciona al index
			else:
				if user.is_active and user.documentacion_completa == True:

					login(request,user) #se loguea como alumno
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

#Index Alumno
class IndexView(LoginRequiredMixin, TemplateView):

	template_name = 'alumno/index.html'
	login_url = '/'
	model = User
	context_object_name = 'usuario'


class PerfilView(LoginRequiredMixin, TemplateView):
	
	template_name = 'alumno/perfil.html'
	login_url = '/'

#Vista para el Perfil de Usuario
class UserDetailView(LoginRequiredMixin, DetailView):

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
			message = "Mensaje de : [%s][%s]<br> Texto : [%s]"%(request.user.nombre_apellido, email,texto)
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

#Visualizar el Historial Academico
class HistorialAcademicoView(TemplateView):

	models = HistorialAcademico
	template_name = 'alumno/historial_academico.html'

	def get_context_data(self, **kwargs):

		context = super(HistorialAcademicoView, self).get_context_data(**kwargs)
		context['historial_materias'] = HistorialAcademico.objects.filter(alumno = self.request.user)
		#print context
		return context
        #historial_materias = HistorialAcademico.objects.filter(alumno = request.user)
        #context['historial_materias'] = historial_materias
    	

#Vista para que el alumno pueda modificar sus datos
class AlumnoUpdateView(LoginRequiredMixin, UpdateView):

	model = User 
	form_class = UserForm
	slug_field = 'username'
	fields = ['nombre_apellido','username', 'email', 'dni', 'lugar_nacimiento','fecha_nacimiento', 'ciudad_actual', 'domicilio_actual', 'imagen', 'password']
	template_name_suffix = '__update_form'
	success_url = '/index'
	context_object_name = 'usuario'

	def get_object(self, queryset=None): 
		return self.request.user
	
	def form_valid(self, form):
		user = form.save() #asignamos a la variabe user el formulario
		user.set_password(form.cleaned_data['password']) #guardamos la clave encriptada
		user.save() #guardamos el formulario
		return super(AlumnoUpdateView, self).form_valid(form)

	def form_invalid(self, form):
		
		return super(AlumnoUpdateView, self).form_invalid(form)

#Imprimir Historial Academico
class ImprimirHistorial(PDFTemplateView):
       filename = 'historial.pdf'
       template_name = 'pfd/pdfhistorial.html'
       cmd_options = {
           'margin-top': 3,
       }
       
       def get_context_data(self, **kwargs):
		   context = super(ImprimirHistorial, self).get_context_data(**kwargs)
		   context['historial_materias'] = HistorialAcademico.objects.filter(alumno = self.request.user)
		  # context['historial']=Articulo.objects.get(id=kwargs['pk'])
		   return context

#imprime las materias a cursar
class ImprimirMaterias(PDFTemplateView):
       filename = 'historial.pdf'
       template_name = 'pfd/pdfmaterias.html'
       cmd_options = {
           'margin-top': 3,
       }
       
       def get_context_data(self, **kwargs):
		   context = super(ImprimirMaterias, self).get_context_data(**kwargs)
		   context['lista_materias'] = InscripcionMateria.objects.filter(alumno = self.request.user)
		   return context

#imprime las materias a rendir FInal
class ImprimirFinales(PDFTemplateView):
       filename = 'permiso.pdf'
       template_name = 'pfd/pdf-finales.html'
       cmd_options = {
           'margin-top': 3,
       }
       
       def get_context_data(self, **kwargs):
		   context = super(ImprimirFinales, self).get_context_data(**kwargs)
		   context['lista_materias'] = InscripcionFinal.objects.filter(alumno = self.request.user)
		   return context

# #Imprimir Acta de examen final
class ImprimirActa(PDFTemplateView):

 	filename='acta.pdf'
 	template_name = 'pfd/pdf-acta.html'
 	cmd_options = {
 		'encoding': 'utf8', 'quiet': True
 	}

 	def get_context_data(self, **kwargs):
           context = super(ImprimirActa, self).get_context_data(**kwargs)
           context['total_alumnos_acta']=InscripcionFinal.objects.filter(materia=kwargs['pk'])
           return context

#Me muestra todas las materias en las que el alumno se inscribio para cursar
class ListaMateriasView(TemplateView):

    model = InscripcionMateria
    template_name = 'alumno/lista_materias.html'

    def get_context_data(self, **kwargs):

        context = super(ListaMateriasView, self).get_context_data(**kwargs)
        context['lista_materias'] = InscripcionMateria.objects.filter(alumno = self.request.user)
        return context

#Me muestra todas las materias en las que el alumno se inscribio para rendir final
class ListaFinalView(TemplateView):

    model = InscripcionFinal
    template_name = 'alumno/lista_finales.html'

    def get_context_data(self, **kwargs):

        context = super(ListaFinalView, self).get_context_data(**kwargs)
        context['lista_materias'] = InscripcionFinal.objects.filter(alumno = self.request.user)
        return context
