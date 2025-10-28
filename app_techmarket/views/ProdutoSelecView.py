

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout 

def prod_selecionado_view(request):
        
    return render(request, 'produto_selecionado.html') 