from django.contrib import admin
from . import models
# Register your models here.
class UserExtensionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'phone_number', 'address_country', 'address_city', 'address_index', 'address_fist', 'address_second', 'description')

admin.site.register(models.UserExtension, UserExtensionAdmin)