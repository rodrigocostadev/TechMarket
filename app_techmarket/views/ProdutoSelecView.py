

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout 
from app_techmarket.models.Produto import Produto
from app_techmarket.models.Compra import Compra
from app_techmarket.models.Movimentacao import Movimentacao
from app_techmarket.models import PerfilUsuario

def prod_selecionado_view(request, pk):

    produto = Produto.objects.get(id=pk)
    usuario = PerfilUsuario.objects.get(usuario=request.user)

    if request.method == 'POST':
        if 'compra_realizada' in request.POST:

            usuario.saldo -= produto.preco
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
            return redirect ('home_view')
        
    else:        
        return render(request, 'produto_selecionado.html', {'produto': produto}) 