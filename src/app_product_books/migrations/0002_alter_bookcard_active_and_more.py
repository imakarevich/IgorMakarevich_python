# Generated by Django 4.1.2 on 2022-11-02 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_book', '0005_remove_authors_first_name_remove_authors_last_name_and_more'),
        ('app_product_books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcard',
            name='active',
            field=models.BooleanField(verbose_name='Доступен для заказа'),
        ),
        migrations.AlterField(
            model_name='bookcard',
            name='age_restrictions',
            field=models.CharField(max_length=4, verbose_name='Возрастные ограничения'),
        ),
        migrations.AlterField(
            model_name='bookcard',
            name='authors',
            field=models.ManyToManyField(to='app_reference_book.authors', verbose_name='Авторы книги'),
        ),
        migrations.AlterField(
            model_name='bookcard',
            name='availability',
            field=models.PositiveSmallIntegerField(verbose_name='Количество книг в наличии'),
        ),
        migrations.AlterField(
            model_name='bookcard',
            name='cover',
            field=models.CharField(max_length=100, verbose_name='Переплет'),
        ),
        migrations.AlterField(
            model_name='bookcard',
            name='format',
            field=models.CharField(max_length=100, verbose_name='Формат'),
        ),
        migrations.AlterField(
            model_name='bookcard',
            name='genre',
            field=models.ManyToManyField(to='app_reference_book.genres', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='bookcard',
            name='isbn',
            field=models.CharField(max_length=100, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='bookcard',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название книги'),
        ),
        migrations.AlterField(
            model_name='bookcard',
            name='pages',
            field=models.PositiveSmallIntegerField(verbose_name='Страниц'),
        ),
        migrations.AlterField(
            model_name='bookcard',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='upload/books/', verbose_name='Фото обложки'),
        ),
        migrations.AlterField(
            model_name='bookcard',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Цена (BYN)'),
        ),
        migrations.AlterField(
            model_name='bookcard',
            name='publishing',
            field=models.ManyToManyField(to='app_reference_book.publishinghouse', verbose_name='Издательство'),
        ),
        migrations.AlterField(
            model_name='bookcard',
            name='rating',
            field=models.PositiveSmallIntegerField(verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='bookcard',
            name='serie',
            field=models.ManyToManyField(to='app_reference_book.series', verbose_name='Серия'),
        ),
        migrations.AlterField(
            model_name='bookcard',
            name='weight',
            field=models.PositiveSmallIntegerField(verbose_name='Вес (гр)'),
        ),
        migrations.AlterField(
            model_name='bookcard',
            name='year_of_publishing',
            field=models.PositiveSmallIntegerField(verbose_name='Год издания'),
        ),
    ]
