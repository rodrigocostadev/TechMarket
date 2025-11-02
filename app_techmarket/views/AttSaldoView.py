
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout 
from app_techmarket.models import PerfilUsuario
from app_techmarket.models.Movimentacao import Movimentacao
from decimal import Decimal
import requests



def atualizar_saldo_view(request):

    usuario = PerfilUsuario.objects.get(usuario=request.user)

    if request.method == 'POST':

        if 'depositar' in request.POST:

            deposito = Decimal(request.POST.get('depositar'))

            usuario.saldo += deposito

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

                    Movimentacao.objects.create(
                        usuario=request.user,
                        valor=deposito,
                        tipo_movimentacao="Deposito"
                    )

                    print(" Saldo criado com sucesso na API.")
                    messages.success(request, f"Deposito de R$ {deposito} realizado com sucesso!")
                    return redirect ('atualizar_saldo_view')

                else:
                    print(f" Erro ao criar saldo na API: {response.status_code}")
                    print(response.text)
                return redirect ('atualizar_saldo_view')
            except requests.exceptions.RequestException as e:
                print(f" Falha ao conectar à API de saldo: {e}")

            

            messages.success(request, f"Depósito de R$ {deposito} realizado com sucesso!")
            return redirect ('atualizar_saldo_view')

        if 'sacar' in request.POST:

            saque = Decimal(request.POST.get('sacar'))

            api_url_saldo_usuario = f"http://localhost:8080/saldos/{request.user.username}/"
            
            try:
                response = requests.get(api_url_saldo_usuario)
                print("API Response:", response.text)  # para debug

                if response.status_code == 200:
                    data = response.json()
                    saldo_api = Decimal(data.get('saldo'))

                    if saldo_api >= saque and  usuario.saldo > 0:
                        usuario.saldo -= saque
                        usuario.save()

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

                                Movimentacao.objects.create(
                                    usuario=request.user,
                                    valor=saque,
                                    tipo_movimentacao="Saque"
                                )

                                print(" Saldo criado com sucesso na API.")
                                messages.success(request, f"Saque de R$ {saque} realizado com sucesso!")
                                return redirect ('atualizar_saldo_view')

                            else:
                                print(f" Erro ao criar saldo na API: {response.status_code}")
                                print(response.text)
                            return redirect ('atualizar_saldo_view')
                        except requests.exceptions.RequestException as e:
                            print(f" Falha ao conectar à API de saldo: {e}")

                        # messages.success(request, f"Saque de R$ {saque} realizado com sucesso!")
                        # return redirect ('atualizar_saldo_view')
                    else:
                        messages.error(request, f"Saldo insuficiente (R$ {saldo_api}).")
                        return redirect ('atualizar_saldo_view')
                elif response.status_code == 404:
                    messages.error(request, "Usuário ou saldo não encontrado na API.")
                else:
                    messages.error(request, "Erro ao consultar o saldo na API.")
            except requests.exceptions.RequestException:
                messages.error(request, "Não foi possível conectar à API de saldo.")
            
            # else:
            #     messages.error(request, f"Saldo Indisponivel")
            #     return redirect ('atualizar_saldo_view')

            return redirect ('atualizar_saldo_view')

    else:
        
        return render(request, 'atualizar_saldo.html', {'usuario': usuario}) 
    





# def atualizar_saldo_view(request):

#     usuario = PerfilUsuario.objects.get(usuario=request.user)

#     if request.method == 'POST':

#         if 'depositar' in request.POST:

#             deposito = Decimal(request.POST.get('depositar'))
#             usuario.saldo += deposito
#             usuario.save()

#             Movimentacao.objects.create(
#                 usuario=request.user,
#                 valor=deposito,
#                 tipo_movimentacao="Deposito"
#             )

#             messages.success(request, f"Depósito de R$ {deposito} realizado com sucesso!")
#             return redirect ('atualizar_saldo_view')

#         if 'sacar' in request.POST:

#             saque = Decimal(request.POST.get('sacar'))
#             usuario.saldo -= saque

#             if usuario.saldo > 0:
#                 usuario.save()

#                 Movimentacao.objects.create(
#                     usuario=request.user,
#                     valor=saque,
#                     tipo_movimentacao="Saque"
#                 )

#                 messages.success(request, f"Saque de R$ {saque} realizado com sucesso!")
#                 return redirect ('atualizar_saldo_view')
            
#             else:
#                 messages.error(request, f"Saldo Indisponivel")
#                 return redirect ('atualizar_saldo_view')

#     else:
        
#         return render(request, 'atualizar_saldo.html', {'usuario': usuario}) 





