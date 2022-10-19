"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_reference_book import views as ref



urlpatterns = [
    path('admin/', admin.site.urls), 
    path('publishing_house/', ref.ListPublishingHouse.as_view()),
    path('publishing_house_create/', ref.CreatePublishingHouse.as_view()),
    path('publishing_house_read/<int:pk>', ref.ReadPublishingHouse.as_view()),
    path('publishing_house_update/<int:pk>', ref.UpdatePublishingHouse.as_view()),
    path('publishing_house_delete/<int:pk>', ref.DeletePublishingHouse.as_view()),
    path('authors/', ref.ListAuthors.as_view()),
    path('authors_create/', ref.CreateAuthors.as_view()),
    path('authors_read/<int:pk>', ref.ReadAuthors.as_view()),
    path('authors_update/<int:pk>', ref.UpdateAuthors.as_view()),
    path('authors_delete/<int:pk>', ref.DeleteAuthors.as_view()),
    path('genres/', ref.ListGenres.as_view()),
    path('genres_create/', ref.CreateGenres.as_view()),
    path('genres_read/<int:pk>', ref.ReadGenres.as_view()),
    path('genres_update/<int:pk>', ref.UpdateGenres.as_view()),
    path('genres_delete/<int:pk>', ref.DeleteGenres.as_view()),
    path('series/', ref.ListSeries.as_view()),
    path('series_create/', ref.CreateSeries.as_view()),
    path('series_read/<int:pk>', ref.ReadSeries.as_view()),
    path('series_update/<int:pk>', ref.UpdateSeries.as_view()),
    path('series_delete/<int:pk>', ref.DeleteSeries.as_view()),
]
