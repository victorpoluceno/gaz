from django.db import models


class Company(models.Model):
    code = models.CharField(max_length=30, unique=True)
    cnpj = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    corporate_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


class Deposit(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    company = models.ForeignKey(Company)


class Tank(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company)


class ProductGroup(models.Model):
    name = models.CharField(max_length=30)


class Product(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    deposits = models.ManyToManyField(Deposit)
    group = models.ForeignKey(ProductGroup)
    price = models.FloatField()
    barcode = models.CharField(max_length=30)


class Fuel(models.Model):
    code = models.CharField(max_length=30, unique=True)
    code_anp = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    tank = models.ForeignKey(Tank)


class Pump(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)


class Nozzle(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    tank = models.ForeignKey(Tank)
    pump = models.ForeignKey(Pump)
