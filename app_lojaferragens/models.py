from django.db import models


class Usuario (models.Model):
    id = models.AutoField(primary_key=True, null= False, auto_created= True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    
class Fornecedor (models.Model):
    id = models.AutoField(primary_key=True, null= False, auto_created= True)
    nome = models.TextField(max_length=255, null= False)
    cnpj_cpf= models.TextField(max_length=15, null= False)
    contato = models.TextField(max_length=100, null= True)
    endereco = models.TextField(max_length=255, null= True)
    classificacao_preco = models.TextField(max_length=45, null= True)
    classificacao_tempo = models.TextField(max_length=45, null= True)
    classificacao_qualidade = models.TextField(max_length=45, null= True)

class Categoria (models.Model):
    id = models.AutoField(primary_key=True, null= False, auto_created= True)
    nome = models.TextField(max_length=255, null= False)

class Sub_Categoria (models.Model):
    id = models.AutoField(primary_key=True, null= False, auto_created= True)
    nome = models.TextField(max_length=255, null= False)
    categoria = models.ForeignKey(Categoria, on_delete= models.DO_NOTHING)

class Produto (models.Model):
    id = models.AutoField(primary_key=True, null= False, auto_created= True)
    nome = models.TextField(max_length=255, null= True)
    descricao = models.TextField(max_length=255, null= True)
    preco_venda = models.DecimalField(max_digits=6, decimal_places=2, null= True)
    custo = models.DecimalField(max_digits=6, decimal_places=2, null= True)
    imagem = models.TextField(max_length=255, null= True)
    manual_instrucao = models.TextField(max_length=255, null= True)
    classificacao = models.TextField(max_length=255, null= True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete= models.DO_NOTHING)
    categoria = models.ForeignKey(Categoria, on_delete= models.DO_NOTHING)
    sub_categoria = models.ForeignKey(Sub_Categoria, on_delete= models.DO_NOTHING)

class Estoque (models.Model):
    id = models.AutoField(primary_key=True, null= False, auto_created= True)
    produto = models.ForeignKey(Produto, on_delete= models.DO_NOTHING)
    quantidade = models.IntegerField(null= True)
    localizacao = models.TextField(max_length=255, null= True)
    data_entrada = models.DateField(auto_now_add= True)

class Alerta (models.Model):
    id = models.AutoField(primary_key=True, null= False, auto_created= True)
    descricao = models.TextField(max_length=255, null= True)
    tipo = models.TextField(max_length=255, null= True)
    data_alerta = models.DateField(auto_now_add= True) 
    estoque = models.ForeignKey(Estoque, on_delete= models.DO_NOTHING)

class Registro_Historico (models.Model):
    id = models.AutoField(primary_key=True, null= False, auto_created= True)
    descricao = models.TextField(max_length=255, null= True)
    tipo = models.TextField(max_length=255, null= True)
    detalhes = models.TextField(max_length=255, null= True)
    data_registro = models.DateField(auto_now_add= True) 

class Cliente (models.Model):
    id = models.AutoField(primary_key=True, null= False, auto_created= True)
    nome = models.TextField(max_length=255, null= True)
    email = models.TextField(max_length=255, null= True)
    telefone = models.TextField(max_length=255, null= True)
    endereco = models.TextField(max_length=255, null= True)
    
class Venda (models.Model):
    id = models.AutoField(primary_key=True, null= False, auto_created= True)
    cliente = models.ForeignKey(Cliente, on_delete= models.DO_NOTHING)
    data_venda = models.DateField(auto_now_add= True)
    tipo = models.TextField(max_length=255, null= True)
    valor_total = models.DecimalField(max_digits=6, decimal_places=2, null= True)

class Itens_Venda (models.Model):
    id = models.AutoField(primary_key=True, null= False, auto_created= True)
    venda = models.ForeignKey(Venda, on_delete= models.DO_NOTHING)
    produto = models.ForeignKey(Produto, on_delete= models.DO_NOTHING)
    quantidade_vendida = models.IntegerField(null= True)
    preco_unitario = models.DecimalField(max_digits=6, decimal_places=2, null= True)
    total_item_venda = models.DecimalField(max_digits=6, decimal_places=2, null= True)

class Fracionamento (models.Model):
    id = models.AutoField(primary_key=True, null= False, auto_created= True)
    produto = models.ForeignKey(Produto, on_delete= models.DO_NOTHING)
    quantidade_fracionada = models.IntegerField(null= True)
    data_fracionamento = models.DateField(auto_now_add= True)
    fracionamentocol = models.TextField(max_length=255, null= True)

class Compra (models.Model):
    id = models.AutoField(primary_key=True, null= False, auto_created= True)
    data_compra = models.DateField(auto_now_add= True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete= models.DO_NOTHING)
    valor_total = models.DecimalField(max_digits=6, decimal_places=2, null= True)

class Itens_Compra (models.Model):
    id = models.AutoField(primary_key=True, null= False, auto_created= True)
    compra = models.ForeignKey(Compra, on_delete= models.DO_NOTHING)
    produto = models.ForeignKey(Produto, on_delete= models.DO_NOTHING)
    quantidade = models.IntegerField(null= True)
    preco_lote = models.DecimalField(max_digits=6, decimal_places=2, null= True)
    preco_unitario = models.DecimalField(max_digits=6, decimal_places=2, null= True)
    unidade_medida = models.TextField(max_length=255, null= True)
      
 