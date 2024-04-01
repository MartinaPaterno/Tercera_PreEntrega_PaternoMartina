from django.urls import path
from BlogApp import views
from .views import AboutMe

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('about/', AboutMe, name="About"),
    path('post/', views.agregar_posteo, name="AgregarBlog"),
    #path('sobre/', views.d, name="Post"),
    path('buscar/', views.buscar, name="Buscar"),
    path('crearTema/', views.crear_tema, name='CrearTema'),
    path('foro/', views.lista_posteo, name='Foro'),
    path('detalleTema/', views.detalle_posteo, name='DetalleTema'),
    path('post/<int:pk>/eliminar/', views.EliminarPost, name="EliminarTema"),
    path('post/<int:pk>/editar/', views.PostUpdateView, name="EditarTema")
    #path('formu/', views.formulario1, name="Formulario")
    
]