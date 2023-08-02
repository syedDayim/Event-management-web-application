from django.db import models

class Paper(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='papers/')
    user = models.CharField(max_length=150, blank=True)
    percentage = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.title
