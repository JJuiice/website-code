from django.db import models
from django.core.validators import MaxValueValidator
from datetime import date

current_date = date.today()


# Create your models here.
class TechSkills(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])

    class Meta:
        ordering = ['-level', 'name']


class PE(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    company = models.CharField(max_length=30)
    additional_time_info = models.CharField(max_length=30, blank=True)
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
