from django.shortcuts import render
from django.views import generic

# Create your views here.

class HomePage(generic.TemplateView):
    template_name = "app_home_page/home_page.html"

