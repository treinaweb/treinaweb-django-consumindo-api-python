import requests
import json

from ..models import *
from ..encoder import MeuEncoder

def listar_tarefas():
    response = requests.get("http://localhost:3002/api/tarefas-django")
    tarefas = json.loads(response.content)
    return tarefas

def listar_tarefa_id(id):
    response = requests.get(f"http://localhost:3002/api/tarefas-django?id={id}")
    tarefa = json.loads(response.content)
    return tarefa

def remover_tarefa(id):
    requests.delete(f"http://localhost:3002/api/tarefas-django?id={id}")

def cadastrar_tarefa(tarefa):
    data = json.dumps(tarefa, cls=MeuEncoder)
    requests.post("http://localhost:3002/api/tarefas-django", data=data)

def editar_tarefa(tarefa_editada, id):
    data = json.dumps(tarefa_editada, cls=MeuEncoder)
    requests.put(f"http://localhost:3002/api/tarefas-django?id={id}", data=data)

