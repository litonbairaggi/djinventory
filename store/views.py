from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http.response import HttpResponse
from django.views import View
from django.contrib import messages

# Create your views here.
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    View,
)    
from .models import (
    Product, 
    Supplier,
    Customer,
    Purchase,
    Sell,
    Setting,
) 
from . froms import (
    ProductForm,
    SupplierForm,
    CustomerForm,
    PurchaseForm,
    SellForm,
    SettingForm,
)

# Supplier views
class SupplierListView(ListView):
    model = Supplier
    template_name = 'store/list_supplier.html'
    context_object_name = 'suppliers'

class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'store/create_supplier.html' 
    def form_invalid(self, form):
        form.instance.user = self.request.user   
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('store:create_supplier')

def create_supplier(request):
    forms = SupplierForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('store/create_supplier')
    context = {
        'form': forms
    }
    return render(request, 'store/create_supplier.html', context) 

class SupplierEditView(UpdateView):
    model = Supplier 
    form_class = SupplierForm
    template_name = 'store/edit_supplier.html'
    def get_success_url(self):
        id= self.object.id
        return reverse_lazy('store:supplier_edit', kwargs={'pk':id})

class SupplierDeleteView(DeleteView):
    model = Supplier 
    template_name = 'store/delete_supplier.html'
    success_url = reverse_lazy('store:supplier_list')


class ProductListView(ListView):
    model = Product
    template_name = 'store/list_product.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product 
    form_class = ProductForm
    template_name = 'store/create_product.html'
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('store:create_product')    

# Product views
#@login_required(login_url='login')
# def create_product(request):
#     forms = ProductForm()
#     if request.method == 'POST':
#         forms = ProductForm(request.POST)
#         if forms.is_valid():
#             forms.save()
#             return redirect('/store/product_list')
#     else:
#         context ={
#             'form': forms
#         }
#     return render(request, 'store/product_list.html', context)            

class ProductEditView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'store/edit_product.html'
    def get_success_url(self):
        id= self.object.id
        return reverse_lazy('store:product_edit', kwargs={'pk':id})
  
class ProductDeleteView(DeleteView):
    model = Product
    template_name="store/delete_product.html"
    success_url = reverse_lazy('store:product_list')
    
# Customer    
class CustomerCreateView(CreateView):
    model = Customer 
    form_class = CustomerForm 
    template_name = 'store/create_customer.html'
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('store:create_customer')

class CustomerListView(ListView):
    model = Customer 
    template_name = 'store/list_customer.html'
    context_object_name = 'customers'

class CustomerEditView(UpdateView):
    model = Customer 
    form_class = CustomerForm
    template_name = 'store/edit_customer.html'
    def get_success_url(self):
        id = self.object.id
        return reverse_lazy('store:customer_edit', kwargs={'pk':id})

class CustomerDeleteView(DeleteView):
    model = Customer 
    template_name = 'store/delete_customer.html'
    success_url = reverse_lazy('store:customer_list')

class PurchaseCreateView(CreateView):
    model = Purchase 
    form_class = PurchaseForm
    template_name = 'store/create_purchase.html'
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)
    def get_success_url(self):
        return reverse_lazy('store:create_purchase')    

class PurchaseListView(ListView):
    model = Purchase 
    template_name = 'store/list_purchase.html'
    context_object_name = 'purchases'

class PurchaseEditView(UpdateView):
    model = Purchase 
    form_class = PurchaseForm
    template_name = 'store/edit_purchase.html'
    def get_success_url(self):
        id = self.object.id
        return reverse_lazy('store:purchase_edit', kwargs={'pk':id})

class PurchaseDeleteView(DeleteView):
    model = Purchase 
    template_name = 'store/delete_purchase.html'
    success_url = reverse_lazy('store:purchase_list')

# Sell
class SellCreateView(CreateView):
    model = Sell 
    form_class = SellForm
    template_name = 'store/create_sell.html'   
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)
    def get_success_url(self):
        id = self.object.id
        return reverse_lazy('store:create_sell')  
class SellListView(ListView):
    model = Sell 
    template_name = 'store/list_sell.html' 
    context_object_name = 'sells' 
class SellEditView(UpdateView):
    model = Sell 
    form_class = SellForm
    template_name = 'store/edit_sell.html'  
    def get_success_url(self):   
        id = self.object.id
        return reverse_lazy('store:sell_edit', kwargs={'pk':id})
class SellDeleteView(DeleteView):
    model = Sell 
    template_name = 'store/delete_sell.html'
    success_url = reverse_lazy('store:sell_list')

# Settings 
class SettingCreateView(CreateView): 
    model = Setting
    form_class = SettingForm
    template_name = 'store/create_settings.html'
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)
    def get_success_url(self):
        id = self.object.id
        return reverse_lazy('store:create_settings')    