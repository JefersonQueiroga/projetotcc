from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Trabalho,Categoria,Curso,Professor

class TrabalhoForm(forms.ModelForm):
    titulo =forms.CharField(label='titulo:',
                       max_length=100,
                       widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao= forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':150}))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control col-md-7 col-xs-12', 'weight': '50%'}))
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control col-md-7 col-xs-12', 'weight': '50%'}))
    professores = forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple,
                       queryset = Professor.objects.all());


    class Meta:
        model = Trabalho
        fields = ('__all__')