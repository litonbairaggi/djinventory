from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import (
    create_supplier,
    
    SupplierListView,
    ProductCreateView,
    ProductListView,
    ProductEditView,
    ProductDeleteView,
)
app_name="store"
urlpatterns = [
    # path('create_product/', create_product, name='create_product'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('create_supplier/', create_supplier, name='create_supplier'),

    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_edit/<int:pk>/', ProductEditView.as_view(), name='product_edit'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('supplier_list/', SupplierListView.as_view(), name='supplier_list'),
]
