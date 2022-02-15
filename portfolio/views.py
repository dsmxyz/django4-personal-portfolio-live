from django.shortcuts import render
from .models import Project

# View that shows the homepage
def home(request):
    projects=Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

