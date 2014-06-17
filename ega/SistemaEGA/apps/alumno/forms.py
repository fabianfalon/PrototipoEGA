#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import User

class UserForm(ModelForm):

	class Meta:

		model = User
		fields = ('username','email','carrera', 'nombre_apellido', 
				   'dni', 'lugar_nacimiento', 'fecha_nacimiento','ciudad_actual',
				   'domicilio_actual' ,'imagen', 'password')


	username = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Usuario',
					'required' : 'required'
				}))

	email = forms.EmailField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Email',
					'required' : 'required'
				}))


	carrera = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese la Carrera ',
					'required' : 'required'
				}))
	nombre_apellido = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Nombre y Apellido',
					'required' : 'required'
				}))

	dni = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su DNI',
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

	password = forms.CharField(widget = forms.PasswordInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Contraseña',
					'required' : 'required'
				}))

	imagen = forms.ImageField(widget=forms.FileInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Imagen de Pefil',
					

				}))



	
class LoginForm(forms.Form):

	username = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'name' : 'username',
					'placeholder' : 'Ingrese su Usuario',
					'required' : 'required'
				}))
	password = forms.CharField(widget = forms.PasswordInput(attrs={
					'class' : 'form-control',
					'name' : 'password',
					'placeholder' : 'Ingrese su Contraseña',
					'required' : 'required'
				}))



class ContactForm(forms.Form):
	Email = forms.EmailField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Email',
					'required' : 'required'
				}))

	Titulo = forms.CharField(widget=forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Asunto',
					'required' : 'required'

				}))
	Texto = forms.CharField(widget=forms.Textarea(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Texto',
					'required' : 'required'
				}))
	


class EditForm(forms.Form):

	username = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su NOmbre de Usuario',
					'required' : 'required'
				}))

	email = forms.EmailField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Email',
					'required' : 'required'
				}))

	nombre_apellido = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Nombre y Apellido',
					'required' : 'required'
				}))

	dni = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su DNI',
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

	imagen = forms.ImageField(widget=forms.FileInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Imagen de Perfil'

				}))
