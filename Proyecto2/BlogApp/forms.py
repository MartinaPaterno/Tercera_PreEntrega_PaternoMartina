from django import forms
from BlogApp.models import Posteo, Agregar, Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['usuario', 'biografia']


class AgregarForm(forms.ModelForm):
     class Meta:
        model = Agregar
        fields = ['autor', 'contenido']
    

class PosteoForm(forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ['titulo', 'contenido']

class BusquedaForm(forms.Form):
    autor = forms.CharField(max_length=20)