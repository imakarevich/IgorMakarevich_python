from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'app_admin_portal'

urlpatterns = [
    path('admin_portal/', views.AdminPortalForExployees.as_view(), name = 'admin-portal'),
    path('login/', auth_views.LoginView.as_view(template_name='app_admin_portal/login.html', next_page=reverse_lazy('app_admin_portal:admin-portal')), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'home_page'), name='logout')
]