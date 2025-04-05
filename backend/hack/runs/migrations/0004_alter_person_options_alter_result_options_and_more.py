# Generated by Django 5.2 on 2025-04-05 08:23

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0003_alter_person_acceleration_alter_person_coef_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['id'], 'verbose_name': 'Человек', 'verbose_name_plural': 'Люди'},
        ),
        migrations.AlterModelOptions(
            name='result',
            options={'verbose_name': ('Результат',), 'verbose_name_plural': 'Результаты'},
        ),
        migrations.AddField(
            model_name='result',
            name='value',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='coef',
            field=models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(-2.1), django.core.validators.MaxValueValidator(0.1)]),
        ),
        migrations.AlterField(
            model_name='result',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='result', to='runs.person', verbose_name='Человек'),
        ),
    ]
