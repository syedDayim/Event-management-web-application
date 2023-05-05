from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class EventRegistration(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    semester = models.IntegerField(validators=[MaxValueValidator(9), MinValueValidator(1)])
    enrolment_no = models.CharField(max_length=11)
    department = models.CharField(max_length=100)
