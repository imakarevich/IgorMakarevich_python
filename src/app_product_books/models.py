from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from app_reference_book import models as reference
from django.contrib.auth import get_user_model
from django.db.models import Avg
# Create your models here.
User = get_user_model()

class BookCard(models.Model):
    name = models.CharField(
        verbose_name="Название книги",
        max_length=200
        )
    picture = models.ImageField(
        verbose_name="Фото обложки",
        upload_to='upload/books/',
        blank=True,
        null=True
    )
    price = models.DecimalField(
        verbose_name="Цена (BYN)",
        max_digits=6,
        decimal_places=2 
    )
    authors = models.ManyToManyField(
        reference.Authors,
        related_name="Book",
        verbose_name="Авторы книги"
    )
    serie = models.ManyToManyField(
        reference.Series,
        verbose_name="Серия",
        blank=True
    )
    genre = models.ManyToManyField(
        reference.Genres,
        related_name="Book",
        verbose_name="Жанр"
    )
    year_of_publishing = models.PositiveSmallIntegerField(
        verbose_name="Год издания"
    )
    pages = models.PositiveSmallIntegerField(
        verbose_name="Страниц"
    )
    cover = models.CharField(
        verbose_name="Переплет",
        max_length=100
    )
    format = models.CharField(
        verbose_name="Формат",
        max_length=100
    )
    isbn = models.CharField(
        verbose_name="ISBN",
        max_length=100
    )
    weight = models.PositiveSmallIntegerField(
        verbose_name="Вес (гр)"
    )
    age_restrictions = models.CharField(
        verbose_name="Возрастные ограничения",
        max_length=4
    )
    publishing = models.ManyToManyField(
        reference.PublishingHouse,
        related_name="Book",
        verbose_name="Издательство"
    )
    availability = models.PositiveSmallIntegerField(
        verbose_name="Количество книг в наличии",
    )
    active = models.BooleanField(
        verbose_name="Доступен для заказа",
    )
    description = models.TextField(
    )
    date_entered_catalog = models.DateField(
        verbose_name="Дата внесения в каталог",
        auto_now_add=True
    )
    updated_date = models.DateField(
        verbose_name="Дата последнего изменения карточки",
        auto_now=True
    )
    
    def __str__(self):
        return self.name

    @property
    def rating_average(self):
        if BookComments.objects.filter(bookcard=self):
            avg = BookComments.objects.filter(bookcard=self).aggregate(Avg('rate'))
            print(round(avg['rate__avg'],2))
            # BookCard.objects.get(self).aggregate(Avg('bookcomments__rate'))
            return round(avg['rate__avg'],2)
        

class BookComments(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='book_comments',
        verbose_name='Комментарий пользователя',
        null=True,
        blank=True
    )
    bookcard = models.ForeignKey(
        'app_product_books.BookCard',
        verbose_name='Книга', 
        related_name='bookcomments',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    rate = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Рейтинг",
        null=True,
        blank=True
    )
    comment = models.TextField(
        verbose_name="Комментарий",
    )
    created_date = models.DateTimeField(
    "Created date",
    auto_now_add=True
    )
    updated_date = models.DateTimeField(
    "Update date",
    auto_now=True
    )        




