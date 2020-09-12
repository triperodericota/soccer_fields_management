# Generated by Django 3.1 on 2020-09-11 15:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoccerField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=30)),
                ('locker_room', models.BooleanField(verbose_name='Locker room')),
                ('ilumination', models.BooleanField()),
                ('syntehtic_grass', models.BooleanField(verbose_name='Synthetic Grass')),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=50)),
                ('employee', models.CharField(help_text='How did take the rental?', max_length=50)),
                ('rental_date', models.DateField(default=datetime.date(2020, 9, 11), verbose_name='Date')),
                ('turn', models.DateTimeField(help_text='When is the match going to play?')),
                ('soccer_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soccer_fields_management.soccerfield')),
            ],
        ),
    ]