# Generated by Django 4.0 on 2022-04-22 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerulean', '0017_employeeworkdetails_end_time_02_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='printorder',
            old_name='phone_number',
            new_name='phonenumber',
        ),
    ]
