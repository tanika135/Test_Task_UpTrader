# Generated by Django 4.2.7 on 2023-11-23 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_menu', '0007_remove_menuitem_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='url_old',
            new_name='url',
        ),
    ]
