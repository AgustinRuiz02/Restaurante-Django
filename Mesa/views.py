from django.shortcuts import render, redirect
from .forms import mesaForm
from .models import Mesa

# Create your views here.

def mesaHome(request):
    return render(request, 'Mesa/mesa.html')

def mesaNueva(request):
    formNuevo = mesaForm

    contexto = {
        'form': formNuevo,
        'mensaje':'Crear Mesa'
    }

    if request.method == 'POST':
        formPOST = mesaForm(request.POST)

        if formPOST.is_valid():
            formPOST.save()
            return redirect('listaMesas')
        else:
            contexto['mensaje']+='Error en el formulario'
            contexto['form'] = formPOST
    else:
        return render(request, 'Mesa/formMesa.html', contexto)
    
def listaMesas(request):
    mesas = Mesa.objects.all()

    contexto = {
        'titulo':'Lista de Mesas',
        'mesas':mesas
    }

    return render(request, 'Mesa/listaMesas.html', contexto)

