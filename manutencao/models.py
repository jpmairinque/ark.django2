from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class Company(models.Model):

    id = IntegerField(primary_key=True)
    tipo = IntegerField(null=True)
    nome = CharField(max_length=50, null=True)
    nome_fantasia = CharField(max_length=50, null=True)
    superior = CharField(max_length=50, null=True)
    cnpj = CharField(max_length=50, null=True)
    observacoes = CharField(max_length=50, null=True)
    contato = CharField(max_length=50, null=True)
    email = CharField(max_length=50, null=True)
    telefone2 = CharField(max_length=50, null=True)
    ramal2 = CharField(max_length=50, null=True)
    telefone1 = CharField(max_length=50, null=True)
    ramal1 = CharField(max_length=50, null=True)
    fax = CharField(max_length=50, null=True)
    cep = CharField(max_length=50, null=True)
    rua = CharField(max_length=50, null=True)
    numero = IntegerField(null=True)
    complemento = CharField(max_length=50, null=True)
    bairro = CharField(max_length=50, null=True)
    cidade = CharField(max_length=50, null=True)
    estado = CharField(max_length=50, null=True)

class Equipment(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    fabricante = models.CharField(max_length=100, null=True)
    modelo = models.CharField(max_length=100, null=True)
    patrimonio = models.CharField(max_length=100, null=True)
    numero_serie = models.CharField(max_length=100, null=True)
    proprietario = models.CharField(max_length=100, null=True)
    
   

    def __str__(self):
        return self.modelo

class Chamado(models.Model):
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    numero = models.IntegerField(null=True)
    equipamento_id = models.IntegerField()
    responsavel_str = models.CharField(max_length=100, null=True)
    proprietario_nome = models.CharField(max_length=50, null=True)
    proprietario_apelido = models.CharField(max_length=50, null=True)    
   

    def __str__(self):
        return self.id