from django.shortcuts import render
from BlogApp.forms import AutorForm, AgregarForm, BusquedaForm, PosteoForm
from BlogApp.models import Posteo, Agregar, Autor


# Create your views here.
def inicio(request):
    return render(request, "BlogApp/index.html")

def agregar_posteo(request):
    if request.method == 'POST':

        miFormulario = AutorForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            autores = Autor(
            usuario=informacion["usuario"],
            biografia=informacion['biografia']
            )
            autores.save()
        return render(request, 'BlogApp/index.html')
    else:
        miFormulario= AutorForm() 
    
    return render(request, 'BlogApp/about.html', {'autor': miFormulario})
    
    
def detalle_post(request):
    comentarios = Autor.objects.all()
    return render(request, 'BlogApp/sobre.html', {'comentario':comentarios})

def listar_posteo(request):
    posts = Posteo.objects.all()
    return render(request, 'BlogApp/post.html', {'posts': posts})
    

def formulario1(request):
    if request.method == 'POST':

        miFormulario= AgregarForm(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nuevo = Agregar(
            autor=informacion['autor'],
            contenido=informacion['contenido']
            )
            nuevo.save()
        return render(request, 'BlogApp/index.html')
    
    else:
        miFormulario= AgregarForm()
 
    return render(request, "BlogApp/formulario.html", {"formu": miFormulario})

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