from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TarefasForm
from .models import tarefasModel
from django.http import HttpRequest

def tarefas_home(request):
    contexto = {
        "nome": "João",
        "tarefas" : tarefasModel.objects.all()
    }
    return render(request, 'tarefas/home.html', contexto)

def tarefas_add(request:HttpRequest):
    if request.method =="POST":
        formulario = TarefasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")
    contexto = {
        'form' : TarefasForm()
    }
    return render(request, "tarefas/adicionar.html", contexto)

def tarefas_remover(request:HttpRequest, id):
    tarefa = get_object_or_404(tarefasModel, id=id)
    tarefa.delete()
    return redirect("tarefas:home")

def tarefas_editar(request:HttpRequest, id):
    tarefa = get_object_or_404(tarefasModel, id=id)
    if request.method == "POST":
        formulario = TarefasForm(request.POST, instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")
    formulario = TarefasForm(instance=tarefa)
    context = {
        'form':formulario
    }
    return render(request, 'tarefas/editar.html', context)

# Create your views here.