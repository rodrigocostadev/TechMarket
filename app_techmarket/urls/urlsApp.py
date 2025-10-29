
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, static
from django.conf import settings
from app_techmarket.views.HomeView import home_view
from app_techmarket.views.LogoutView import logout_user
from app_techmarket.views.AttSaldoView import atualizar_saldo_view
from app_techmarket.views.CadastroUsuarioView import cadastro_view
from app_techmarket.views.ExtratoView import extrato_view
from app_techmarket.views.MinhasComprasView import minhas_compras_view
from app_techmarket.views.PerfilView import perfil_view
from app_techmarket.views.ProdutoSelecView import prod_selecionado_view



urlpatterns = [
    path("home/", home_view, name='home_view'),
    path("logout/", logout_user, name='logout'),
    path('atualizar_saldo/', atualizar_saldo_view, name="atualizar_saldo_view"),
    path('cadastro/', cadastro_view, name="cadastro_view"),
    path('extrato/', extrato_view, name="extrato_view"),
    path('minhas_compras/', minhas_compras_view, name="minhas_compras_view"),
    path('perfil/', perfil_view, name="perfil_view"),
    path('produto_selecionado/<int:pk>/', prod_selecionado_view, name="prod_selecionado_view"),
]