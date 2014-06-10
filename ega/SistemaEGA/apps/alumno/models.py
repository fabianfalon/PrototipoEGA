from django.db import models
from PIL import Image

class Carrera(models.Model):

	cod_materia = models.IntegerField()
	nombre = models.CharField(max_length=500)
	duracion = models.IntegerField()

	def __unicode__(self):
		return self.nombre

class Alumno(models.Model):

	cod_alumno = models.IntegerField(blank=True, null=True)
	carrera = models.ForeignKey(Carrera)
	nombre_apellido = models.CharField(max_length=800)
	dni = models.CharField(max_length=10)
	edad = models.IntegerField()
	lugar_nacimiento = models.CharField(max_length=500)
	fecha_nacimiento = models.DateField()
	ciudad_actual = models.CharField(max_length=500)
	domicilio_actial = models.CharField(max_length=500)
	usuario = models.CharField(max_length=500)
	email = models.EmailField()
	tipo_usuario = models.IntegerField(blank=True, null=True)
	documentacion_completa = models.BooleanField(default=False)
	fecha = models.DateField(auto_now=True, auto_now_add=True)
	imagen = models.ImageField(upload_to='alumnos/', blank=True, null=True)

	def __unicode__(self):
		return self.nombre_apellido





