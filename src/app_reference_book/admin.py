from django.contrib import admin

# Register your models here.

from . import models

class StatusAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')

admin.site.register(models.PublishingHouse)
admin.site.register(models.Authors)
admin.site.register(models.Genres)
admin.site.register(models.Series)
admin.site.register(models.Status, StatusAdmin)



