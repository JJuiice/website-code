from django.shortcuts import render
from about.models import Header, ProgrammingLanguage, TechSkill, PE, Leadership


# Create your views here.
def about(request):
    headers = Header.objects.all()
    pls = ProgrammingLanguage.objects.all()
    skills = TechSkill.objects.all()
    pes = PE.objects.all()
    leaderships = Leadership.objects.all()
    context = {
        'headers': headers,
        'pls': pls,
        'skills': skills,
        'pes': pes,
        'leaderships': leaderships
    }

    return render(request, 'about.html', context)
