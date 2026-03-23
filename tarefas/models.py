from django.db import models

# Create your models here.
class tarefasModel(models.Model):
    nome = models.CharField(max_length=100)
    tarefa = models.TextField(null=True, blank=True)
    feito = models.BooleanField(default=False)
    

    def __str__(self):
        return self.nome
