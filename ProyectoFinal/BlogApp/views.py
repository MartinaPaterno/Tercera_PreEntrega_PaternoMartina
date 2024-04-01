from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from BlogApp.forms import AutorForm, BusquedaForm, TemaForm
from BlogApp.models import  Agregar, Autor, Tema
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from users.forms import *
from perfil.models import Avatar
from django.views.generic import DeleteView, UpdateView

# Create your views here.
def inicio(request):
    try: 
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, 'BlogApp/index.html', {'url': avatar.imagen.url})
    except:
        return render(request, "BlogApp/index.html")


def AboutMe(request):
    return render(request, "BlogApp/about.html")

@login_required
def agregar_posteo(request):
    if request.method == 'POST':

        miFormulario = AutorForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            autores = Autor(
            usuario=informacion.POST["usuario"],
            biografia=informacion.POST['biografia']
            )
            autores.save()
            return render(request, 'BlogApp/index.html', {'mensaje': "Posteo agregado con éxito."})
        else:
            return render(request, "BlogApp/index.html", {'mensaje': "Error en el formulario."}) 
    
    else:
        miFormulario= AutorForm()
        return render(request, 'BlogApp/post.html', {'miFormulario': miFormulario})

@login_required
def crear_tema(request):
    tema = Tema.objects.all()
    if request.method == 'POST':
        form = TemaForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            
            tema = Tema(
                titulo=info["titulo"],
                descripcion=info["descripcion"],
                creador=info["creador"]
            )    
            tema.save()
            return render(request, "BlogApp/post.html")
    else:
        form = TemaForm()
    return render(request, 'BlogApp/crear_tema.html', {'form': form})    

@login_required
class EliminarPost(DeleteView):
    model = Tema
    template_name = 'BlogApp/eliminar.html'
    success_url = 'BlogApp/index.html'

@login_required
class PostUpdateView(UpdateView):
    model = Tema
    template_name = 'BlogApp/foro.html'
    fields = ['titulo', 'contenido']  
    success_url = reverse_lazy('BlogApp/index.html')

@login_required
def lista_posteo(request):
    temas = Tema.objects.all()
    return render(request, 'BlogApp/foro.html', {'temas': temas})

@login_required
def detalle_posteo(request):

      blog = Tema.objects.all() 

      contexto= {"blog":blog} 

      return render(request, "BlogApp/foro.html",contexto)


def buscar(request):
    if request.method == 'POST':
        miFormulario = BusquedaForm(request.POST)
        if miFormulario.is_valid():
            info= miFormulario.cleaned_data
            buscar2 = Agregar.objects.filter(autor__icontains=info["autor"])

        return render (request, 'BlogApp/buscar.html', {'posteos': buscar2})
    else:
        miFormulario = BusquedaForm()
    return render(request, 'BlogApp/buscar.html', {'form': miFormulario})