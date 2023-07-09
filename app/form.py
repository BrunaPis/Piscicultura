from django.forms import ModelForm
from app.models import Piscicultores, Peixes, Racao
from app.models import Viveiros
# Create the form class.
class PiscicultoresForm(ModelForm):
    class Meta:
        model =Piscicultores
        fields = ['piscicultor','rg','contato']

class ViveirosForm2(ModelForm):
     class Meta:
        model =Viveiros
        fields = ['biomassaViveiro', 'dataIniciar', 'mortalidade', 'dataRetirada', 'numeroViveiro', 'temperatura', 'largura_M', 'ganhoViveiro', 'ladoMenor_M', 'pH_daAgua', 'amostragemViveiro', 'numeroPeixesViveiro']


class PeixesForm(ModelForm):
    class Meta:
        model =Peixes
        fields = ['especie','pesoMedioPeixe_kg']

class RacaoForm(ModelForm):
    class Meta:
        model =Racao
        fields = ['quantidaderacaokg','marcaracao','precoracao','protreinabruta']