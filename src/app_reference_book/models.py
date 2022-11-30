from django.db import models

# Create your models here.

class PublishingHouse(models.Model):
    name = models.CharField(
        max_length=40,
        verbose_name="Название"
        )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание"
        )
    def __str__(self):
        return f'{self.name}'

class Authors(models.Model):
    first_last_name = models.CharField(
        max_length=100,
        verbose_name="ФИО"
        )
    photo = models.ImageField(
        verbose_name="Фотография",
        upload_to='upload/Authors/',
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True)
    def __str__(self):
        return f'{self.first_last_name}'

class Genres(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название"
        )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание"
        )
    def __str__(self):
        return f'{self.name}'

class Series(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название"
        )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание"
        )
    def __str__(self):
        return f'{self.name}'

class Status(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Название"
        )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание"
        )
    def __str__(self):
        return f'{self.name}'

