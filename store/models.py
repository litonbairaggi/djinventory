from django.db import models
from django.utils.timezone import now
from PIL import Image

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=120, unique=True, blank=False)
    product_code = models.CharField(max_length=32, blank=False)
    bying_price = models.PositiveIntegerField(default=0)
    selling_price = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=120, blank=False)
    company_name = models.CharField(max_length=120, unique=True, blank=False)
    supplier_email = models.EmailField(max_length=64, blank=False)
    supplier_phone = models.CharField(max_length=120, unique=True, blank=False)
    supplier_address = models.CharField(max_length=120, blank=False)
    created_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=120, blank=False)
    customer_email = models.EmailField(max_length=64, unique=True, blank=False)
    customer_phone = models.CharField(max_length=17, unique=True, blank=False)
    customer_address = models.CharField(max_length=120, blank=False)
    created_date = models.DateTimeField(default=now)
    def __str__(self):
        return self.name

    
class Purchase(models.Model):
    STATUS =(
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product_quantity = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=100, choices=STATUS, default='paid') 
    created_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.product.name 

class Sell(models.Model):
    STATUS =(
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=200, blank= False)
    status = models.CharField(max_length=100, choices=STATUS, default='paid')
    created_date = models.DateTimeField(default=now)

class Setting(models.Model):
    company_name = models.CharField(max_length=100, blank=False)
    logo = models.ImageField(upload_to='logoimg/',blank=False)
    email = models.EmailField(max_length=64, blank=False)
    facebook = models.CharField(max_length=64, blank=True)
    phone = models.CharField(max_length=32, blank=True)
    address = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(default=now)

    def save(self):
        # count will have all of the objects from the Seeting model
        count = Setting.objects.all().count()
        # this will check if the variable exist so we can update the existing ones
        save_permission = Setting.has_add_permission(self)

        # if there's more than two objects it will not save them in the database
        if count < 1:
            super(Setting, self).save()
        elif save_permission:
            super(Setting, self).save()

    def has_add_permission(self):
        return Setting.objects.filter(id=self.id).exists()
    