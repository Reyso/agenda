from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.
class eventos(models.Model):
    titulo = models.CharField(max_length=100) #max de 100 caracteres
    descricao = models.TextField(blank=True, null=True) #pode ser branco ou nulo
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True) #preenchimento automatico 
    usuario = models.ForeignKey(User , on_delete=models.CASCADE) #usuario excluido tbm excluirá todos os eventos em cascata

    
    class Meta:
        db_table = 'Evento'  #definindo o nome da tabela como 

    def __str__(self):
        return self.titulo