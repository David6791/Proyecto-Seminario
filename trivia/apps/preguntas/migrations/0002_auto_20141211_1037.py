# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tema_preguntas',
            name='nombre',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
