from distutils.sysconfig import customize_compiler
from re import T
from statistics import mode
from django.db import models
import datetime

# Create your models here.

class SystemUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,null=True,unique=True)
    email_id = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=20,null=True)

class ArtworkOrder(models.Model):
    customer_id	= models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=200,null=True)	
    email_id = models.CharField(max_length=200,null=True)	
    phone_number = models.CharField(max_length=20,null=True)	
    discount_rate = models.FloatField(null=True)
    order_date = models.DateField(null=True)
    approved_date = models.DateField(null=True)
    scheduled_print_date = models.DateField(null=True)	
    total_price	= models.FloatField(null=True)
    apparel_item = models.CharField(max_length=150,null=True)
    event_name = models.CharField(max_length=150,null=True)
    base_color	= models.CharField(max_length=50,null=True)
    theme_name	= models.CharField(max_length=150,null=True)
    max_colors	= models.CharField(max_length=150,null=True)
    art_location_01	= models.CharField(max_length=150,null=True)
    description_01 = models.CharField(max_length=1000,null=True)
    cost_01	= models.IntegerField(null=True)
    employee_01	= models.CharField(max_length=150,null=True)
    complete_date_01 = models.DateField(null=True)
    colors_01 = models.CharField(max_length=150,null=True)
    art_location_02	= models.CharField(max_length=150,blank=True,null=True)
    description_02	= models.CharField(max_length=1000,blank=True,null=True)
    cost_02	= models.IntegerField(blank=True,null=True)
    employee_02	= models.CharField(max_length=150,blank=True,null=True)
    complete_date_02 = models.DateField(blank=True,null=True)
    colors_02 = models.CharField(max_length=150,blank=True,null=True)


class EmployeeWorkDetails(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=50, null=True)
    employee_phone = models.CharField(max_length=50, null=True)
    work_type = models.CharField(max_length=50, null=True)
    pd_date_01 = models.DateField(blank=True,null=True)
    pd_start_time_01 = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    project_01 = models.CharField(max_length=50, null=True)
    art_item_01 = models.CharField(max_length=50, null=True)
    task_01 = models.CharField(max_length=50, null=True)
    end_time_01 = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    pd_date_02 = models.CharField(max_length=50, null=True)
    pd_start_time_02 = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    project_02 = models.CharField(max_length=50, null=True)
    art_item_02 = models.CharField(max_length=50, null=True)
    task_02 = models.CharField(max_length=50, null=True)
    end_time_02 = models.TimeField(auto_now=False, auto_now_add=False, null=True)



class PrintOrder(models.Model):

    customer_id	= models.AutoField(primary_key=True)
    customername = models.CharField(max_length=200,null=True)	
    emailid = models.CharField(max_length=200,null=True)	
    phonenumber = models.CharField(max_length=20,null=True)	
    orderdate = models.DateField(null=True)
    artdate = models.DateField(null=True)
    duedate = models.DateField(null=True)
    setupcharge = models.CharField(max_length=150,null=True)
    deposit = models.CharField(max_length=150,null=True)
    discount = models.CharField(max_length=150,null=True)
    totalcost = models.CharField(max_length=150,null=True)
    apparelorderdate = models.DateField(null=True)
    filmdate = models.DateField(null=True)
    printdate = models.DateField(null=True)
    delivereddate = models.DateField(null=True)
    basecolor = models.CharField(max_length=150,null=True)
    vendorname = models.CharField(max_length=150,null=True)
    xsnumber = models.CharField(max_length=150,null=True)
    xscharge = models.CharField(max_length=150,null=True)
    snumber = models.CharField(max_length=150,null=True)
    scharge = models.CharField(max_length=150,null=True)
    mnumber = models.CharField(max_length=150,null=True)
    mcharge = models.CharField(max_length=150,null=True)
    lnumber = models.CharField(max_length=150,null=True)
    lcharge = models.CharField(max_length=150,null=True)
    xlnumber = models.CharField(max_length=150,null=True)
    xlcharge = models.CharField(max_length=150,null=True)
    xxlnumber = models.CharField(max_length=150,null=True)
    xxlcharge = models.CharField(max_length=150,null=True)
    unitbaseprice = models.CharField(max_length=150,null=True)
    colorcharge = models.CharField(max_length=150,null=True)
    blankprice = models.CharField(max_length=150,null=True)
    locationsize = models.CharField(max_length=150,null=True)
    colorchange = models.CharField(max_length=150,null=True)
    colorlist = models.CharField(max_length=150,null=True)
    finalcost = models.CharField(max_length=150,null=True)

class ProjectCostAnalysis(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=150,null=True)
    event_name = models.CharField(max_length=150,null=True)
    item_name = models.CharField(max_length=150,null=True)
    customer_name = models.CharField(max_length=150,null=True)
    phonenumber = models.CharField(max_length=150,null=True)
    mc_item_01 = models.CharField(max_length=150,null=True)
    mc_unitcost_01 = models.CharField(max_length=150,null=True)
    mc_pricecharge_01 = models.CharField(max_length=150,null = True)
    mc_units_01 = models.CharField(max_length=150,null=True)
    mc_cost_01 = models.CharField(max_length=150,null=True)
    mc_revenue_01 = models.CharField(max_length=150,null=True)
    mc_item_02 = models.CharField(max_length=150,null=True)
    mc_unitcost_02 = models.CharField(max_length=150,null=True)
    mc_pricecharge_02 = models.CharField(max_length=150,null=True)
    mc_units_02 = models.CharField(max_length=150,null=True)
    mc_cost_02 = models.CharField(max_length=150,null=True)
    mc_revenue_02 = models.CharField(max_length=150,null=True)
    totalcost_01 = models.CharField(max_length=150,null=True)
    totalrevenue_01 = models.CharField(max_length=150,null=True)
    lc_item_01 = models.CharField(max_length=150,null=True)
    lc_unitcost_01 = models.CharField(max_length=150,null=True)
    lc_pricecharge_01 = models.CharField(max_length=150,null=True)
    lc_units_01 = models.CharField(max_length=150,null=True)
    lc_cost_01 = models.CharField(max_length=150,null=True)
    lc_revenue_01 = models.CharField(max_length=150,null=True)
    lc_item_02 = models.CharField(max_length=150,null=True)
    lc_unitcost_02 = models.CharField(max_length=150,null=True)
    lc_pricecharge_02 = models.CharField(max_length=150,null=True)
    lc_units_02 = models.CharField(max_length=150,null=True)
    lc_cost_02 = models.CharField(max_length=150,null=True)
    lc_revenue_02 = models.CharField(max_length=150,null=True)
    totalrevenue_02 = models.CharField(max_length=150,null=True)
    material_charge = models.CharField(max_length=150,null = True)
    artwork_fees = models.CharField(max_length=150,null=True)
    fixed_charges = models.CharField(max_length=150,null=True)
    total_discounts = models.CharField(max_length=150,null=True)
    net_profits = models.CharField(max_length=150,null=True)

