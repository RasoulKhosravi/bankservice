from django.db import models

# Create your models here.

class Atm(models.Model):
    name = models.CharField(max_length=264, unique=True)

class Bank(models.Model):
    name = models.CharField(max_length=264, unique=True)

class BankBranch(models.Model):
    name = models.CharField(max_length=264, unique=True)
    bank_id = models.ForeignKey(Bank)

class Customer(models.Model):
    name = models.CharField(max_length=264, unique=True)

class CustomerRegister(models.Model):
    bank_id = models.ForeignKey(Bank)
    bank_branch_id = models.ForeignKey(BankBranch)
    customer_id = models.ForeignKey(Customer)

class Employee(models.Model):
    name = models.CharField(max_length=264, unique=True)
    operation = models.CharField(max_length=264, unique=True)
    bank_branch_id = models.ForeignKey(BankBranch)

class Transaction(models.Model):
    bank_id = models.ForeignKey(Bank)
    bank_branch_id = models.ForeignKey(BankBranch)
    customer_id = models.ForeignKey(Customer)
    atm_id = models.ForeignKey(Atm)
    operation = models.CharField(max_length=264, unique=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)