from django.contrib import admin

# Register your models here.
from . models import (
    Product, Supplier
    )
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'product_code', 'bying_price', 'selling_price']


admin.site.register(Supplier)