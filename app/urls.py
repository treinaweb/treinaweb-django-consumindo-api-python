from django.urls import path
from .views import *

urlpatterns = [
    path('listar', listar_tarefas, name="listar_tarefas"),
    path('cadastrar', inserir_tarefa, name="inserir_tarefa"),
    path('listar/<int:id>', listar_tarefa_id, name="listar_tarefa_id"),
    path('editar/<int:id>', editar_tarefa, name="editar_tarefa"),
    path('remover/<int:id>', remover_tarefa, name="remover_tarefa")
]
