from django.shortcuts import render
from .models import Datos_Usuario
from .forms import DatosForm
# Create your views here.

def home(request):
    data = {
        'Datos_Form': DatosForm(),
    }
    if request.method == 'POST':
        formulario = DatosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Solicituda Enviada Exitosamente"
        else:
            data["form"] = formulario
    return render(request, 'FormModule/home.html', data)

def datos(request):
    Datos_DB = Datos_Usuario.objects.all()
    data = {
        'Datos_Clientes': Datos_DB,
    }
    return render(request, 'FormModule/datos.html', data)


