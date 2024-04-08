from django.db import models

# Create your models here.
class Oficina (models.Model):
  nombre = models.CharField(max_length=100)
  abreviatura = models.CharField(max_length=100)
  def __str__(self):
    return self.nombre

class Usuario (models.Model):
  nombre = models.CharField(max_length=100)
  apellido = models.CharField(max_length=100)
  oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)
  def __str__(self):
    return '{} {}'.format(self.nombre, self.apellido)
