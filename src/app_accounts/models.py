from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class UserExtension(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='extension',
        verbose_name='Пользователь',
        blank=True,
        null=True
        )
    phone_number = models.CharField(
        verbose_name="Телефон",
        max_length=15
    )
    address_country = models.CharField(
        verbose_name="Страна",
        max_length=20,
        blank=True,
        null=True
    )
    address_city = models.CharField(
        verbose_name="Город",
        max_length=20,
        blank=True,
        null=True
    )
    address_index = models.SmallIntegerField(
        verbose_name="Индекс",
        blank=True,
        null=True
    )
    address_fist = models.CharField(
        verbose_name="Адрес 1",
        max_length=50,
        blank=True,
        null=True
    )
    address_second = models.CharField(
        verbose_name="Адрес 2",
        max_length=50,
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name="Дополнительная информация",
        blank=True,
        null=True
    )

    class Meta:
        permissions = (("access_for_managers_admin", "Managers and admin can see it"), )

