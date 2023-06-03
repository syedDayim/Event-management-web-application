# Generated by Django 4.1.7 on 2023-06-03 13:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_eventregistration_contact_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='semester',
            field=models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^[1-9]$|^10$')]),
        ),
    ]