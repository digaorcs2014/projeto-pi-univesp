from django.shortcuts import render
from .models import Usuario
from .models import Produto

def home(request):
    return render(request,'usuarios/home.html')

def fornecedores(request):
    return render(request,'fornecedores/fornecedores.html')

def produtos(request):
    return render(request,'produtos/produtos.html')

def vendas(request):
    return render(request,'vendas/vendas.html')

def clientes(request):
    return render(request,'clientes/clientes.html')

#salvar os daods da tela para o banco
def usuarios(request):
    # novo_usuario = Usuario()
    # novo_usuario.nome = request.POST.get('nome')
    # novo_usuario.idade = request.POST.get('idade')
    # novo_usuario.save()

    #exibir usuarios ja cadastrados em nova pagina 
    usuarios = {
           'usuarios' : Usuario.objects.all()
    }
    #retornar os dados para a pagina de listagem de usuarios 
    return render(request,'usuarios/usuarios.html',usuarios)

def listar_produtos(request):
    produtos = {
        'produtos' : Produto.objects.all()
    }
    return render(request,'produtos/listar_produtos.html', produtos)