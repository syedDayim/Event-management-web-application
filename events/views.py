from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import EventRegistration
from .forms import EventRegistrationForm

# Create your views here.
def registrationSuccess(request):
    return render(request, 'events/success.html',{})


def events(request):
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            semester = form.cleaned_data['semester']
            enrolment_no = form.cleaned_data['enrolment_no']
            department = form.cleaned_data['department']
            register_data = EventRegistration(name=name, email=email, semester=semester, enrolment_no=enrolment_no, department=department)
            register_data.save()
            return HttpResponseRedirect('sucess/')
    else:
        form = EventRegistrationForm()
    return render(request, 'events/events.html',{'form': form})