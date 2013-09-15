from django.contrib import admin

from gaz.product.models import Product, Fuel, Tank, Deposit, Company,\
        ProductGroup, MeasurementUnit, ProductBarcode


class ProductBarcodeInline(admin.TabularInline):
    model = ProductBarcode


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductBarcodeInline,
    ]


admin.site.register(MeasurementUnit)
admin.site.register(Company)
admin.site.register(ProductGroup)
admin.site.register(Product, ProductAdmin)
admin.site.register(Fuel)
admin.site.register(Tank)
admin.site.register(Deposit)
