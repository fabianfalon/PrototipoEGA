#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import User

class UserForm(ModelForm):

	class Meta:

		model = User
		fields = ('username','email','carrera', 'nombre_apellido', 
				   'dni', 'lugar_nacimiento', 'fecha_nacimiento','ciudad_actual',
				   'domicilio_actual' ,'password1' ,'imagen')


	username = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Nombre y Apellido',
					'required' : 'required'
				}))

	email = forms.EmailField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Email',
					'required' : 'required'
				}))


	carrera = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su DNI',
					'required' : 'required'
				}))
	nombre_apellido = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su DNI',
					'required' : 'required'
				}))

	dni = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Edad',
					'required' : 'required'
				}))

	lugar_nacimiento = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su lugar de Nacimiento',
					'required' : 'required'
				}))

	fecha_nacimiento = forms.DateField(widget= forms.widgets.DateInput(format= '%d.%m.%Y')) 


	ciudad_actual = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese la ciudad donde recide actualmente',
					'required' : 'required'
				}))

	domicilio_actual = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Domicilio Actual',
					'required' : 'required'
				}))



	password1 = forms.CharField(widget = forms.PasswordInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Usuario',
					'required' : 'required'
				}))



	imagen = forms.ImageField(widget=forms.FileInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Asunto',
					'required' : 'required'

				}))
	
class LoginForm(forms.Form):

	username = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Domicilio Actual',
					'required' : 'required'
				}))
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))







