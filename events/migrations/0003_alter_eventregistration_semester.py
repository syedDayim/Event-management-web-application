# Generated by Django 4.1.7 on 2023-05-05 10:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_eventregistration_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='semester',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(1)]),
        ),
    ]
