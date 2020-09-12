# Generated by Django 3.1 on 2020-09-11 15:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('soccer_fields_management', '0002_auto_20200911_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='rental_date',
            field=models.DateField(default=datetime.datetime(2020, 9, 11, 15, 42, 51, 497789, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='turn',
            field=models.DateTimeField(help_text='When is the match going to play?', verbose_name='Date and Time Turn'),
        ),
    ]
