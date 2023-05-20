from django import forms
from .models import EventRegistration

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['name', 'email', 'semester', 'enrolment_no', 'contact_no',  'department' ]

        labels = {
            'name': '',
            'email': '',
            'semester': '',
            'enrolment_no': '',
            'contact_no': '',
            'department': '',
        }

        error_messages = {
            'name':{'required': 'Enter your name'},
            'email':{'required': 'Enter your email address'},
            'semester':{'required': 'Enter your semester'},
            'enrolment_no':{'required': 'Enter your Enrollment Number'},
            'contact_no': {'required': 'Enter your Contact Number'},
            'department':{'required': 'Enter your department'},
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'name-field', 'placeholder':'Name'}),
            'email': forms.EmailInput(attrs={'class': 'email-field', 'placeholder': 'Email'}),
            'semester': forms.TextInput(attrs={'class': 'semester-field', 'placeholder': 'Semester'}),
            'enrolment_no': forms.TextInput(attrs={'class': 'enrollment', 'placeholder': 'Enrollment Number'}),
            'contact_no': forms.TextInput(attrs={'class': 'enrollment', 'placeholder': 'Contact Number'}),
            'department': forms.TextInput(attrs={'class': 'department-field', 'placeholder': 'Department'}),

        }