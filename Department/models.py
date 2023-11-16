# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bill(models.Model):
    bid = models.IntegerField(db_column='BID', primary_key=True)  # Field name made lowercase.
    bdate = models.DateField(db_column='BDate', blank=True, null=True)  # Field name made lowercase.
    byear = models.IntegerField(db_column='BYear', blank=True, null=True)  # Field name made lowercase.
    bmonth = models.CharField(db_column='BMonth', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cusid = models.ForeignKey('Customer', models.DO_NOTHING, db_column='CUSId', blank=True, null=True)  # Field name made lowercase.
    current_reading = models.IntegerField(db_column='Current_Reading', blank=True, null=True)  # Field name made lowercase.
    prev_reading = models.IntegerField(db_column='Prev_Reading', blank=True, null=True)  # Field name made lowercase.
    bamount = models.FloatField(db_column='Bamount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'bill'


class Branch(models.Model):
    branch_id = models.IntegerField(db_column='Branch_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    status_b = models.IntegerField(db_column='Status_b')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'branch'


class Customer(models.Model):
    scno = models.IntegerField(db_column='SCNO', blank=True, null=True)  # Field name made lowercase.
    cusid = models.IntegerField(db_column='CUSID', primary_key=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mobileno = models.IntegerField(db_column='MobileNo', blank=True, null=True)  # Field name made lowercase.
    branch = models.ForeignKey(Branch, models.DO_NOTHING, db_column='Branch_Id', blank=True, null=True)  # Field name made lowercase.
    demand_type = models.ForeignKey('Demandtype', models.DO_NOTHING, db_column='Demand_type_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'customer'


class Demandrate(models.Model):
    drid = models.IntegerField(db_column='DRID', primary_key=True)  # Field name made lowercase.
    demand_type = models.ForeignKey('Demandtype', models.DO_NOTHING, db_column='Demand_type_ID', blank=True, null=True)  # Field name made lowercase.
    rate = models.FloatField(blank=True, null=True)
    effective_date = models.DateField(db_column='Effective_Date', blank=True, null=True)  # Field name made lowercase.
    iscurrent = models.IntegerField(db_column='IsCurrent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'demandrate'


class Demandtype(models.Model):
    demand_type_id = models.IntegerField(db_column='Demand_Type_ID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status_d = models.IntegerField(db_column='Status_d', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'demandtype'


class Payment(models.Model):
    pid = models.IntegerField(db_column='PID', primary_key=True)  # Field name made lowercase.
    bid = models.ForeignKey(Bill, models.DO_NOTHING, db_column='BId', blank=True, null=True)  # Field name made lowercase.
    pdate = models.DateField(db_column='PDate', blank=True, null=True)  # Field name made lowercase.
    pamount = models.FloatField(db_column='PAmount', blank=True, null=True)  # Field name made lowercase.
    payment_type = models.ForeignKey('PaymentOption', models.DO_NOTHING, db_column='Payment_Type_ID', blank=True, null=True)  # Field name made lowercase.
    rebate_amt = models.FloatField(db_column='Rebate_Amt', blank=True, null=True)  # Field name made lowercase.
    fine_amt = models.FloatField(db_column='Fine_Amt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'payment'


class PaymentOption(models.Model):
    poid = models.IntegerField(db_column='POID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    po_status = models.IntegerField(db_column='PO_Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'payment_option'
