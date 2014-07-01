from django.shortcuts import render
from django.views.generic import TemplateView, FormView, DetailView, UpdateView, DeleteView 
from braces.views import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect
from apps.alumno.models import User
from apps.home.models import Carrera, Materia, HistorialAcademico, InscripcionMateria, InscripcionFinal, MesaFinal
from .forms import CarreraForm, MateriaForm, UserForm, HistorialForm, MesaFinalForm


class BedelView(LoginRequiredMixin, TemplateView):

    template_name = 'bedel/menu_bedel.html'

#Comienza operaciones con carreras

#Crear Carrera
class CarreraView(LoginRequiredMixin, FormView):

	template_name = 'bedel/agregar_carrera.html'
	form_class = CarreraForm
	success_url = '/index-bedel/'
	
	def form_valid(self, form):

		user = form.save() #asignamos a la variabe user el formulario
		user.save() #guardamos el formulario
		return super(CarreraView, self).form_valid(form)

	def form_invalid(self, form):
		
		return super(CarreraView, self).form_invalid(form)

#Mostrar Carreras
class CarrerasListaView(LoginRequiredMixin, TemplateView):

	model = Carrera
	template_name = 'bedel/lista_carreras.html'

	def get_context_data(self, **kwargs):

		context = super(CarrerasListaView, self).get_context_data(**kwargs)
		context['lista_carrera'] = Carrera.objects.all()
		return context

#Eliminar Carreras
class CarreraDeleteView(LoginRequiredMixin, DeleteView):

    model = Carrera
    success_url = '/index-bedel/lista-carreras'

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

#Actualizar datos de Carrera
class CarreraUpdateView(LoginRequiredMixin, UpdateView):

	model = Carrera
	form_class = CarreraForm
	template_name_suffix = '__update_form'
	success_url = '/index-bedel/lista-carreras'
	context_object_name = 'carrera'
	
	def form_valid(self, form):
		user = form.save() #asignamos a la variabe user el formulario
		return super(CarreraUpdateView, self).form_valid(form)

	def form_invalid(self, form):
		
		return super(CarreraUpdateView, self).form_invalid(form)



#Operaciones con Materias

#Agregar Materias
class MateriasView(LoginRequiredMixin, FormView):

	template_name = 'bedel/agregar_materias.html'
	form_class = MateriaForm
	success_url = '/index-bedel/'
	
	def form_valid(self, form):

		user = form.save() #asignamos a la variabe user el formulario
		user.save() #guardamos el formulario
		return super(MateriasView, self).form_valid(form)

	def form_invalid(self, form):
		
		return super(MateriasView, self).form_invalid(form)

#Mostrar Materias
class MateriasListaView(LoginRequiredMixin,TemplateView):

	model = Materia
	template_name = 'bedel/lista_materias.html'

	def get_context_data(self, **kwargs):

		context = super(MateriasListaView, self).get_context_data(**kwargs)
		context['lista_materias'] = Materia.objects.all()
		return context

#Eliminar Materias
class MateriaDeleteView(LoginRequiredMixin, DeleteView):

    model = Materia
    success_url = '/index-bedel/lista-materias'

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

#Actualizar datos de Materia
class MateriaUpdateView(LoginRequiredMixin, UpdateView):

	model = Materia
	form_class = MateriaForm
	template_name_suffix = '__update_form'
	success_url = '/index-bedel/lista-materias'
	context_object_name = 'materia'
	
	def form_valid(self, form):
		user = form.save() #asignamos a la variabe user el formulario
		return super(MateriaUpdateView, self).form_valid(form)

	def form_invalid(self, form):
		
		return super(MateriaUpdateView, self).form_invalid(form)

#Operaciones con Alumnos
#Mostrar Alumnos
class AlumnosListaView(LoginRequiredMixin, TemplateView):

	model = User
	template_name = 'bedel/lista_alumnos.html'

	def get_context_data(self, **kwargs):

		context = super(AlumnosListaView, self).get_context_data(**kwargs)
		context['lista_alumnos'] = User.objects.filter(tipo_usuario = False)
		return context

#Actualizar datos de alumno
class AlumnoUpdateView(LoginRequiredMixin, UpdateView):

	model = User
	form_class = UserForm
	slug_field = 'username'
	template_name_suffix = 'alumno__update_form'
	success_url = '/index-bedel/lista-alumnos'
	context_object_name = 'materia'

	def form_valid(self, form):
		user = form.save() #asignamos a la variabe user el formulario
		user.set_password(form.cleaned_data['password']) #guardamos la clave encriptada
		user.save() #guardamos el formulario
		return super(AlumnoUpdateView, self).form_valid(form)

	def form_invalid(self, form):
		
		return super(AlumnoUpdateView, self).form_invalid(form)
	

#Agregar Historial Academico
class HistorialAcademicoView(LoginRequiredMixin, FormView):

	model = HistorialAcademico
	template_name = 'bedel/agregar_nota_final.html'
	form_class = HistorialForm
	success_url = '/index-bedel/'

	def post(self, request, *args, **kwargs):
		post = super(HistorialAcademicoView, self).post(request, *args, **kwargs)
		alumno = request.POST['alumno']
		materia = request.POST['materia']
		nota = request.POST['nota']
		fecha = request.POST['fecha']
		HistorialAcademico.objects.create(alumno=User.objects.get(nombre_apellido=alumno), materia=Materia.objects.get(nombre=materia), nota=nota, fecha=fecha)
		return post


	def form_invalid(self, form):
		
		return super(HistorialAcademicoView, self).form_invalid(form)

#Operaciones con Mesa de Examen final
#Agregar Mesa de Examen Final
class MesaFinalAddView(LoginRequiredMixin, FormView):

	template_name = 'bedel/agregar_mesa_final.html'
	form_class = MesaFinalForm
	success_url = '/index-bedel/'
	
	def form_valid(self, form):

		user = form.save() #asignamos a la variabe user el formulario
		user.save() #guardamos el formulario
		return super(MesaFinalAddView, self).form_valid(form)

	def form_invalid(self, form):
		
		return super(MesaFinalAddView, self).form_invalid(form)


#Mostrar Mesas
class MesaFinalListaView(LoginRequiredMixin,TemplateView):

	model =  MesaFinal
	template_name = 'bedel/lista_mesa_final.html'

	def get_context_data(self, **kwargs):

		context = super(MesaFinalListaView, self).get_context_data(**kwargs)
		context['lista_mesa_final'] =  MesaFinal.objects.all()
		return context

#Eliminar Mesa
class MesaFinalDeleteView(LoginRequiredMixin, DeleteView):

    model = MesaFinal
    success_url = '/index-bedel/'

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

#Actualizar datos de Mesa
class MesaFinalUpdateView(LoginRequiredMixin, UpdateView):

	model = MesaFinal
	form_class = MesaFinalForm
	template_name_suffix = '__update_form'
	success_url = '/index-bedel/lista-materias'
	context_object_name = 'mesafinal'
	
	def form_valid(self, form):
		user = form.save() #asignamos a la variabe user el formulario
		return super(MesaFinalUpdateView, self).form_valid(form)

	def form_invalid(self, form):
		
		return super(MesaFinalUpdateView, self).form_invalid(form)

#Lista de materias para generar Acta
class ListaMateriasActaView(LoginRequiredMixin,TemplateView):

	model = Materia
	template_name = 'bedel/lista_materias_acta.html'

	def get_context_data(self, **kwargs):

		context = super(ListaMateriasActaView, self).get_context_data(**kwargs)
		context['lista_materias_acta'] = Materia.objects.all()
		return context


#Mostrar Alumnos inscriptos en la materia que se hizo click
class AlumnosListaActaDetailView(LoginRequiredMixin, TemplateView):

	template_name = 'bedel/lista_alumnos_acta.html'
	model = InscripcionFinal
	context_object_name = "acta"	

	def get_context_data(self, **kwargs):
		context = super(AlumnosListaActaDetailView, self).get_context_data(**kwargs)
		context['total_alumnos_acta'] = InscripcionFinal.objects.filter(materia= kwargs['pk'])
		#print context['total_alumnos_acta']
		return context


# class AlumnosListaActaDetailView(LoginRequiredMixin,DetailView):

# 	template_name = 'bedel/lista_alumnos_acta.html'
# 	model = InscripcionFinal

# 	def get_context_data(self, *args, **kwargs):

# 		context = super(AlumnosListaActaDetailView, self).get_context_data(**kwargs)
# 		context['total_alumnos_acta'] = InscripcionFinal.objects.filter(materia=context['object'])
# 		print inscripcionfinal
# 		print context['total_alumnos_acta']
# 		return context