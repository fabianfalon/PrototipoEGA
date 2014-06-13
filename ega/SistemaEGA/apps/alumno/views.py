from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.views.generic import TemplateView, FormView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from braces.views import LoginRequiredMixin


from .forms import UserForm, LoginForm


def index(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None and user.is_active:
			login(request,user)
			return redirect('/index')
		else:
			return HttpResponse('Algo salio mal')
		#else: 
		#	return HttpResponse('El formulario no es valido')
	else:
		form = LoginForm()
		ctx = {'form':form}
		return render(request, 'alumno/login.html', ctx )

@login_required(login_url='/')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')



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


