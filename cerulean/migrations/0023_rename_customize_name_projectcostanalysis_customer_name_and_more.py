# Generated by Django 4.0 on 2022-04-23 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerulean', '0022_rename_art_date_printorder_artdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectcostanalysis',
            old_name='customize_name',
            new_name='customer_name',
        ),
        migrations.RenameField(
            model_name='projectcostanalysis',
            old_name='lc_rvenue_02',
            new_name='lc_revenue_02',
        ),
        migrations.RenameField(
            model_name='projectcostanalysis',
            old_name='phone_number',
            new_name='phonenumber',
        ),
    ]