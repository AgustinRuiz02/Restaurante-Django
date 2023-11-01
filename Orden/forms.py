from django.forms import ModelForm
from .models import Orden
from Plato.models import Plato

class ordenForm(ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'
