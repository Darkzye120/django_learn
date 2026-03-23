from django import forms
from .models import tarefasModel

class TarefasForm(forms.ModelForm):
    class Meta:
        model = tarefasModel
        fields = ['nome', 'tarefa', 'feito']


