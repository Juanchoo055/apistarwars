from django.db import models

# Create your models here.
class Personaje(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return '%s' %(self.nombre)

class planeta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return '%s' %(self.nombre)

class peliculas(models.Model):
    nombre = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    productores = models.CharField(max_length=50)
    texto_apertura = models.CharField(max_length=1000)
    personajes = models.ManyToManyField(Personaje)
    planetas = models.ManyToManyField(planeta)
    

    