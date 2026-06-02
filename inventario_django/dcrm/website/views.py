from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddRecordForm
from .models import Record

def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Bienvenido al CMR Credenciales correctas! 🙂😎😁")
            return redirect('home')
        else:
            messages.error(request, "Credenciales invalidas 😅🥲🫠")
            return redirect('home')
    else:
        if request.user.is_authenticated:
            records = Record.objects.all()
            return render(request, 'home.html', {'user': request.user, 'records': records})
        else:
            return render(request, 'home.html')

# Create your views here.

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = authenticate(request, username=username, password=password, email=email)
        if user is not None:
            login(request, user)
            messages.success(request, "Bienvenido al CRM. Credenciales correctas 🙂😎😁")
            return redirect('home')
        messages.error(request, "Credenciales inválidas 😅🥲🫠")
        return redirect('home')

    return redirect('home')


# El logout de la aplicación

def logoutUser(request):
    logout(request)
    messages.success(request, "Has cerrado sesión")
    return redirect('home')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe.")
            return redirect('register')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
        return redirect('home')

    return render(request, 'register.html', {})

def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "Registro eliminado exitosamente.")
        return redirect('home')
    else:
        messages.error(request, "Debes iniciar sesión para eliminar un registro.")
        return redirect('home')

def add_record(request):
    
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Registro agregado exitosamente.")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "Debes iniciar sesión para agregar un registro.")
        return redirect('home')