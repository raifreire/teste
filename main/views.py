from django.shortcuts import render
from .models import Aluno
from django.http import HttpResponse

def alunoView(request):
    alunos_list = Aluno.objects.all
    # return HttpResponse('exibindo os alunos')
    return render(request, 'main/alunos.html',{'alunos_list':alunos_list})
