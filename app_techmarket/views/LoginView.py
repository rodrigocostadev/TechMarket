from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout 

def login_user(request):
    if request.method == "POST":
        username = request.POST['usuario']
        password = request.POST['senha']
        
        user = authenticate(
            request,
            username = username,
            password = password
        )
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Realizado com Sucesso!')
            return redirect('home_view')
        else:
            messages.error(request, 'Informações de Login Incorretas.')
            return redirect('login')
        
    return render(request, 'login.html') 