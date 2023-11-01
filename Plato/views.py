from django.shortcuts import render, redirect
from .forms import platoForm
from .models import Plato

# Create your views here.

def platoHome(request):
    return render(request, 'Plato/plato.html')

def platoNuevo(request):
    formNuevo = platoForm

    contexto = {
        'form': formNuevo,
        'mensaje':'Crear Plato'
    }

    if request.method == 'POST':
        formPOST = platoForm(request.POST)

        if formPOST.is_valid():
            formPOST.save()
            return redirect('listaPlatos')
        else:
            contexto['mensaje']+='Error en el formulario'
            contexto['form'] = formPOST
    else:
        return render(request, 'Plato/formPlato.html', contexto)
    
def listaPlatos(request):
    platos = Plato.objects.all()

    contexto = {
        'titulo':'Lista de Platos',
        'platos':platos
    }

    return render(request, 'Plato/listaPlatos.html', contexto)
