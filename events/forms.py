from django import forms


class EventRegistrationForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    semester = forms.CharField()
    enrollment_no = forms.CharField()
    department = forms.CharField()
