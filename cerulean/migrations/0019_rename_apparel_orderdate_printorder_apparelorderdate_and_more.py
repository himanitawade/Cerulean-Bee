# Generated by Django 4.0 on 2022-04-22 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerulean', '0018_rename_phone_number_printorder_phonenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='printorder',
            old_name='apparel_orderdate',
            new_name='apparelorderdate',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='base_color',
            new_name='basecolor',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='blank_price',
            new_name='blankprice',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='color_change',
            new_name='colorchange',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='color_charge',
            new_name='colorcharge',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='color_list',
            new_name='colorlist',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='delivered_date',
            new_name='delivereddate',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='due_date',
            new_name='duedate',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='film_date',
            new_name='filmdate',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='final_cost',
            new_name='finalcost',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='l_charge',
            new_name='lcharge',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='l_number',
            new_name='lnumber',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='location_size',
            new_name='locationsize',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='m_charge',
            new_name='mcharge',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='m_number',
            new_name='mnumber',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='print_date',
            new_name='printdate',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='s_charge',
            new_name='scharge',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='s_number',
            new_name='setupcharge',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='setup_charge',
            new_name='snumber',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='total_cost',
            new_name='totalcost',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='unitbase_price',
            new_name='unitbaseprice',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='vendor_name',
            new_name='vendorname',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='xl_charge',
            new_name='xlcharge',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='xl_number',
            new_name='xlnumber',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='xs_charge',
            new_name='xscharge',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='xs_number',
            new_name='xsnumber',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='xxl_charge',
            new_name='xxlcharge',
        ),
        migrations.RenameField(
            model_name='printorder',
            old_name='xxl_number',
            new_name='xxlnumber',
        ),
    ]
