from django.shortcuts import render, redirect

#from django.views.generic import TemplateView
# Create your views here.
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    View,
)

from .models import Product

from . froms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'store/list_product.html'
    context_object_name = 'products'


# Product views
#@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/store/create-product')
    context = {
        'form': forms
    }
    return render(request, 'store/create_product.html', context)

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'product_code', 'bying_price', 'selling_price']
    template_name = 'store/edit_product.html'