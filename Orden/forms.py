from django.forms import ModelForm
from .models import Orden

class ordenForm(ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'