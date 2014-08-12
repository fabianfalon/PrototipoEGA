from django.db import models
from apps.alumno.models import User


class Carrera(models.Model):

	cod_carrera = models.CharField(max_length=50)
	nombre = models.CharField(max_length=500)
	resolucion = models.CharField(max_length=500, blank=True, null=True)
	duracion = models.IntegerField()
	alumno = models.ManyToManyField(User)

	def __unicode__(self):
		
		return self.nombre


class Materia(models.Model):

	cod_materia = models.CharField(max_length=50)
	nombre = models.CharField(max_length=500)
	carrera = models.ForeignKey(Carrera)
	duracion = models.CharField(max_length=25)
	anio = models.IntegerField()
	correlativa = models.ManyToManyField('Materia', blank=True, null=True)

	def __unicode__(self):
		return self.nombre


class Profesor(models.Model):

	nombre = models.CharField(max_length=500)
	materia = models.ForeignKey(Materia)

	def __unicode__(self):
		return self.nombre


class MesaFinal(models.Model):

	fecha = models.DateField()
	hora = models.TimeField(blank=True, null=True) 
	materia = models.ForeignKey(Materia)
	turno = models.CharField(max_length=100)
	cod_mesa = models.CharField(max_length=50)

	def __unicode__(self):
		return self.turno


from apps.alumno.models import User


class InscripcionMateria(models.Model):

	alumno= models.ForeignKey(User)
	materia = models.ForeignKey(Materia)
	regular = models.BooleanField(default=False)


class InscripcionFinal(models.Model):

	cod_inscripcion = models.CharField(max_length=60,  unique=True)
	alumno = models.ForeignKey(User)
	materia = models.ForeignKey(Materia)
	mesa = models.ForeignKey(MesaFinal)

	def __unicode__(self):
		return self.cod_inscripcion


class HistorialAcademico(models.Model):

	alumno = models.ForeignKey(User)
	materia = models.ForeignKey(Materia)
	nota = models.IntegerField()
	fecha = models.DateField()
	cod_acta = models.CharField(max_length=50)
	def __unicode__(self):
		return self.cod_acta
	 
# isncripcion = InscripcionFinal.objects.filter(user = request.user )
# inscripcion.materia
# inscripcion.materia.carrera