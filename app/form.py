from django.forms import ModelForm
from app.models import Piscicultores
from app.models import Viveiros
from django import forms
# Create the form class.
from django import forms
from .models import Piscicultores,Peixes, Racao


class PiscicultoresForm(forms.ModelForm):
    class Meta:
        model = Piscicultores
        fields = ['nome', 'rg', 'contato', 'senha']  # Adicione 'senha' se ainda não estiver lá.


class ViveirosForm(ModelForm):
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





