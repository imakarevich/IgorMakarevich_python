from django.db import models
from app_reference_book import models as reference
# Create your models here.


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
        verbose_name="Авторы книги"
    )
    serie = models.ManyToManyField(
        reference.Series,
        verbose_name="Серия",
        blank=True
    )
    genre = models.ManyToManyField(
        reference.Genres,
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
        verbose_name="Издательство"
    )
    availability = models.PositiveSmallIntegerField(
        verbose_name="Количество книг в наличии",
    )
    active = models.BooleanField(
        verbose_name="Доступен для заказа",
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name="Рейтинг",
    )
    description = models.TextField(
    )
    date_entered_catalog = models.DateField(
        auto_now_add=True
    )
    date_last_modified = models.DateField(
        auto_now=True
    )
    def __str__(self):
        return self.name
    





