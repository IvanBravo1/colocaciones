from django.db import models
from django.utils import timezone

class Desocupado(models.Model):
    nombre =  models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=200)
    numTelefono = models.CharField(max_length=200)
    descripcion =  models.CharField(max_length=200)
    edad = models.IntegerField
    fechaNac = models.DateField(auto_now=False)

    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre =  models.CharField(max_length=200)
    contacto =  models.CharField(max_length=200)
    tipoEmpresa =  models.CharField(max_length=200)
    descripcion =  models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Ofertas(models.Model):
    cargo =  models.CharField(max_length=200)
    trabajo =  models.CharField(max_length=200)
    horarios =  models.CharField(max_length=200)
    profesion =  models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre



