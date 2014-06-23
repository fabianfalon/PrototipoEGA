import random
from django.shortcuts import redirect
from braces.views import LoginRequiredMixin
from django.views.generic import FormView, CreateView, DetailView
from .models import Materia, User, InscripcionFinal, InscripcionMateria, Carrera
from .forms import FinalForm, MateriaForm


class FinalCreateView(LoginRequiredMixin, CreateView):

    model = InscripcionFinal
    form_class = FinalForm
    cod_alumno = ""
    alumno = ""
    materia = ""
    mesa =""
    carrera = ""
    success_url = '/index'

    numero =  random.randint (1, 20)

    def form_valid(self, form):

        cod_inscripcion = form.cleaned_data['cod_inscripcion']
        alumno = form.cleaned_data['alumno']
        materia = form.cleaned_data['materia']
        mesa = form.cleaned_data['mesa']
        form.save()
        return super(FinalCreateView, self).form_valid(form)

    def form_invalid(self, form):
        
        return super(FinalCreateView, self).form_invalid(form)



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

class MateriaDetailView(LoginRequiredMixin, DetailView):

    model = Materia
    form_class = MateriaForm
    context_object_name = 'materia'

    def post(self, request, *args, **kwargs):

        inscripcion = InscripcionMateria()
        inscripcion.alumno = request.user
        inscripcion.materia = Materia.objects.get(pk = kwargs['pk'])
        inscripcion.save()
        return redirect('/inscripcion-materias')

