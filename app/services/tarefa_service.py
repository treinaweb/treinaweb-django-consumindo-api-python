import requests
import json

from ..models import *

def listar_tarefas():
    response = requests.get("http://localhost:3002/api/tarefas-django")
    tarefas = json.loads(response.content)
    return tarefas

def listar_tarefa_id(id):
    tarefa = Tarefa.objects.get(id=id)
    return tarefa

def remover_tarefa(tarefa):
    tarefa.delete()

def cadastrar_tarefa(tarefa):
    Tarefa.objects.create(titulo=tarefa.titulo, descricao=tarefa.descricao)

def editar_tarefa(tarefa, tarefa_novo):
    tarefa.titulo = tarefa_novo.titulo
    tarefa.descricao = tarefa_novo.descricao
    tarefa.save(force_update=True)

