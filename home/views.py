#  Copyright (c) 2020-2021 Ojas Anand.
#
#  This file is part of GNU package. GNU package is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version. GNU package is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
#  PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of
#  the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.

from django.shortcuts import render
from django.views import View
import requests


# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html', {})


class License(View):
    def get(self, request):
        url = "https://raw.githubusercontent.com/sigmaupsilon/website-code/master/LICENSE"
        content = requests.get(url).text

        context = {
            "license": content
        }

        return render(request, 'LICENSE.html', context)
