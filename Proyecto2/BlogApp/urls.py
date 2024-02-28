from django.urls import path
from BlogApp import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('about/', views.agregar_posteo, name="Agregar"),
    path('post/', views.listar_posteo, name="Blogs"),
    path('sobre/', views.detalle_post, name="Sobre"),
    path('buscar/', views.buscar, name="Buscar"),
    path('formu/', views.formulario1, name="Formulario")
    
]