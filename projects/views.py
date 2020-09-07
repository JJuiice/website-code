from django.shortcuts import render
from projects.models import ProjectList


# Create your views here.
def projects(request):
    pl = ProjectList.objects.all()
    pLink = ProjectList.objects.all()
    context = {
        'pl': pl,
        'pLink': pLink
    }

    return render(request, 'projects.html', context)