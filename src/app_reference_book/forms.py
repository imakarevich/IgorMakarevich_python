from django import forms
from . import models

class PublishingHouseForm(forms.ModelForm):
    class Meta:
        model = models.PublishingHouse
        fields = '__all__'

class AuthorsForm(forms.ModelForm):
    class Meta:
        model = models.Authors
        fields = '__all__'

class GenresForm(forms.ModelForm):
    class Meta:
        model = models.Genres
        fields = '__all__'

class SeriesForm(forms.ModelForm):
    class Meta:
        model = models.Series
        fields = '__all__'

class StatusForm(forms.ModelForm):
    class Meta:
        model = models.Status
        fields = '__all__'