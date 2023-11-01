from django.shortcuts import render, redirect
from .forms import ordenForm
from .models import Orden

# Create your views here.

def ordenHome(request):
    return render(request, 'Orden/orden.html')

def ordenNueva(request):
    formNuevo = ordenForm

    contexto = {
        'form': formNuevo,
        'mensaje':'Crear Orden'
    }

    if request.method == 'POST':
        formPOST = ordenForm(request.POST)

        if formPOST.is_valid():
            formPOST.save()
            return redirect('listaOrdenes')
        else:
            contexto['mensaje']+='Error en el formulario'
            contexto['form'] = formPOST
    else:
        return render(request, 'Orden/formOrden.html', contexto)
    
def listaOrdenes(request):
    ordenes = Orden.objects.all()

    contexto = {
        'titulo':'Lista de Ordenes',
        'ordenes':ordenes
    }

    return render(request, 'Orden/listaOrdenes.html', contexto)
