# Generated by Django 4.1.2 on 2022-12-11 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_accounts', '0005_alter_userextension_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userextension',
            options={'permissions': (('access_for_managers_admin', 'Managers and admin can see it'),)},
        ),
    ]