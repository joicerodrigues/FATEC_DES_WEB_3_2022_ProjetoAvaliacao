# Generated by Django 4.1.1 on 2022-11-29 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alunomodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alunomodel',
            options={'verbose_name': 'Aluno', 'verbose_name_plural': 'Alunos'},
        ),
        migrations.AlterModelOptions(
            name='palestramodel',
            options={'verbose_name': 'Palestra', 'verbose_name_plural': 'Palestras'},
        ),
    ]