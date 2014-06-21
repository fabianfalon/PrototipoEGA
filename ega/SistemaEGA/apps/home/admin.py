from django.contrib import admin
from .models import Carrera, Materia, Profesor, InscripcionFinal, MesaFinal, InscripcionMateria, HistorialAcademico

class MateriaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'carrera', 'duracion', 'cod_materia')
	ordering = ('cod_materia',)
	search_fields = ('nombre','cod_materia',)

class CarreraAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'duracion')
	search_fields = ('nombre',)


admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Profesor)
admin.site.register(InscripcionFinal)
admin.site.register(MesaFinal)
admin.site.register(InscripcionMateria)
admin.site.register(HistorialAcademico)

