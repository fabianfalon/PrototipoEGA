from django.db import models
from apps.alumno.models import User



class Carrera(models.Model):

	cod_carrera = models.IntegerField()
	nombre = models.CharField(max_length=500)
	resolucion = models.CharField(max_length=500, blank=True, null=True)
	duracion = models.IntegerField()

	def __unicode__(self):
		return self.nombre


class Materia(models.Model):

	cod_materia = models.IntegerField()
	nombre = models.CharField(max_length=500)
	carrera = models.ForeignKey(Carrera)
	duracion = models.CharField(max_length=25)


	def __unicode__(self):
		return self.nombre

class Profesor(models.Model):

	nombre = models.CharField(max_length=500)
	materia = models.ForeignKey(Materia)

	def __unicode__(self):
		return self.nombre

class InscripcionFinal(models.Model):

	cod_inscripcion = models.IntegerField(unique=True)
	carrera = models.ForeignKey(Carrera)
	materia = models.ForeignKey(Materia)
	alumno = models.ForeignKey(User)
	profesor = models.ForeignKey(Profesor)
	fecha = models.DateField(auto_now_add=True)




class Reglascorrelatividades(models.Model):

	carrera = models.ForeignKey(Carrera)
	materiacursar = models.ForeignKey(Materia)

	def __unicode__(self):
		return self.carreracursar