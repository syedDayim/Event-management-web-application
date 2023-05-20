from django.db import models
from django.core.validators import RegexValidator


class EventRegistration(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    semester = models.CharField(max_length=1, validators=[RegexValidator(r'^[1-9]$|^10$')])
    enrolment_no = models.CharField(max_length=11)
    contact_no = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')], default='')
    department = models.CharField(max_length=100)

class Event(models.Model):
    image = models.ImageField(upload_to='media/events/images/')
    title = models.CharField(max_length=77)
    month = models.CharField(max_length=12)
    day = models.CharField(max_length=14)
    year = models.CharField(max_length=4)
    duration = models.CharField(max_length=10)
    eligibility = models.CharField(max_length=1024, default='You must know at least 1 programming language.')
    prize = models.CharField(max_length=1024, default='Certifications and trophies will be given to first 3 rank holders.')
