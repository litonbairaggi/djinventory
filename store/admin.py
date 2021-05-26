from django.contrib import admin

# Register your models here.
from . models import (
    Product,
    Supplier,
    Customer, 
    Purchase, 
    Sell, 
    Setting
    )
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'product_code', 'bying_price', 'selling_price']


admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Purchase)
admin.site.register(Sell)
admin.site.register(Setting)