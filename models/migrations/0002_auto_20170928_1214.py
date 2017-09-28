# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('contacto', models.CharField(max_length=200)),
                ('tipoEmpresa', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=200)),
                ('numTelefono', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('fechaNac', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='author',
        ),
        migrations.DeleteModel(
            name='Noticia',
        ),
    ]
