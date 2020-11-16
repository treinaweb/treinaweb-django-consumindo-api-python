from django.shortcuts import render, redirect
from .forms import TarefaForm
from .entidades import tarefa
from .services import tarefa_service
# Create your views here.

def listar_tarefas(request):
    tarefas = tarefa_service.listar_tarefas()
    return render(request, 'tarefas/lista_tarefas.html', {'tarefas': tarefas})

def inserir_tarefa(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data["titulo"]
            descricao = form.cleaned_data["descricao"]
            tarefa_nova = tarefa.Tarefa(titulo=titulo, descricao=descricao)
            tarefa_service.cadastrar_tarefa(tarefa_nova)
            return redirect('listar_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'tarefas/formulario_tarefa.html', {'form': form})

def listar_tarefa_id(request, id):
    tarefa = tarefa_service.listar_tarefa_id(id)
    return render(request, 'tarefas/lista_tarefa.html', {'tarefa': tarefa})

def editar_tarefa(request, id):
    tarefa_busca = tarefa_service.listar_tarefa_id(id)
    form = TarefaForm(request.POST or None, instance=tarefa_busca)
    if form.is_valid():
        titulo = form.cleaned_data["titulo"]
        descricao = form.cleaned_data["descricao"]
        tarefa_novo = tarefa.Tarefa(titulo=titulo, descricao=descricao)
        tarefa_service.editar_tarefa(tarefa_busca, tarefa_novo)
        return redirect('listar_tarefas')

    return render(request, 'tarefas/formulario_tarefa.html', {'form': form, 'tarefa': tarefa})

def remover_tarefa(request, id):
    tarefa = tarefa_service.listar_tarefa_id(id)
    if request.method == "POST":
        tarefa_service.remover_tarefa(id)
        return redirect('listar_tarefas')

    return render(request, 'tarefas/confirma_exclusao.html', {'tarefa': tarefa})