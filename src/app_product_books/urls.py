from django.urls import path
from . import views
app_name = 'app_product_books'

urlpatterns = [
    path('bookcard/', views.ListBookCard.as_view(), name = 'bookcard-list'),
    path('bookcard_create/', views.CreateBookCard.as_view(), name = 'bookcard-create'),
    path('bookcard_read/<int:pk>', views.ReadBookCard.as_view(), name = 'bookcard-detail'),
    path('bookcard_update/<int:pk>', views.UpdateBookCard.as_view(), name = 'bookcard-update'),
    path('bookcard_delete/<int:pk>', views.DeleteBookCard.as_view(), name = 'bookcard-delete'),
]