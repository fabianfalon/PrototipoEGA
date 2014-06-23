import random
from django.shortcuts import redirect, HttpResponseRedirect
from braces.views import LoginRequiredMixin
from django.views.generic import FormView, CreateView, DetailView, TemplateView, DeleteView
from .models import Materia, User, InscripcionFinal, InscripcionMateria, Carrera, MesaFinal
from .forms import FinalForm, MateriaForm

#Mostrar lista de materias para rendir examen Final
class FinalCreateView(LoginRequiredMixin, CreateView):

    model = Materia

    def get_context_data(self, **kwargs):

        context = super(FinalCreateView, self).get_context_data(**kwargs)
        carrera = Carrera.objects.get(alumno__in = [self.request.user])
        context['total_materias_finales'] = Materia.objects.filter(carrera = carrera)
        return context

#Muestra el detalle de la materia para inscribirse al examen final
class FinalDetailView(LoginRequiredMixin, DetailView):

    template_name = 'home/create_final.html'
    model = Materia
    form_class = FinalForm
    context_object_name = 'materia'

    def get_context_data(self, **kwargs):
        mesa = MesaFinal()    
        context = super(FinalDetailView, self).get_context_data(**kwargs)
        context['mesa'] =mesa.turno
        return context

    def post(self, request, *args, **kwargs):

        inscripcionfinal = InscripcionFinal()
        inscripcionfinal.alumno = request.user
        inscripcionfinal.materia = Materia.objects.get(pk = kwargs['pk'])
        #inscripcionfinal.mesa = request.POST['kwargs']
        cpu = random.choice(range(10000))
        materia = inscripcionfinal.materia
        numero = cpu , materia
        inscripcionfinal.cod_inscripcion = numero
        inscripcionfinal.save()
        return redirect('/inscripcion-materias')


#Muestra lista de materias para inscribirse a cursar
class MateriaCreateView(LoginRequiredMixin, CreateView):

    model = InscripcionMateria
    success_url = '/index'

    def get_context_data(self, **kwargs):

        context = super(MateriaCreateView, self).get_context_data(**kwargs)
        carrera = Carrera.objects.get(alumno__in = [self.request.user])
        context['total_materias'] = Materia.objects.filter(carrera = carrera)
        return context
        #materias = Materia.objects.filter(carrera = carrera)
        #context['total_materias'] = materias

#Muestra el detalle de las materias a inscribirse a cursar
class MateriaDetailView(LoginRequiredMixin, DetailView):

    model = Materia
    form_class = MateriaForm
    context_object_name = 'materia'

    def post(self, request, *args, **kwargs):


        inscripcion = InscripcionMateria()

        if inscripcion.regular == False:
            inscripcion.alumno = request.user
            inscripcion.materia = Materia.objects.get(pk = kwargs['pk'])
            inscripcion.regular = 'True'
            inscripcion.save()
            return redirect('/inscripcion-materias')

class BedelView(LoginRequiredMixin, TemplateView):

    template_name = 'bedel/menu_bedel.html'


class FinalDeleteView(LoginRequiredMixin, DeleteView):

    model = InscripcionFinal
    success_url = '/inscripcion-finales'

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

