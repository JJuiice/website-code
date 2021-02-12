#  Copyright (c) 2020-2021 Ojas Anand.
#
#  This file is part of GNU package. GNU package is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version. GNU package is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
#  PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of
#  the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.

from django.db import models
from django.core.validators import MaxValueValidator
from datetime import date

current_date = date.today()


# Create your models here.
class Header(models.Model):
    header = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])

    class Meta:
        ordering = ['-level', 'name']


class TechSkill(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])

    class Meta:
        ordering = ['-level', 'name']


class PE(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    company = models.CharField(max_length=40)
    start_period = models.CharField(max_length=10, blank=True)
    start_year = models.CharField(max_length=4, default=current_date.year)
    end_period = models.CharField(max_length=10, default="Present")
    end_year = models.CharField(max_length=4, blank=True)
    details = models.TextField()

    class Meta:
        ordering = ['-start_year']


class Leadership(models.Model):
    title = models.CharField(max_length=50)
    organization = models.CharField(max_length=30)
    start_period = models.CharField(max_length=10, blank=True)
    start_year = models.CharField(max_length=4, default=current_date.year)
    end_period = models.CharField(max_length=10, default="Present")
    end_year = models.CharField(max_length=4, blank=True)
    details = models.TextField()

    class Meta:
        ordering = ['-start_year']
