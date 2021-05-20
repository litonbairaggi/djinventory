from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True, blank=False)
    product_code = models.CharField(max_length=32, blank=False)
    bying_price = models.PositiveIntegerField(default=0)
    selling_price = models.PositiveIntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=120, blank=False)
    company_name = models.CharField(max_length=120, unique=True, blank=False)
    supplier_email = models.EmailField(max_length=64, blank=False)
    supplier_phone = models.CharField(max_length=120, unique=True, blank=False)
    supplier_address = models.CharField(max_length=120, blank=False)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
