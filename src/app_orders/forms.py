from django import forms
from . import models




class OrderForm(forms.ModelForm):
    class Meta:
        model = models.OrderAll
        fields = ('phone_number', 'address', 'email', 'comments')