# Generated by Django 4.1.2 on 2022-11-30 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_book', '0008_alter_genres_description_alter_genres_name_and_more'),
        ('app_product_books', '0010_alter_bookcard_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcard',
            name='publishing',
            field=models.ManyToManyField(related_name='Book', to='app_reference_book.publishinghouse', verbose_name='Издательство'),
        ),
    ]
