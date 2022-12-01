from django import forms

#criação dos forms
class AlunoForm(forms.Form):
    nome = forms.CharField(max_length=50)
    curso = forms.CharField(max_length=50)
    idade = forms.IntegerField()