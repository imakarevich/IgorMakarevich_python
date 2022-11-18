from django.urls import path
from . import views
app_name = 'app_admin_portal'

urlpatterns = [
    path('admin_portal/', views.AdminPortalForExployees.as_view(), name = 'admin-portal'),
]