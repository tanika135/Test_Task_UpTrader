# Generated by Django 4.2.7 on 2023-11-23 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_menu', '0006_menuitem_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='url',
        ),
    ]
