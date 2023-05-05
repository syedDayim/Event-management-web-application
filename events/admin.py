from django.contrib import admin
from .models import EventRegistration

# Register your models here.

@admin.register(EventRegistration)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'semester', 'enrolment_no', 'department')