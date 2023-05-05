from django import forms
from .models import EventRegistration

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['name', 'email', 'semester', 'enrolment_no', 'department' ]

        labels = {
            'name': '',
            'email': '',
            'semester': '',
            'enrolment_no': '',
            'department': '',
        }

        error_messages = {
            'name':{'required': 'Enter your name'},
            'email':{'required': 'Enter your email address'},
            'semester':{'required': 'Enter your semester'},
            'enrolment_no':{'required': 'Enter your Enrollment Number'},
            'department':{'required': 'Enter your department'},
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'name-field', 'placeholder':'Name'}),
            'email': forms.EmailInput(attrs={'class': 'email-field', 'placeholder': 'Email'}),
            'semester': forms.NumberInput(attrs={'class': 'semester-field', 'placeholder': 'Semester'}),
            'enrolment_no': forms.TextInput(attrs={'class': 'enrollment', 'placeholder': 'Enrollment Number'}),
            'department': forms.TextInput(attrs={'class': 'department-field', 'placeholder': 'Department'}),

        }