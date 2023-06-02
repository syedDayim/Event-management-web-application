from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def learn(request):
    course = Course.objects.all()
    print(course)
    return render(request, 'learn/learn.html', {'course': course})
    