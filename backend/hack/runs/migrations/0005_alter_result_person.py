# Generated by Django 5.2 on 2025-04-05 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0004_alter_person_options_alter_result_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='result', to='runs.person', verbose_name='Человек'),
        ),
    ]
