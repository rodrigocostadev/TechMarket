

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout 
from app_techmarket.models import PerfilUsuario

def perfil_view(request):
        
    perfil = PerfilUsuario.objects.get(usuario=request.user)

    return render(request, 'perfil.html', {'perfil': perfil}) 