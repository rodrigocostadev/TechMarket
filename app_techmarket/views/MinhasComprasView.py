

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout 
from app_techmarket.models.Compra import Compra

def minhas_compras_view(request):

    compras_usuario = Compra.objects.filter(usuario=request.user).order_by('-data_hora')
        
    return render(request, 'minhas_compras.html', {'compras_usuario': compras_usuario}) 