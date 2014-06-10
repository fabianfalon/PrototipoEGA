from django.contrib import admin
from .models import Carrera
from .models import Alumno



class AlumnoAdmin(admin.ModelAdmin):
	list_display = ('cod_alumno', 'nombre_apellido', 'dni', 'edad', 'carrera')
	list_filter = ('nombre_apellido', 'cod_alumno',)
	search_fields = ('cod_alumno','nombre_apellido',)



admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Carrera)