from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Retype Password', widget=forms.PasswordInput)
    username = forms.CharField(
        error_messages={'required': 'Please enter a username.'}
    )
    first_name = forms.CharField(
        error_messages={'required': 'Please enter your first name.'}
    )
    last_name = forms.CharField(
        error_messages={'required': 'Please enter your last name.'}
    )
    email = forms.EmailField(
        error_messages={
            'required': 'Please enter your email address.',
            'invalid': 'Please enter a valid email address.',
        }
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
