from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
        return render(request, 'home.html')

# Create your views here.

def loginUser(request):
    pass


# El logout de la aplicación

def logoutUser(request):
    logout(request)
    messages.success(request, "Has cerrado sesión") # Al 
    return redirect('home')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username = username, password = password)
        return redirect('login')
    return render(request, 'registro.html', {})
    