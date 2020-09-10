from django.contrib import admin
from projects.models import ProjectList


# Register your models here.
class ProjectListAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProjectList, ProjectListAdmin)
