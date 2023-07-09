from django.db import models


class Piscicultores(models.Model):
    piscicultor = models.CharField(max_length=30)
    rg = models.CharField(max_length=7)
    contato = models.CharField(max_length=13)


class Viveiros(models.Model):
    biomassaViveiro = models.CharField(max_length=30)
    dataIniciar = models.CharField(max_length=30)
    mortalidade = models.CharField(max_length=30)
    dataRetirada = models.CharField(max_length=30)
    numeroViveiro = models.IntegerField()
    temperatura = models.CharField(max_length=30)
    largura_M = models.CharField(max_length=30)
    ganhoViveiro = models.CharField(max_length=30)
    ladoMenor_M = models.CharField(max_length=30)
    pH_daAgua = models.CharField(max_length=30)
    amostragemViveiro = models.CharField(max_length=30)
    numeroPeixesViveiro = models.IntegerField()


class Peixes(models.Model):
    especie = models.CharField(max_length=30)
    pesoMedioPeixe_kg = models.CharField(max_length=13)


class Racao(models.Model):
    quantidaderacaokg = models.CharField(max_length=30)
    marcaracao = models.CharField(max_length=30)
    precoracao = models.CharField(max_length=30)
    protreinabruta = models.CharField(max_length=30)