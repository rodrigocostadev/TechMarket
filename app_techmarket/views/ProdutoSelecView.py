

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout 
from app_techmarket.models.Produto import Produto
from app_techmarket.models.Compra import Compra
from app_techmarket.models.Movimentacao import Movimentacao
from app_techmarket.models import PerfilUsuario
import requests


def prod_selecionado_view(request, pk):

    produto = Produto.objects.get(id=pk)
    usuario = PerfilUsuario.objects.get(usuario=request.user)

    if request.method == 'POST':
        if 'compra_realizada' in request.POST:

            if usuario.saldo > produto.preco:

                usuario.saldo -= produto.preco

                # Envio de Saldo para registrar na API
                api_url = "http://localhost:8080/saldos/"
                payload = {
                    "usuario": str(usuario),
                    "saldo": str(usuario.saldo)
                }

                try:
                    # Cria registro de saldo do usuario na API
                    response = requests.post(api_url, json=payload)
                    if response.status_code == 201:
                        
                        usuario.save()

                        Compra.objects.create(
                            produto=produto,
                            usuario=request.user
                        )

                        Movimentacao.objects.create(
                            produto=produto,
                            usuario=request.user,
                            valor=produto.preco,
                            tipo_movimentacao="Compra"
                        )

                        messages.success(request, f"Compra realizada com sucesso!")
                        return redirect ('atualizar_saldo_view')

                    else:
                        print(f" Erro ao realizar a compra na API: {response.status_code}")
                        # print(response.text)
                    return redirect ('atualizar_saldo_view')
                except requests.exceptions.RequestException as e:
                    print(f" Falha ao conectar à API : {e}")

                

                messages.success(request, f"Compra realizada com sucesso!")
                return redirect ('home_view')
            
    else:        
        return render(request, 'produto_selecionado.html', {'produto': produto}) 




# def prod_selecionado_view(request, pk):

#     produto = Produto.objects.get(id=pk)
#     usuario = PerfilUsuario.objects.get(usuario=request.user)

#     if request.method == 'POST':
#         if 'compra_realizada' in request.POST:

#             if usuario.saldo > produto.preco:

#                 usuario.saldo -= produto.preco
#                 usuario.save()

#                 Compra.objects.create(
#                     produto=produto,
#                     usuario=request.user
#                 )

#                 Movimentacao.objects.create(
#                     produto=produto,
#                     usuario=request.user,
#                     valor=produto.preco,
#                     tipo_movimentacao="Compra"
#                 )

#                 messages.success(request, f"Compra realizada com sucesso!")
#                 return redirect ('home_view')
            
#             else:
#                 messages.error(request, f"Você não possui Saldo Suficiente.")
#                 return redirect ('home_view')
        
#     else:        
#         return render(request, 'produto_selecionado.html', {'produto': produto}) 