from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def learn(request):
    if request.user.is_authenticated:
        course = Course.objects.all()
        print(course)
        return render(request, 'learn/learn.html', {'course': course})
    else:
        return redirect('login')