from django.contrib import admin
from .models import Carrera, Materia, Profesor, InscripcionFinal, MesaFinal, InscripcionMateria, HistorialAcademico

class MateriaAdmin(admin.ModelAdmin):

	list_display = ('nombre', 'carrera', 'duracion', 'cod_materia')
	ordering = ('cod_materia',)
	search_fields = ('nombre','cod_materia',)

class CarreraAdmin(admin.ModelAdmin):
	filter_horizontal = ('alumno',)
	list_display = ('nombre', 'duracion')
	search_fields = ('nombre',)

class HistorialAcademicoAdmin(admin.ModelAdmin):
	list_display = ('cod_acta', 'alumno')
	search_fields = ('cod_acta', )

class InscripcionFinalAdmin(admin.ModelAdmin):
	list_display = ('cod_inscripcion', 'alumno', 'materia', 'mesa')
	search_fields = ('cod_inscripcion', )

class MesaFinalAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'hora', 'materia', 'turno', 'cod_mesa')
	search_fields = ('cod_mesa', )	


admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Profesor)
admin.site.register(InscripcionFinal, InscripcionFinalAdmin)
admin.site.register(MesaFinal, MesaFinalAdmin)
admin.site.register(InscripcionMateria)
admin.site.register(HistorialAcademico, HistorialAcademicoAdmin)

