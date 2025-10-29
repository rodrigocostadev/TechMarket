
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout 
from app_techmarket.models.Produto import Produto

def home_view(request):

    lista_produtos = Produto.objects.all()
        
    return render(request, 'home.html', {'lista_produtos': lista_produtos}) 