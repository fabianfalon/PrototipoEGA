#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Alumno

class AlumnoForm(ModelForm):

	class Meta:

		model = Alumno
		fields = ('carrera','nombre_apellido','dni','edad','lugar_nacimiento','fecha_nacimiento',
			'ciudad_actual','domicilio_actial','usuario','email','imagen')

	

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

	edad = forms.IntegerField(widget = forms.TextInput(attrs={
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

	domicilio_actial = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Domicilio Actual',
					'required' : 'required'
				}))

	usuario = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Usuario',
					'required' : 'required'
				}))


	email = forms.EmailField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Email',
					'required' : 'required'
				}))

	imagen = forms.ImageField(widget=forms.FileInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese su Asunto',
					'required' : 'required'

				}))
	
