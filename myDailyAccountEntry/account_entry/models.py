from django.db import models

# Create your models here.

class account_database(models.Model):
    date = models.DateField()
    credit_debit = models.CharField(max_length=50)
    category = models.CharField(max_length=200)
    account = models.CharField(max_length=200)
    particular = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    notes = models.CharField(max_length=200, blank=True)

class category_list(models.Model):
    category = models.CharField(max_length=100)
    category_names = models.CharField(max_length=100)

class balance_sheet(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    rs500 = models.IntegerField()
    rs200 = models.IntegerField()
    rs100 = models.IntegerField()
    rs50 = models.IntegerField()
    rs20 = models.IntegerField()
    rs10 = models.IntegerField()
    rs5 = models.IntegerField()
    rs2 = models.IntegerField()
    rs1 = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status = models.CharField(max_length=50, blank=True)