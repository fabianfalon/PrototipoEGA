from django.forms import ModelForm
from django import forms
from .models import InscripcionFinal, InscripcionMateria

class FinalForm(ModelForm):

	class Meta:

		model = InscripcionFinal
		fields = ('cod_inscripcion', 'materia', 'alumno', 'mesa')


		cod_inscripcion = forms.CharField(widget = forms.TextInput(attrs={
	 				'class' : 'form-control',
	 				'placeholder' : 'Ingrese su Domicilio Actual',
	 				'required' : 'required'
	 			}))

	 	alumno = forms.CharField(widget = forms.TextInput(attrs={
	 				'class' : 'form-control',
	 				'placeholder' : 'Ingrese su Domicilio Actual',
	 				
	 			}))


	 	materia = forms.CharField(widget = forms.TextInput(attrs={
	 				'class' : 'form-control',
	 				'placeholder' : 'Ingrese su Domicilio Actual',
	 				'required' : 'required'
	 			}))

	 	mesa = forms.CharField(widget = forms.TextInput(attrs={
	 				'class' : 'form-control',
					'placeholder' : 'Ingrese su Domicilio Actual',
    				'required' : 'required'
	 			}))

		carrera = forms.CharField(widget = forms.TextInput(attrs={
	 				'class' : 'form-control',
	 				'placeholder' : 'Ingrese su Domicilio Actual',
	 			
	 			}))

class MateriaForm(ModelForm):

	class Meta:

		model = InscripcionMateria
		fields = ('materia',)

