from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from users.forms import UserRegisterForm

# Create your views here.

def login_request(request):
    msg_login = ""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contrasenia = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "AppCoder/index.html")
            
        msg_login = "Usuario o Contraseña incorrectos"
    
    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

def register(request):

    msg_register= ""
    if request.method=="POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppCoder/index.html", {"mensaje": "Usuario Creado!"})
        
        msg_register = "Error en los datos ingresados"
        
    else:
        form = UserRegisterForm()

    return render(request, "users/registro.html", {"form": form, "msg_register": msg_register})
