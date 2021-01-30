# Generated by Django 3.1.5 on 2021-01-29 23:50

from django.db import migrations, models
import main_gusto.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_gusto', '0005_auto_20210126_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='weight',
            field=models.IntegerField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='photo',
            field=models.ImageField(null=True, upload_to=main_gusto.models.Dish.get_file_name_dishes),
        ),
    ]
