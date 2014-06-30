from django.db import models
from PIL import Image

class Articulos(models.Model):

	titulo = models.CharField(max_length=250)
	resumen = models.CharField(max_length=500)
	cuerpo = models.TextField()
	fecha = models.DateTimeField(auto_now_add = True)
	imagen = models.ImageField(upload_to='articulos/', blank=True, null=True)

	def __unicode__(self):

		return self.titulo

