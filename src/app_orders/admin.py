from django.contrib import admin
from . import models

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')

class BookInCartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'book', 'cart', 'quantity', 'price', 'created_date', 'updated_date')

class OrderAllAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status', 'cart', 'phone_number', 'address', 'email', 'comments', 'created_date', 'updated_date')

admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.BookInCart, BookInCartAdmin)
admin.site.register(models.OrderAll, OrderAllAdmin)