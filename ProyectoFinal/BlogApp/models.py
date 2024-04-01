from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Autor(models.Model):
    usuario = models.CharField(max_length=40)
    biografia = models.TextField()

class Agregar(models.Model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField(max_length=100)
   
    def __str__(self):
        return f"Autor: {self.autor} | Blog: {self.contenido}"

class Posteo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField(max_length=200)

class Tema(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.creador} - {self.titulo} - {self.descripcion}"
    