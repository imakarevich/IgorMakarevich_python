from django.urls import path
from . import views
app_name = 'app_accounts'

urlpatterns = [
    path('accounts/', views.ListAccounts.as_view(), name = 'accounts-list'),
    # path('accounts_create/', views.create_account, name = 'accounts-create'),
    # path('authors_read/<int:pk>', views.ReadAuthors.as_view(), name = 'authors-detail'),
    path('accounts_update/<int:pk>', views.update_accounts, name = 'accounts-update'),
    path('accounts_detail/<int:pk>', views.DetailAccounts.as_view(), name = 'accounts-detail'),
    # path('authors_delete/<int:pk>', views.DeleteAuthors.as_view(), name = 'authors-delete'),
]