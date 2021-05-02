from django import forms
from . models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_code', 'bying_price', 'selling_price']
        widgets = {
            'name': forms.TextInput(attrs={
                "placeholder": "name",
                'class': 'form-control', 
                'id': 'name'
            }),
            'product_code': forms.TextInput(attrs={
                "placeholder": "Product code",
                'class': 'form-control', 
                'id': 'product_code'
            }),
            'bying_price': forms.NumberInput(attrs={
                "placeholder": "Bying price",
                'class': 'form-control', 
                'id': 'bying_price'
            }),
            'selling_price': forms.NumberInput(attrs={
                "placeholder": "Selling price",
                'class': 'form-control', 
                'id': 'selling_price'
            })
        }