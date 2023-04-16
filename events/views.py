from django.shortcuts import render
from .forms import EventRegistrationForm
# Create your views here.
def events(request):
    form = EventRegistrationForm()
    return render(request, 'events/events.html', {'form': form})