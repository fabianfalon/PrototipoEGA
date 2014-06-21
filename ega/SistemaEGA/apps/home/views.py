import random
from django.shortcuts import render
from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView, FormView, CreateView, DetailView
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

    def form_valid(form, self):
        alumno = form.cleaned_data['self.request.user']
        materia = form.cleaned_data['tecnologia1']
        form.save()
        return super(MateriaDetailView, self).form_valid(form)

    def form_invalid(self, form):
        
        return super(MateriaDetailView, self).form_invalid(form)




# def guardar_inscripcion(request):

#     form_class = MateriaForm
#     alumno = ""
#     materia = ""
#     if request.method == 'POST':
#         formulario = MateriaForm(request.POST)
#         if formulario.is_valid():
#             alumno = formulario.cleaned_data['request.user']
#             materia = formulario.cleaned_data['']
#             return redirect('/create_materia')

#         else: 
#             formulario = MateriaForm()
#             ctx = {'form':formulario}
#             return render_to_response('home/materia_detail.html',ctx, context_instance=RequestContext(request))



       

