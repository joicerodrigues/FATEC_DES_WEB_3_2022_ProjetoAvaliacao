# Generated by Django 4.1.1 on 2022-11-29 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='palestramodel',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, verbose_name='modificado em'),
        ),
    ]
