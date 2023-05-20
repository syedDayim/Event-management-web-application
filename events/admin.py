from django.contrib import admin
from .models import EventRegistration,Event
import pandas as pd
import csv
from django.http import HttpResponse

@admin.register(EventRegistration)
class StudentList(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'semester', 'enrolment_no', 'contact_no', 'department')
    actions = ['export_candidates']

    # ...

    def export_candidates(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="candidates.csv"'

        writer = csv.writer(response)

        candidates = queryset.values_list('name', 'email', 'semester', 'enrolment_no', 'contact_no', 'department')
        field_names = ['Name', 'Email', 'Semester', 'Enrolment No', 'Contact No', 'Department']
        writer.writerow(field_names)
        for candidate in candidates:
            writer.writerow(candidate)

        return response

# ...


    export_candidates.short_description = "Export selected candidates to CSV"


@admin.register(Event)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'month', 'day', 'year', 'duration', 'eligibility', 'prize')
