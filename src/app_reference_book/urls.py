from django.urls import path
from . import views
app_name = 'app_reference_book'

urlpatterns = [
    path('publishing_house/', views.ListPublishingHouse.as_view(), name = 'publishing-house-list'),
    path('publishing_house_create/', views.CreatePublishingHouse.as_view(), name = 'publishing-house-create'),
    path('publishing_house_read/<int:pk>', views.ReadPublishingHouse.as_view(), name = 'publishing-house-detail'),
    path('publishing_house_update/<int:pk>', views.UpdatePublishingHouse.as_view(), name = 'publishing-house-update'),
    path('publishing_house_delete/<int:pk>', views.DeletePublishingHouse.as_view(), name = 'publishing-house-delete'),
    path('authors/', views.ListAuthors.as_view(), name = 'authors-list'),
    path('authors_create/', views.CreateAuthors.as_view(), name = 'authors-create'),
    path('authors_read/<int:pk>', views.ReadAuthors.as_view(), name = 'authors-detail'),
    path('authors_update/<int:pk>', views.UpdateAuthors.as_view(), name = 'authors-update'),
    path('authors_delete/<int:pk>', views.DeleteAuthors.as_view(), name = 'authors-delete'),
    path('genres/', views.ListGenres.as_view(), name = 'genres-list'),
    path('genres_create/', views.CreateGenres.as_view(), name = 'genres-create'),
    path('genres_read/<int:pk>', views.ReadGenres.as_view(), name = 'genres-detail'),
    path('genres_update/<int:pk>', views.UpdateGenres.as_view(), name = 'genres-update'),
    path('genres_delete/<int:pk>', views.DeleteGenres.as_view(), name = 'genres-delete'),
    path('series/', views.ListSeries.as_view(), name = 'series-list'),
    path('series_create/', views.CreateSeries.as_view(), name = 'series-create'),
    path('series_read/<int:pk>', views.ReadSeries.as_view(), name = 'series-detail'),
    path('series_update/<int:pk>', views.UpdateSeries.as_view(), name = 'series-update'),
    path('series_delete/<int:pk>', views.DeleteSeries.as_view(), name = 'series-delete'),
    path('status/', views.ListStatus.as_view(), name = 'status-list'),
    path('status_create/', views.CreateStatus.as_view(), name = 'status-create'),
    path('status_read/<int:pk>', views.ReadStatus.as_view(), name = 'status-detail'),
    path('status_update/<int:pk>', views.UpdateStatus.as_view(), name = 'status-update'),
    path('status_delete/<int:pk>', views.DeleteStatus.as_view(), name = 'status-delete'),
]