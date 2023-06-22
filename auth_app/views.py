from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login as auth_login, authenticate, logout
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings


def signup(request):
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        sign_up_form = SignUpForm()
    context = {
        'form': sign_up_form,
    }
    return render(request, 'auth_app/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            login_form = AuthenticationForm(request=request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('profile')
        else:
            login_form = AuthenticationForm()

    context = {
        'form': login_form,
        'name': request.user,
    }
    return render(request, 'auth_app/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('homepage')


from django.contrib.auth.models import User
from .models import Profile

def profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.filter(user=user).first()
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=user)
            if profile:
                p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
            else:
                p_form = ProfileUpdateForm(request.POST, request.FILES)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                if p_form.instance:
                    p_form.instance.user = user
                    p_form.save()
                else:
                    profile = p_form.save(commit=False)
                    profile.user = user
                    profile.save()
                return redirect('profile')
        else:
            u_form = UserUpdateForm()
            if profile:
                p_form = ProfileUpdateForm(instance=profile)
            else:
                p_form = ProfileUpdateForm()
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, 'auth_app/profile.html', context)
    else:
        return redirect('login')


def user_change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            changePassword = PasswordChangeForm(user=request.user, data=request.POST)
            if changePassword.is_valid():
                changePassword.save()
                return redirect('profile')
        else:
            changePassword = PasswordChangeForm(user=request.user)

        context = {
            'form': changePassword
        }
        return render(request, 'auth_app/password_change.html', context)
    else:
        return redirect('login')


from django.urls import reverse

# def password_reset_request(request):
#     if request.method == 'POST':
#         password_reset_form = PasswordResetForm(request.POST)
#         if password_reset_form.is_valid():
#             user_email = password_reset_form.cleaned_data['email']
#             associated_users = User.objects.filter(email=user_email)
#             if associated_users.exists():
#                 for user in associated_users:
#                     # Generate the password reset token and encode the user ID
#                     uid = urlsafe_base64_encode(force_bytes(user.pk))
#                     token = default_token_generator.make_token(user)
                    
#                     # Build the password reset URL
#                     reset_url = request.build_absolute_uri(
#                         reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
#                     )
                    
#                     # Generate the email content
#                     subject = 'Password Reset Request'
#                     email_template = 'auth_app/password_reset_email.html'
#                     email_context = {
#                         'user': user,
#                         'reset_url': reset_url,
#                     }
#                     email_content = render_to_string(email_template, email_context)
                    
#                     # Send the password reset email
#                     send_mail(subject, email_content, settings.DEFAULT_FROM_EMAIL, [user_email])
                    
#                     messages.success(request, 'Password reset email has been sent.')
#                     return redirect('password_reset_done')
#     else:
#         password_reset_form = PasswordResetForm()

#     return render(request, 'auth_app/password_reset.html', {'form': password_reset_form})


class PasswordResetConfirmViewCustom(PasswordResetConfirmView):
    template_name = 'auth_app/password_reset_confirm.html'
    form_class = SetPasswordForm
    success_url = '/auth/password-reset/complete/'


# def password_reset_complete(request):
#     return render(request, 'auth_app/password_reset_complete.html')
