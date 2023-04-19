from django.shortcuts import render
from .forms import EventRegistrationForm
# Create your views here.
def registrationSuccess(request):
    return render(request, 'events/success.html',{})


def events(request):
    form = EventRegistrationForm()
    return render(request, 'events/events.html', {'form': form})