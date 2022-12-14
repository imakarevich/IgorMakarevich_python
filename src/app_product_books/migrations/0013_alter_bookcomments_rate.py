# Generated by Django 4.1.2 on 2022-12-12 11:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product_books', '0012_remove_bookcard_rating_bookcomments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcomments',
            name='rate',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Рейтинг'),
        ),
    ]
