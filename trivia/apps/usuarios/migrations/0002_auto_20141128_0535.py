# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil_registro',
            name='user',
        ),
        migrations.DeleteModel(
            name='perfil_registro',
        ),
    ]
