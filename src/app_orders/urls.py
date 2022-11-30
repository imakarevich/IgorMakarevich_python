from django.urls import path
from . import views
app_name = 'app_orders'

urlpatterns = [
    path('cart/', views.show_cart, name = 'cart'),
    path('delete_position/<int:pk>', views.delete_position, name = 'delete-position'),
    path('create_order/', views.Order.as_view(), name = 'create-order'),
    path('order_success/', views.OrderSuccess.as_view(), name = 'order-success'),   
]