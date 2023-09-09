from rest_framework import viewsets
from .serializers import PiscicultoresSerializer,ViveirosSerializer,PeixesSerializer,RacaoSerializer
from .models import Piscicultores,Viveiros,Peixes,Racao

class PiscicultoresViewSet(viewsets.ModelViewSet):
    model = Piscicultores
    serializer_class = PiscicultoresSerializer
    queryset = Piscicultores.objects.all()
    filter_fields = ('nome', 'rg', 'cep','cidade','contato', 'senha')

class ViveirosViewSet(viewsets.ModelViewSet):
    model = Viveiros
    serializer_class = ViveirosSerializer
    queryset = Viveiros.objects.all()
    filter_fields = ('biomassaViveiro', 'dataIniciar', 'mortalidade', 'dataRetirada', 'numeroViveiro', 'temperatura', 'largura_M', 'ganhoViveiro', 'ladoMenor_M', 'pH_daAgua', 'amostragemViveiro', 'numeroPeixesViveiro')

class PeixesViewSet(viewsets.ModelViewSet):
    model = Peixes
    serializer_class =  PeixesSerializer
    queryset = Peixes.objects.all()
    filter_fields = ('especie','pesoMedioPeixe_kg')


class RacaoViewSet(viewsets.ModelViewSet):
    model = Racao
    serializer_class =  RacaoSerializer
    queryset = Racao.objects.all()
    filter_fields = ('quantidaderacaokg','marcaracao','precoracao','protreinabruta')
