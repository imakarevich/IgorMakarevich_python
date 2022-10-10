from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.PublishingHouse)
admin.site.register(models.Authors)
admin.site.register(models.Genres)
admin.site.register(models.Series)