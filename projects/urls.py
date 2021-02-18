#  Copyright (c) 2020-2021 Ojas Anand.
#
#  This file is part of GNU package. GNU package is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version. GNU package is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
#  PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of
#  the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.

from django.urls import path
from projects import views

urlpatterns = [
    path('', views.Projects.as_view(), name='projects')
]
