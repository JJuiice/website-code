#  Copyright (c) 2020-2021 Ojas Anand.
#
#  This file is part of GNU package. GNU package is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version. GNU package is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
#  PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of
#  the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.

from about.models import Header, ProgrammingLanguage, TechSkill, PE, Leadership
from django.views.generic.base import TemplateView


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        headers = Header.objects.all()
        pls = ProgrammingLanguage.objects.all()
        skills = TechSkill.objects.all()
        pes = PE.objects.all()
        leaderships = Leadership.objects.all()

        context = super().get_context_data(**kwargs)
        context['headers'] = headers
        context['pls'] = pls
        context['skills'] = skills
        context['pes'] = pes
        context['leaderships'] = leaderships

        return context
