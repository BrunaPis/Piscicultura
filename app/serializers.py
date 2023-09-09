from .models import Piscicultores, Viveiros,Peixes,Racao
from rest_framework import serializers

class PiscicultoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piscicultores
        fields = ['nome', 'rg', 'cep','cidade','contato', 'senha']

class ViveirosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viveiros
        fields = ['biomassaViveiro', 'dataIniciar', 'mortalidade', 'dataRetirada', 'numeroViveiro', 'temperatura', 'largura_M', 'ganhoViveiro', 'ladoMenor_M', 'pH_daAgua', 'amostragemViveiro', 'numeroPeixesViveiro']


class PeixesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peixes
        fields = ['especie', 'pesoMedioPeixe_kg']


class RacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Racao
        fields = ['quantidaderacaokg','marcaracao','precoracao','protreinabruta']
