from django.db import models
from django.contrib.auth import get_user_model
from app_reference_book.models import Status
# Create your models here.
User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='carts',
        verbose_name='Корзина пользователя',
        null=True,
        blank=True
    )
    def total_price_cart(self):
        all_positions_in_cart = self.book_in_cart.all()
        total_price_cart = 0
        for position_in_cart in all_positions_in_cart:
            total_price_cart += position_in_cart.total_price_position
        return total_price_cart
        
    def __str__(self):
        return f'{self.user}_{self.pk}'

class BookInCart(models.Model):
    book = models.ForeignKey(
        "app_product_books.BookCard",
        verbose_name="Book in cart",
        on_delete=models.PROTECT
        )
    cart = models.ForeignKey(
        "app_orders.Cart",
        verbose_name="Cart",
        related_name="book_in_cart",
        on_delete=models.CASCADE
        )
    quantity = models.PositiveSmallIntegerField(
        verbose_name="Quantity",
        default=1
    )
    price = models.DecimalField(
        "price",
        max_digits=6,
        decimal_places=2
    )
    created_date = models.DateTimeField(
        "Created date",
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        "Update date",
        auto_now=True
    )
    @property
    def total_price_position(self):
        return self.quantity*self.price


class OrderAll(models.Model):
    status = models.ForeignKey(
        "app_reference_book.Status",
        verbose_name='Статус заказа', 
        related_name='order',
        on_delete=models.PROTECT,
        default=1)
    cart = models.ForeignKey(
        "app_orders.Cart",
        verbose_name="Корзина",
        related_name='order',
        on_delete=models.PROTECT)
    phone_number = models.CharField(
        verbose_name="Телефон",
        max_length=15
    )
    address = models.CharField(
        verbose_name="Адрес доставки",
        max_length=30
    )
    email = models.EmailField(
        verbose_name="EMAIL",
        max_length=254)
    comments = models.TextField(
        verbose_name="Примечание",
        blank=True, null=True
    )
    created_date = models.DateTimeField(
    "Created date",
    auto_now_add=True
    )
    updated_date = models.DateTimeField(
    "Update date",
    auto_now=True
    )        
