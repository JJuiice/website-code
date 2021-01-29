from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=20)
    external_url = models.URLField(default='#')

    class Meta:
        ordering = ['id']
