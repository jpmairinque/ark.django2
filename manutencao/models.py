from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class Empresa(models.Model):

    id = IntegerField(primary_key=True)
    tipo = IntegerField()
    nome = CharField(max_length=50)
    nome_fantasia = CharField(max_length=50)
    superior = CharField(max_length=50)
    cnpj = CharField(max_length=50)
    observacoes = CharField(max_length=50)
    contato = CharField(max_length=50)
    email = CharField(max_length=50)
    telefone2 = CharField(max_length=50)
    ramal2 = CharField(max_length=50)
    telefone1 = CharField(max_length=50)
    ramal1 = CharField(max_length=50)
    fax = CharField(max_length=50)
    cep = CharField(max_length=50)
    rua = CharField(max_length=50)
    numero = IntegerField()
    complemento = CharField(max_length=50)
    bairro = CharField(max_length=50)
    cidade = CharField(max_length=50)
    estado = CharField(max_length=50)