from django.contrib import admin

from gaz.product.models import Product, Fuel, Tank, Deposit, Company,\
        ProductGroup, Pump, Nozzle



admin.site.register(Company)
admin.site.register(ProductGroup)
admin.site.register(Product)
admin.site.register(Fuel)
admin.site.register(Tank)
admin.site.register(Deposit)
admin.site.register(Pump)
admin.site.register(Nozzle)
