from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=30)


class Deposit(models.Model):
    name = models.CharField(max_length=30)


class MeasurementUnit(models.Model):
    name = models.CharField(max_length=30)


class ProductGroup(models.Model):
    name = models.CharField(max_length=30)


class Product(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, blank=True)
    deposits = models.ManyToManyField(Deposit)
    group = models.ForeignKey(ProductGroup)
    price = models.FloatField()
    unit = models.ForeignKey(MeasurementUnit)


class ProductBarcode(models.Model):
    code = models.CharField(max_length=30)
    product = models.ForeignKey(Product)


class Fuel(models.Model):
    code = models.CharField(max_length=30, unique=True)
    code_anp = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    unit = models.ForeignKey(MeasurementUnit)
    price = models.FloatField()


class Tank(models.Model):
    code = models.CharField(max_length=30, unique=True)
    company = models.ForeignKey(Company, blank=True)
    description = models.CharField(max_length=30)
    fuel = models.ForeignKey(Fuel)


class Bico(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    tank = models.ForeignKey(Tank)
