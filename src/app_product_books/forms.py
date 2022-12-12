from django import forms
from . import models




class BookCard(forms.ModelForm):
    class Meta:
        model = models.BookCard
        fields = '__all__'

class BookCommentsForm(forms.ModelForm):
    class Meta:
        model = models.BookComments
        fields = ('rate', 'comment',)