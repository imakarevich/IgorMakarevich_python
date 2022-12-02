from django.urls import path
from . import views
app_name = 'app_home_page'

urlpatterns = [
    path('search_from_accordion/', views.search_from_accordion, name = 'search-from-accordion'),
]