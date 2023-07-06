from django.db import models

class Piscicultores(models.Model):
    piscicultor = models.CharField(max_length=30)
    rg = models.CharField(max_length=7)
    contato = models.CharField(max_length=13)