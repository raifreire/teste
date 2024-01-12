from django.shortcuts import render,get_object_or_404
from .models import Aluno

def alunoView(request):
    alunos_list = Aluno.objects.all
    # return HttpResponse('exibindo os alunos')
    return render(request, 'main/alunos.html',{'alunos_list':alunos_list})

def alunoIDview(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    print(aluno)
    return render(request,'main/alunoID.html',{'aluno': aluno})    


def contactView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print('Nome: '+name, ' Email: '+email, 'Mensagem: '+message)
    return render(request, 'main/contact.html')