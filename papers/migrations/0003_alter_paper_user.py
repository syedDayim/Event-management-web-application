# Generated by Django 4.2.4 on 2023-08-02 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0002_paper_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='user',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
