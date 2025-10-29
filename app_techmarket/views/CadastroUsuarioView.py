
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from app_techmarket.models import PerfilUsuario

def cadastro_view(request):

    if request.method == "POST":
        usuario = request.POST.get("usuario")
        email = request.POST.get("email")
        senha1 = request.POST.get("senha1")
        senha2 = request.POST.get("senha2")
        saldo = request.POST.get("saldo")

        if senha1 != senha2:
            messages.error(request, "As senhas não coincidem.")
            return redirect('cadastro_view')

        if User.objects.filter(username=usuario).exists():
            messages.error(request, "Usuário já existe.")
            return redirect('cadastro_view')

        novo_usuario = User.objects.create_user(username=usuario, email=email, password=senha1)
        PerfilUsuario.objects.create(usuario=novo_usuario, saldo=saldo)

        messages.success(request, "Cadastro realizado com sucesso! Faça login para continuar.")
        return redirect('login')
        
    return render(request, 'cadastro_usuario.html') 