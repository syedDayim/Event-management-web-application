from django import forms


class EventRegistrationForm(forms.Form):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'name-field'}))

    email = forms.CharField(label="", widget=forms.EmailInput(attrs={'class': 'email-field'}))

    semester = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'semester-field'}))

    enrollment_no = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'enrollment'}))

    department = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'department-field'}))

    def __init__(self, *args, **kwargs):
        super(EventRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['semester'].widget.attrs['placeholder'] = 'Semester'
        self.fields['enrollment_no'].widget.attrs['placeholder'] = 'Enrollment No'
        self.fields['department'].widget.attrs['placeholder'] = 'Department'