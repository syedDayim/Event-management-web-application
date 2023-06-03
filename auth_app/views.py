from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib import messages

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
        'name' : request.user,
    }
    return render(request, 'auth_app/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('homepage')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'auth_app/profile.html',{})
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
            'form' : changePassword
        }
        return render(request, 'auth_app/password_change.html',context)
    else:
        return redirect('login')