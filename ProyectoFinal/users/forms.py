from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class AuthenticationForm(AuthenticationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'autofocus': True}))
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class UserRegisterForm(UserCreationForm): 
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        help_text = {k: "" for k in fields}


