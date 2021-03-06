from django import forms
from django.forms import widgets

from . models import Product, Supplier, Customer, Purchase, Sell, Setting 

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'company_name', 'supplier_email','supplier_phone', 'supplier_address']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'company_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company name'}),
            'supplier_email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Supplier email'}),
            'supplier_phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Supplier phone'}),
            'supplier_address':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Supplier address', 'rows':8})
        }
        labels={
            'name':'Your Name',
            'company_name':'Company Name',
            'supplier_email':'Email',
            'supplier_phone':'Your Phone',
            'supplier_address':'Address',
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_code', 'bying_price', 'selling_price']
        widgets = {
            'name': forms.TextInput(attrs={"placeholder": "name",'class': 'form-control','id': 'name'}),
            'product_code': forms.TextInput(attrs={"placeholder": "Product code",'class': 'form-control','id': 'product_code'}),
            'bying_price': forms.NumberInput(attrs={"placeholder": "Bying price",'class': 'form-control','id': 'bying_price'}),
            'selling_price': forms.NumberInput(attrs={"placeholder": "Selling price",'class': 'form-control','id': 'selling_price'})
        }
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer 
        fields = ['name', 'customer_email', 'customer_phone', 'customer_address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Customer email'}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer phone'}),
            'customer_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Customer address', 'rows':4})
        }
        labels={
            'name':'Name',
            'customer_email':'Email',
            'customer_phone':'Phone',
            'customer_address':'Address',
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase 
        fields = ['product', 'supplier', 'product_quantity', 'status']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'product_quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }
        labels={
            'product':'Product',
            'supplier':'Supplier',
            'product_quantity':'Quantity',
            'status':'Status',
        }

class SellForm(forms.ModelForm):
    class Meta:
        model = Sell 
        fields = ['product', 'customer', 'product_quantity', 'description', 'status']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'product_quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write something'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }
        labels={
            'product':'Product',
            'customer':'Customer',
            'product_quantity':'Quantity',
            'description':'Description',
            'status':'Status',
        }
  
class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting 
        fields = ['company_name', 'logo', 'email', 'facebook', 'phone', 'address']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'logo': forms.FileInput(),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'facebook'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'address'}),
        }
        labels={
            'company_name':'Company name',
            'logo':'Company logo',
            'email':'Company email',
            'facebook':'Company facebook',
            'phone':'Company phone',
            'address':'Company Address',
        }       
    