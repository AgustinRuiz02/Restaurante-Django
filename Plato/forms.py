from django.forms import ModelForm
from .models import Plato

class platoForm(ModelForm):
    class Meta:
        model = Plato
        fields = '__all__'