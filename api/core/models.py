from django.db import models


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=15)
    telefone = models.CharField(max_length=14)
    celular = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    dtnasc = models.DateField()
    cpf = models.CharField(max_length=15)
    rg = models.CharField(max_length=12)

    class Meta:
        db_table = "Cliente"

    def __str__(self):
        return str(self.id)


class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=80)
    bairro = models.CharField(max_length=80)
    numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    idcliente = models.ForeignKey(Cliente, related_name='enderecos', db_column='idcliente', on_delete=models.CASCADE)

    class Meta:
        db_table = "Endereco"

    def __str__(self):
        return self.rua
