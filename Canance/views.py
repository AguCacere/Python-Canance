from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from .models import Cursos
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.views import LogoutView
from django.urls import reverse
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'base.html')

def home(request):
    cursos = Cursos.objects.all()
    return render(request, "gestion_cursos.html", {"cursos": cursos})

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    precio = request.POST['numPrecio']
    curso = Cursos.objects.create(codigo=codigo, nombre=nombre, precio=precio)
    return redirect('/')

def eliminarCurso(request, codigo):
    curso = Cursos.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')

def edicionCurso(request, codigo):
    curso = Cursos.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    precio = request.POST['numPrecio']
    curso = Cursos.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.precio = precio
    curso.save()
    return redirect('/')



def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    precio=request.POST['numPrecio']
    curso = Cursos.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.precio = precio
    curso.save()
    return redirect('/')

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            messages.error(request, 'Contraseña o nombre de usuario incorrecto.')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro Exitoso.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


class CustomLogoutView(LogoutView):
    next_page = 'login'