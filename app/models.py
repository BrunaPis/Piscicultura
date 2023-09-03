from django.db import models

class Piscicultores(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=20)
    contato = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)


    def __str__(self):
        return self.rg

class Viveiros(models.Model):
    biomassaViveiro = models.CharField(max_length=100)
    dataIniciar = models.CharField(max_length=30)
    mortalidade = models.CharField(max_length=30)
    dataRetirada = models.CharField(max_length=30)
    numeroViveiro = models.CharField(max_length=30)
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
    def __str__(self):
        return self.especie


class Racao(models.Model):
    quantidaderacaokg = models.CharField(max_length=30)
    marcaracao = models.CharField(max_length=30)
    precoracao = models.CharField(max_length=30)
    protreinabruta = models.CharField(max_length=30)
