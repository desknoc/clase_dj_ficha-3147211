from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Esta es tu función Home que ya corregimos para evitar el bucle
def home(request):
    return render(request, 'home.html', {})

# Aquí es donde estaba el error. Asegúrate de que se llame EXACTAMENTE login_user
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "¡Sesión iniciada!")
            return redirect('home')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
            return redirect('login') # Asegúrate de tener una URL llamada 'login'
            
    return render(request, 'login.html', {}) # O el nombre de tu template de login

def logout_user(request):
    logout(request)
    messages.success(request, "Sesión cerrada.")
    return redirect('home')