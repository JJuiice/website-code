from django.shortcuts import render
from about.models import TechSkills

# Create your views here.
def about(request):
    skills = TechSkills.objects.all()
    context = {
        'skills': skills
    }

    return render(request, 'about.html', context)