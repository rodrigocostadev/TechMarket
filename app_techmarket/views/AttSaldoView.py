
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout 
from app_techmarket.models import PerfilUsuario
from app_techmarket.models.Movimentacao import Movimentacao
from decimal import Decimal


def atualizar_saldo_view(request):

    usuario = PerfilUsuario.objects.get(usuario=request.user)

    if request.method == 'POST':

        if 'depositar' in request.POST:

            deposito = Decimal(request.POST.get('depositar'))
            usuario.saldo += deposito
            usuario.save()

            Movimentacao.objects.create(
                usuario=request.user,
                valor=deposito,
                tipo_movimentacao="Deposito"
            )

            messages.success(request, f"Depósito de R$ {deposito} realizado com sucesso!")
            return redirect ('atualizar_saldo_view')

        if 'sacar' in request.POST:

            saque = Decimal(request.POST.get('sacar'))
            usuario.saldo -= saque

            if usuario.saldo > 0:
                usuario.save()

                Movimentacao.objects.create(
                    usuario=request.user,
                    valor=saque,
                    tipo_movimentacao="Saque"
                )

                messages.success(request, f"Saque de R$ {saque} realizado com sucesso!")
                return redirect ('atualizar_saldo_view')
            
            else:
                messages.error(request, f"Saldo Indisponivel")
                return redirect ('atualizar_saldo_view')

    else:
        
        return render(request, 'atualizar_saldo.html', {'usuario': usuario}) 