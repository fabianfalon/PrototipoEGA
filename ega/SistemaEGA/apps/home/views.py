import random
from django.shortcuts import render
from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView, FormView, CreateView
from .models import Materia, User, InscripcionFinal, InscripcionMateria
from .forms import FinalForm, MateriaForm

class MateriasView(LoginRequiredMixin, TemplateView):

	template_name = 'home/materias.html'
	login_url = '/'
	model = Materia
	queryset = Materia.objects.all()
	context_object_name = 'materias'

	def get_context_data(self, **kwargs):

	
		#if Materia.carrera == self.request.user.carrera:
		context = super(MateriasView, self).get_context_data(**kwargs)
		context['materias'] = Materia.objects.all()
		return context


class FinalCreateView(CreateView):

    model = InscripcionFinal
    form_class = FinalForm
    cod_alumno = ""
    alumno = ""
    materia = ""
    mesa =""
    success_url = '/index'

    numero =  random.randint (1, 20)

    def form_valid(self, form):

    	cod_inscripcion = form.cleaned_data['cod_inscripcion']
    	alumno = form.cleaned_data['alumno']
    	materia = form.cleaned_data['materia']
    	mesa = form.cleaned_data['mesa']
    	form.save()
    	return super(FinalCreateView, self).form_valid(form)


class MateriaCreateView(CreateView):

    model = InscripcionMateria
    form_class = MateriaForm

    success_url = '/index'

 

 


# class FinalView(FormView):

# 	template_name = 'home/inscripcionfinal.html'
# 	form_class = FinalForm
# 	success_url = '/index'
	
	
# 	def form_valid(self, form):

# 		if Materia.carrera == self.request.user.carrera:
   
# 			form.instance.user = self.request.user
# 			form.save() #asignamos a la variabe user el formulario
# 			return super(FinalView, self).form_valid(form)

# 	def form_invalid(self, form):
		
# 		return super(FinalView, self).form_invalid(form)

