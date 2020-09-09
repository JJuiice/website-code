from django.shortcuts import render
import requests


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def home_license(request):
    url = "https://raw.githubusercontent.com/sigmaupsilon/website-code/master/LICENSE"
    content = requests.get(url).text

    context = {
        "license": content
    }

    return render(request, 'LICENSE.html', context)
