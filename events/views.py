from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EventRegistrationForm

# Create your views here.
def registrationSuccess(request):
    return render(request, 'events/success.html',{})


def events(request):
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)  
        if form.is_valid():
            return HttpResponseRedirect('sucess/')
    else:
        form = EventRegistrationForm()
    # HttpResponseRedirect('/events/success')
    return render(request, 'events/events.html', {'form': form})