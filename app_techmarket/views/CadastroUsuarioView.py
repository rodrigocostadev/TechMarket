
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from app_techmarket.models import PerfilUsuario
from app_techmarket.models.Movimentacao import Movimentacao

def cadastro_view(request):

    if request.method == "POST":
        nome_completo = request.POST.get("nome_completo")
        cpf = request.POST.get("cpf")
        data_nascimento = request.POST.get("data_nascimento")
        numero_telefone = request.POST.get("telefone")
        usuario = request.POST.get("usuario")
        email = request.POST.get("email")
        senha1 = request.POST.get("senha1")
        senha2 = request.POST.get("senha2")
        saldo = request.POST.get("saldo")
        imagem = request.FILES.get("imagem")

        if senha1 != senha2:
            messages.error(request, "As senhas não coincidem.")
            return redirect('cadastro_view')

        if User.objects.filter(username=usuario).exists():
            messages.error(request, "Usuário já existe.")
            return redirect('cadastro_view')
        
        ano = data_nascimento.split("-")[0]
        mes = data_nascimento.split("-")[1]
        dia = data_nascimento.split("-")[2]

        data_nascimento = f"{dia}/{mes}/{ano}"

        novo_usuario = User.objects.create_user(
            username=usuario, 
            first_name=nome_completo.split(" ")[0],
            last_name=" ".join(nome_completo.split(" ")[1:]),
            email=email, 
            password=senha1,
        )

        PerfilUsuario.objects.create(
            usuario=novo_usuario, 
            saldo=saldo, 
            imagem=imagem,
            cpf=cpf,
            data_nascimento=data_nascimento,
            numero_telefone=numero_telefone,
        )

        Movimentacao.objects.create(
            usuario=novo_usuario,
            valor=saldo,
            tipo_movimentacao="Deposito"
        )

        messages.success(request, "Cadastro realizado com sucesso! Faça login para continuar.")
        return redirect('login')
        
    return render(request, 'cadastro_usuario.html') 