from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class UserExtensionForm(forms.ModelForm):
    class Meta:
        model = models.UserExtension
        fields = ['phone_number', 'address_country', 'address_city', 'address_index', 'address_fist', 'address_second', 'description']

