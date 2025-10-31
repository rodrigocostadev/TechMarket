
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout 
from app_techmarket.models.Movimentacao import Movimentacao

def extrato_view(request):

    movimentacoes_usuario = Movimentacao.objects.filter(usuario=request.user).order_by('-data_hora')
        
    return render(request, 'extrato.html', {'movimentacoes_usuario': movimentacoes_usuario}) 