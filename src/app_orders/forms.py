from django import forms
from . import models




class OrderForm(forms.ModelForm):
    class Meta:
        model = models.OrderAll
        fields = ('phone_number', 'address', 'email', 'comments')


class CartForm(forms.ModelForm):
    class Meta:
        model = models.Cart
        fields = ('user',)

class BookInCartForm(forms.ModelForm):
    class Meta:
        model = models.BookInCart
        fields = ('book', 'quantity')

class OrderAllForm(forms.ModelForm):
    class Meta:
        model = models.OrderAll
        fields =  ['status', 'phone_number', 'address', 'email', 'comments']