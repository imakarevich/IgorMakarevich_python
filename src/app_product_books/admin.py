from django.contrib import admin
from . import models
# Register your models here.



class BookCommentsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'rate', 'comment', 'bookcard', 'created_date', 'updated_date')

admin.site.register(models.BookCard)
admin.site.register(models.BookComments, BookCommentsAdmin)