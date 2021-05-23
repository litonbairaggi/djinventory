from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import (
    create_supplier,
    
    SupplierCreateView,
    SupplierListView,
    SupplierEditView,
    SupplierDeleteView,

    ProductCreateView,
    ProductListView,
    ProductEditView,
    ProductDeleteView,

    CustomerCreateView,
    CustomerListView,
    CustomerEditView,
    CustomerDeleteView,

    PurchaseCreateView,
    PurchaseListView,
    PurchaseEditView,
    PurchaseDeleteView,
)
app_name="store"
urlpatterns = [
    # path('create_product/', create_product, name='create_product'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    # path('create_supplier/', create_supplier, name='create_supplier'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_edit/<int:pk>/', ProductEditView.as_view(), name='product_edit'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('create_supplier/', SupplierCreateView.as_view(), name='create_supplier'),
    path('supplier_list/', SupplierListView.as_view(), name='supplier_list'),
    path('supplier_edit/<int:pk>/', SupplierEditView.as_view(), name='supplier_edit'),
    path('supplier_delete/<int:pk>/', SupplierDeleteView.as_view(), name='supplier_delete'),

    path('create_customer/', CustomerCreateView.as_view(), name='create_customer'),
    path('customer_list/', CustomerListView.as_view(), name='customer_list'),
    path('customer_edit/<int:pk>/', CustomerEditView.as_view(), name='customer_edit'),
    path('customer_delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),

    path('create_purchase/', PurchaseCreateView.as_view(), name='create_purchase'),
    path('purchase_list/', PurchaseListView.as_view(), name='purchase_list'),
    path('purchase_edit/<int:pk>/', PurchaseEditView.as_view(), name='purchase_edit'),
    path('purchase_delete/<int:pk>/', PurchaseDeleteView.as_view(), name='purchase_delete'),
]
