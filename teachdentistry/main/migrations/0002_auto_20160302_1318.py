# flake8: noqa
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dentaleducator',
            name='clinical_field',
            field=models.ManyToManyField(to='main.ClinicalField', blank=True),
        ),
        migrations.AlterField(
            model_name='dentaleducator',
            name='current_dental_career',
            field=models.ManyToManyField(related_name='dentaleducator_current_career', to='main.CareerType', blank=True),
        ),
        migrations.AlterField(
            model_name='dentaleducator',
            name='degree',
            field=models.ManyToManyField(to='main.Degree', blank=True),
        ),
        migrations.AlterField(
            model_name='dentaleducator',
            name='primary_motivation',
            field=models.ManyToManyField(to='main.Motivation', blank=True),
        ),
    ]
