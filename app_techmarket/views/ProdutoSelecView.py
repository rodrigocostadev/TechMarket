

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout 
from app_techmarket.models.Produto import Produto

def prod_selecionado_view(request, pk):

    produto = Produto.objects.get(id=pk)
        
    return render(request, 'produto_selecionado.html', {'produto': produto}) 