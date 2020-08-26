from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class TechSkills(models.Model):
    index = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])
    name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['index']