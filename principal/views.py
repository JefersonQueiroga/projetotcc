from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TrabalhoForm

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
    return render(request, 'principal/trabalho/form.html', {'form': form})