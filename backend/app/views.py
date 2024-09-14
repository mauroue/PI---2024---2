from django.shortcuts import render, redirect
from .forms import TecnicoForm
from .models import Tecnico

def cadastro_tecnico(request):
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tecnicos')
    else:
        form = TecnicoForm()
    return render(request, 'tecnicos/cadastro.html', {'form': form})

def listar_tecnicos(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'tecnicos/listar.html', {'tecnicos': tecnicos})
