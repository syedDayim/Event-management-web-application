from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.forms import ClearableFileInput

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


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        label='',
        required=False
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        label='',
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(
        label='',
        required=False,
        widget=ClearableFileInput(attrs={'class': 'custom-file-input', 'accept': 'image/*'})
    )

    class Meta:
        model = Profile
        fields = ['image']