from django.contrib import admin
from .models import EventRegistration, Event

# Register your models here.

@admin.register(EventRegistration)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'semester', 'enrolment_no', 'department')

@admin.register(Event)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'month', 'day', 'year','duration','eligibility', 'prize')
