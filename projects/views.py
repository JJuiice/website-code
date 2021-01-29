from django.shortcuts import render
from projects.models import Project


# Create your views here.
def projects(request):
    pl = Project.objects.all()
    context = {
        'pl': pl
    }

    return render(request, 'projects.html', context)
