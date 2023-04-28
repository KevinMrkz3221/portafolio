from django.contrib import admin
from . import models

# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
    list_display=('pk','name', 'category',)


admin.site.register(models.Projects, ProjectsAdmin)

class PicturesAdmin(admin.ModelAdmin):
    list_display =('pk', 'image', 'project')

admin.site.register(models.Pictures, PicturesAdmin)