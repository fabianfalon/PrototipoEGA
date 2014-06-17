from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
	list_display = ('nombre_apellido', 'username', 'cod_alumno', 'carrera', )
	ordering = ('nombre_apellido',)
	search_fields = ('nombre_apellido','carrera', 'username',)


admin.site.register(User, UserAdmin)