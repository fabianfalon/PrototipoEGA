from django.forms import ModelForm
from django import forms
from .models import InscripcionFinal, InscripcionMateria, Materia

class FinalForm(ModelForm):

	class Meta:

		model = InscripcionFinal
		fields = ('cod_inscripcion','mesa')


		cod_inscripcion = forms.CharField(widget = forms.TextInput(attrs={
	 				'class' : 'form-control',
	 				'placeholder' : 'Ingrese el codigo de la inscripcion',
	 				'required' : 'required'
	 			}))


	 	mesa = forms.CharField(widget = forms.TextInput(attrs={
	 				'class' : 'form-control',
					'placeholder' : 'Ingrese la mesa',
    				'required' : 'required'
	 			}))


class MateriaForm(ModelForm):

	class Meta:

		model = InscripcionMateria
		fields = ('materia',)
