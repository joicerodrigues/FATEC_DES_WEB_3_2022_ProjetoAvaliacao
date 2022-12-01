from django.db import models

#criação do AlunoModel
class AlunoModel(models.Model):
    nome = models.CharField(max_length=70)
    idade = models.IntegerField()
    curso= models.CharField(max_length=70)
    def __str__(self):
        return self.nome
    

#criação do PalestraModel 
class PalestraModel(models.Model):
    palestra = models.CharField('Palestra',max_length=50)
    palestrante = models.CharField('Palestrante', max_length=50)
    sala = models.CharField('Sala', max_length=50)
    horario = models.DateTimeField()
    curriculo = models.CharField('Curriculo',max_length=50)
    
    def __str__(self):
        return self.palestra
    