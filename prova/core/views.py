from django.shortcuts import render
from .models import PalestraModel, AlunoModel
from .forms import AlunoForm


def alunos(request):
    todos_alunos = AlunoModel.objects.all()
    alunos = {'alunos': todos_alunos}
    return render(request, "alunos.html", alunos)

def cadastrar(request):
    if request.method == 'POST':
        
        form = AlunoForm(request.POST)
        if form.is_valid():
            AlunoModel.objects.create(**form.cleaned_data)   
            contexto = {}
            return render(request, 'index.html', contexto) 
        else:
            contexto = {'form': form}
            return render(request, 'cadastrar.html', contexto)
    else:
        form = AlunoForm()
        contexto = {'form': form}
        return render(request, 'cadastrar.html', contexto)
    
def index(request):
    todas_palestras = PalestraModel.objects.all()
    palestras = {'palestras': todas_palestras}
    return render(request, "index.html", palestras)