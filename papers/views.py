from django.shortcuts import render, redirect
from .forms import PaperForm
from .models import Paper

def papers(request):
    user_papers = Paper.objects.filter(user=request.user.username)

    if request.method == 'POST':
        form = PaperForm(request.POST, request.FILES)
        if form.is_valid():
            paper = form.save(commit=False)
            paper.user = request.user.username  # Set the username
            paper.save()
            return redirect('homepage')
        else:
            print(form.errors)  # Print form errors to the console
    else:
        form = PaperForm()
    
    return render(request, 'paperHome.html', {'form': form, 'user_papers': user_papers})

def user_papers(request):
    user_papers = Paper.objects.filter(user=request.user.username)

    for paper in user_papers:
        if paper.percentage is None:
            paper.display_percentage = "Not Reviewed"
        else:
            paper.display_percentage = f"{paper.percentage}%"

    context = {
        'user_papers': user_papers,
    }

    return render(request, 'user_papers.html', context)
