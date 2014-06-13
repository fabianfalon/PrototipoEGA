from django.db import models


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



class Reglascorrelatividades(models.Model):

	carreracursar = models.ForeignKey(Carrera)
	materiacursar = models.ForeignKey(Materia)

	def __unicode__(self):
		return self.carreracursar