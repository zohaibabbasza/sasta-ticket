from django.contrib import admin
from resume import models

admin.site.register(models.GeneralTag)
admin.site.register(models.Resume)
admin.site.register(models.SkillTag)