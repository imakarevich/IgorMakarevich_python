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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from app_reference_book.views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('app_reference_book/', include('app_reference_book.urls', namespace = 'app_reference_book')),
    path('', HomePage.as_view(), name = 'Home_page'),
    path('app_product_books/', include('app_product_books.urls', namespace = 'app_product_books')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
