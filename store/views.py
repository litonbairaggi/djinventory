from django.shortcuts import render, redirect

#from django.views.generic import TemplateView
# Create your views here.
from django.views.generic import ListView

from .models import Product

from . froms import ProductForm


# Product views
#@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/product-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_product.html', context)


class ProductListView(ListView):
    model = Product.objects.all()
    template_name = 'store/product_list.html'
    context_object_name = 'product'