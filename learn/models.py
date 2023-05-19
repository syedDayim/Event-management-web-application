from django.db import models

# Create your models here.
class Course(models.Model):
    cover = models.ImageField(upload_to='media/cources/images')
    title = models.CharField(max_length=270)
    bio = models.CharField(max_length=1024)
    link = models.CharField(max_length=1024)
