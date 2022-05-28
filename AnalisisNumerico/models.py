from django.db import models

# Create your models here.

class Metodo(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=250)
	imagen = models.ImageField(upload_to='movie/images/')
	url = models.URLField(blank=True)