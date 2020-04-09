from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Trabalho,Categoria


class TrabalhoForm(forms.ModelForm):
    titulo =forms.CharField(label='Nome:',
                       max_length=100,
                       widget=forms.TextInput(attrs={'class': 'form-control'}))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Trabalho
        fields = ('__all__')