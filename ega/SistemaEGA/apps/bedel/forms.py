from django.forms import ModelForm
from django import forms
from apps.home.models import Carrera, Materia, MesaFinal, InscripcionMateria, InscripcionFinal, HistorialAcademico
from apps.alumno.models import User

class CarreraForm(ModelForm):


	class Meta:

		model = Carrera
		fields = ('cod_carrera', 'nombre', 'resolucion', 'duracion')


	cod_carrera = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese el codigo de la carrera',
					'required' : 'required'
				}))

	nombre = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese nombre de la carrera',
					
				}))

	resolucion = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese numero de resolucion de la carrera',
					
				}))

	duracion = forms.IntegerField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese la duracion de la carrera',
					
				}))

class MateriaForm(ModelForm):


	class Meta:

		model = Materia
		fields = ('cod_materia','nombre', 'carrera', 'duracion', 'anio')


	cod_materia = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese el codigo de la materia',
					'required' : 'required'
				}))

	nombre = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese nombre de la Materia',
					
				}))
	duracion = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese la duracion de la materia',
					
				}))
	anio = forms.IntegerField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese el anio al que pertenece la materia',
					
				}))

class UserForm(ModelForm):

	class Meta:

		model = User
		fields = ('nombre_apellido', 'username','email', 'cod_alumno', 'dni', 'lugar_nacimiento',
					'fecha_nacimiento', 'ciudad_actual', 'domicilio_actual','tipo_usuario',
					'documentacion_completa','imagen', 'password')


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
					'placeholder' : 'Ingrese la clave del alumno en caso de que quiera cambiarla'
				}))


class HistorialForm(ModelForm):

	class Meta:

		model = HistorialAcademico


class MesaFinalForm(ModelForm):

	class Meta:

		model = MesaFinal

class InscripcionMateriaForm(ModelForm):

	class Meta:
		
		model = InscripcionMateria
		fields = ('alumno','materia')


	alumno = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese el nombre del alumno',
					'required' : 'required'
				}))

	materia = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese nombre de la Materia',
					
				}))
		



