# Generated by Django 3.1.5 on 2021-01-26 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_gusto', '0003_dish_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_oreder',
            new_name='category_order',
        ),
    ]
