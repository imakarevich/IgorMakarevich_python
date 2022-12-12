# Generated by Django 4.1.2 on 2022-12-12 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_product_books', '0011_alter_bookcard_publishing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcard',
            name='rating',
        ),
        migrations.CreateModel(
            name='BookComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Рейтинг')),
                ('comment', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='book_comments', to=settings.AUTH_USER_MODEL, verbose_name='Комментарий пользователя')),
            ],
        ),
        migrations.AddField(
            model_name='bookcard',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bookcard', to='app_product_books.bookcomments', verbose_name='Комментарии'),
        ),
    ]
