# Generated by Django 4.1.7 on 2023-05-05 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='semester',
            field=models.IntegerField(),
        ),
    ]
