from django.forms import ModelForm
from .models import Mesa

class mesaForm(ModelForm):
    class Meta:
        model = Mesa
        fields = '__all__'