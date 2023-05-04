from .models import Aluno
from django.http import HttpResponse
from django.shortcuts import render

def alunoView(request):
    alunos_list = Aluno.objects.all()
    return render(request, 'main/alunos.html', {'aluno_list': alunos_list})