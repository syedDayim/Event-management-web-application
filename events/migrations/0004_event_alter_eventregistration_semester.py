# Generated by Django 4.1.7 on 2023-05-19 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_eventregistration_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=77)),
                ('month', models.CharField(max_length=12)),
                ('day', models.CharField(max_length=14)),
                ('year', models.CharField(max_length=4)),
                ('duration', models.CharField(max_length=10)),
                ('eligibilityFeild', models.CharField(max_length=255)),
                ('rules', models.CharField(max_length=1024)),
                ('prices', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='semester',
            field=models.IntegerField(),
        ),
    ]
