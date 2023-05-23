from django.shortcuts import render
from events import models as mp
# Create your views here.

def homepage(request):
    event = mp.Event.objects.first()  # Assuming you want to fetch the first event

    context = {
        'event': event,
    }
    return render(request, 'homepage/homepage.html',context)

def aboutus(request):
    return render(request, 'homepage/know.html', {})