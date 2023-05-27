from django.shortcuts import render
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
    else:
        sign_up_form = SignUpForm()
    context = {
        'form': sign_up_form,
    }
    return render(request, 'auth_app/signup.html', context)

def login(request):
    return render(request, 'auth_app/login.html')
