from django.db import models

# Create your models here.

class Perro(models.Model):
    codigo = models.PositiveSmallIntegerField();
    nombre = models.CharField(max_length=15)
    tamano = models.FloatField()
    peso = models.FloatField()
    color = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    estado = models.BooleanField()

    def info(self):
        cadena = "{0} {1} {2}"
        return cadena.format(self.nombre, self.codigo, self.estado)

    def __str__(self):
        return self.info()

