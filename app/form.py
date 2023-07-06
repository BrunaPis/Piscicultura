from django.forms import ModelForm
from app.models import Piscicultores

# Create the form class.
class PiscicultoresForm(ModelForm):
    class Meta:
        model =Piscicultores
        fields = ['piscicultor','rg','contato']