# Generated by Django 3.0.4 on 2020-05-16 04:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_auto_20200516_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='reported_by',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None),
        ),
    ]
