from django import forms
from . import models




class BookCard(forms.ModelForm):
    class Meta:
        model = models.BookCard
        fields = '__all__'