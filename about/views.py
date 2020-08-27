from django.shortcuts import render
from about.models import TechSkills, PE, Leadership


# Create your views here.
def about(request):
    skills = TechSkills.objects.all()
    pes = PE.objects.all()
    leaderships = Leadership.objects.all()
    context = {
        'skills': skills,
        'pes': pes,
        'leaderships': leaderships
    }

    return render(request, 'about.html', context)
