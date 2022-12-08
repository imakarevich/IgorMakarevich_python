from django.urls import path
from . import views
app_name = 'app_orders'

urlpatterns = [
    path('cart/', views.show_cart, name = 'cart'),
    path('delete_position/<int:pk>', views.delete_position, name = 'delete-position'),
    path('create_order/', views.Order.as_view(), name = 'create-order'),
    path('order_success/', views.OrderSuccess.as_view(), name = 'order-success'),
    path('order_list/', views.OrderAllList.as_view(), name = 'orders-list'),
    path('order_update/<int:pk>', views.OrderAllUpdate.as_view(), name = 'orders-update'),
    path('add_book_in_cart_from_order_update/<int:pk>', views.AddBookInCartFromOrderUpdate.as_view(), name = 'add-book-in-cart-from-order-update'),
    path('delete_book_from_order/<int:pk>', views.delete_book_from_order, name = 'delete-book-from-order'),
]