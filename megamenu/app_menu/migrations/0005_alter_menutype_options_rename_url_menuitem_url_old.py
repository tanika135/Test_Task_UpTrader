# Generated by Django 4.2.7 on 2023-11-23 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_menu', '0004_menutype_menuitem_menu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menutype',
            options={'verbose_name': 'Тип меню', 'verbose_name_plural': 'Типы меню'},
        ),
        migrations.RenameField(
            model_name='menuitem',
            old_name='url',
            new_name='url_old',
        ),
    ]
