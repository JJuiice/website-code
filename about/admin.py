from django.contrib import admin
from about.models import Header, ProgrammingLanguage, TechSkill, PE, Leadership


# Register your models here.
class HeaderAdmin(admin.ModelAdmin):
    pass


class ProgrammingLanguageAdmin(admin.ModelAdmin):
    pass


class TechSkillAdmin(admin.ModelAdmin):
    pass


class PEAdmin(admin.ModelAdmin):
    pass


class LeadershipAdmin(admin.ModelAdmin):
    pass


admin.site.register(Header, HeaderAdmin)
admin.site.register(ProgrammingLanguage, ProgrammingLanguageAdmin)
admin.site.register(TechSkill, TechSkillAdmin)
admin.site.register(PE, PEAdmin)
admin.site.register(Leadership, LeadershipAdmin)
