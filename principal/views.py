from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TrabalhoForm
from .models import Trabalho

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def teste(request):
    return render(request, 'principal/teste.html')


@login_required
def trabalho_novo(request):
    form = TrabalhoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save();
        return redirect('trabalho_list')

    return render(request, 'principal/trabalho/form.html', {'form': form})


# Método para realizar a edição
def editar_trabalho(request,id):
    trabalho = get_object_or_404(Trabalho, pk=id)
    form = TrabalhoForm(request.POST or None, request.FILES or None, instance=trabalho)

    if form.is_valid():
        form.save();
        return redirect('trabalho_list')

    print("Editarr----------");

    return render(request, 'principal/trabalho/form.html', {'form': form})



@login_required
def trabalho_list(request):
    trabalhos = Trabalho.objects.all()
    return render(request, 'principal/trabalho/lista.html', {'trabalhos': trabalhos})
