from django.shortcuts import render
from projects.models import projectList


# Create your views here.
def projects(request):
    pl = projectList.objects.all()
    context = {
        'pl': pl
    }

    return render(request, 'projects.html', context)
