# Generated by Django 4.1.2 on 2022-10-10 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
