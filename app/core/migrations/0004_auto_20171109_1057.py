# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_eliminarusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='profesion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Empresa'),
        ),
    ]
