from django.contrib import admin
from about.models import TechSkills, PE, Leadership


# Register your models here.
class TechSkillsAdmin(admin.ModelAdmin):
    pass


class PEAdmin(admin.ModelAdmin):
    pass


class LeadershipAdmin(admin.ModelAdmin):
    pass


admin.site.register(TechSkills, TechSkillsAdmin)
admin.site.register(PE, PEAdmin)
admin.site.register(Leadership, LeadershipAdmin)
