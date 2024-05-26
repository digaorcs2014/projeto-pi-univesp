

from django.urls import path
from app_lojaferragens import views

urlpatterns = [
    path('',views.home, name='home'),
    path('fornecedores/',views.fornecedores, name='fornecedores'),
    path('produtos/',views.produtos, name='produtos'),
    path('vendas/',views.vendas, name='vendas'),
    path('clientes/',views.clientes, name='clientes'),
    path('usuarios/',views.usuarios, name='usuarios'),
    path('listar_produtos/',views.listar_produtos, name='listar_produtos'),
]
