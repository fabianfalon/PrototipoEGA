from django.contrib import admin
from .models import Articulos

class ArticulosAdmin(admin.ModelAdmin):
	list_display = ('titulo' ,'resumen', 'cuerpo')
	ordering = ('titulo',)
	search_fields = ('titulo','resumen',)


admin.site.register(Articulos, ArticulosAdmin)


