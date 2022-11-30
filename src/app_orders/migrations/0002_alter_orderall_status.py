# Generated by Django 4.1.2 on 2022-11-24 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_book', '0007_status'),
        ('app_orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderall',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order', to='app_reference_book.status', verbose_name='Статус заказа'),
        ),
    ]
