from django.db import models

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
 



