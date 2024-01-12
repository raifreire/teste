from django.urls import path
from . import views

urlpatterns = [
    path('',views.alunoView, name='alunos_list'),
    path('alunoID/<int:id>',views.alunoIDview, name='aluno-detalhe'),
    path('contato',views.contactView, name='contato'),
]
