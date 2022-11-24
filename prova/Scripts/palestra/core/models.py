from django.db import models

class PalestaModel(models.Model):
    nome = models.CharField('Palestra', max_lenght=90)
    dia = models.IntegerField('Data')
    mes = models.IntegerField('Mês')
    horario = models.IntegerField('Horário')
    sala = models.IntegerField('Sala')
    miniCurriculo = models.IntegerField('Mini Curriculo')
    modificado_em = models.DateTimeField(
        verbose_name='modificado em',
        auto_now_add=False, auto_now=True)

    def _str_(self):
        return self.nome