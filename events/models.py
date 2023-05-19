from django.db import models

class EventRegistration(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    semester = models.IntegerField()
    enrolment_no = models.CharField(max_length=11)
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
