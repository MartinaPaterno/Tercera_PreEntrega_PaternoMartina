from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('addAvatar', agregar_avatar, name='AgregarAvatar'),
    path('verAvatar', ver_avatar, name="VerAvatar"),
    path('elimAvatar/<int:id>', eliminar_avatar, name="EliminarAvatar"),
    path('editPerfil', editar_perfil, name="EditarPerfil"),
    path('verPerfil', ver_perfil, name="VerPerfil"),
]