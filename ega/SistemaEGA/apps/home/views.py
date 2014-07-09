import random
from django.shortcuts import redirect, HttpResponseRedirect, render
from braces.views import LoginRequiredMixin
from django.views.generic import FormView, CreateView, DetailView
from django.views.generic import TemplateView, DeleteView
from .models import Materia, User, InscripcionFinal
from .models import InscripcionMateria, Carrera, MesaFinal
from .forms import FinalForm, MateriaForm


#Mostrar lista de materias para rendir examen Final
class FinalCreateView(LoginRequiredMixin, CreateView):

    model = Materia

    def get_context_data(self, **kwargs):

        context = super(FinalCreateView, self).get_context_data(**kwargs)
        carrera = Carrera.objects.get(alumno__in = [self.request.user])
        context['total_materias_finales'] = Materia.objects.filter(carrera = carrera).order_by('anio')
        return context


#Muestra el detalle de la materia para inscribirse al examen final
class FinalDetailView(LoginRequiredMixin, DetailView):

    template_name = 'home/create_final.html'
    model = Materia
    form_class = FinalForm
    context_object_name = 'materia'

    def get_context_data(self, *args, **kwargs):

        mesa = MesaFinal()
        form_class = FinalForm()    
        context = super(FinalDetailView, self).get_context_data(**kwargs)
        context['mesa'] = MesaFinal.objects.filter(materia = context['object'])
        return context


    def post(self, request, *args, **kwargs): 

        inscripcionfinal = InscripcionFinal()
        inscripcionfinal.alumno = request.user#Guardamos el usuario que esta haciendo la peticion
        inscripcionfinal.materia = Materia.objects.get(pk = kwargs['pk'])#Buscamos la materia que sea igual pk pasada por parametro
        inscripcionfinal.mesa = MesaFinal.objects.get(fecha=request.POST['fecha'])#Filtramos mesa final segun la mesa que se paso por POST
        cpu = random.choice(range(100000))#Generamos numero aleatorio
        materia = inscripcionfinal.materia
        numero = cpu , inscripcionfinal.materia
        inscripcionfinal.cod_inscripcion = numero
        inscripcioncorrelativa = Materia.objects.filter(materia__pk = kwargs['pk'])
        #Consulta: Me trae una lista de materias correlativas de la materia en la que hice click
        validacion = InscripcionMateria.objects.filter(materia = inscripcioncorrelativa, alumno = inscripcionfinal.alumno)
        # Con el resultado de la consulta anterior preguntamos en InscripcionMateria si tenemos una inscripcion de ese tipo
        if validacion:
            inscripcionfinal.save()
            return redirect('/inscripcion-finales')
        else: 
            contexto = {
                       'inscripcioncorrelativa': inscripcioncorrelativa,
                        }
            return render(request, 'errores/error-inscripcion.html', contexto)


#Muestra lista de materias para inscribirse a cursar
class MateriaCreateView(LoginRequiredMixin, CreateView):

    model = InscripcionMateria
    success_url = '/index'

    def get_context_data(self, **kwargs):

        context = super(MateriaCreateView, self).get_context_data(**kwargs)
        carrera = Carrera.objects.get(alumno__in = [self.request.user])#Filtramos en la clase Carrera segun el usuario registrado
        context['total_materias'] = Materia.objects.filter(carrera = carrera).order_by('anio')#FIltramos las materias de esa carrera
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
        inscripcion.alumno = request.user
        inscripcion.materia = Materia.objects.get(pk = kwargs['pk'])
        inscripcioncorrelativa = Materia.objects.filter(materia__pk = kwargs['pk'])
        inscripcion.regular = True
        validacion = InscripcionMateria.objects.filter(materia = inscripcioncorrelativa, alumno = inscripcion.alumno)
        #validacionuser = InscripcionMateria.objects.get(alumno = inscripcion.alumno)
        if validacion:
            inscripcion.save()
            return redirect('/inscripcion-materias')
        else: 
            contexto = {
                       'inscripcioncorrelativa': inscripcioncorrelativa,
                        }
            return render(request, 'errores/error-inscripcion.html', contexto)


class ErrorInscripcionView(LoginRequiredMixin, TemplateView):

    template_name = 'errores/error-inscripcion.html'


class BedelView(LoginRequiredMixin, TemplateView):

    template_name = 'bedel/menu_bedel.html'


#Eliminar Final
class FinalDeleteView(LoginRequiredMixin, DeleteView):

    model = InscripcionFinal
    success_url = '/inscripcion-finales'

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


