from django.db import models


# Create your models here.
class ProjectList(models.Model):
    name = models.CharField(max_length=20)
    external_url = models.URLField(default='#')
