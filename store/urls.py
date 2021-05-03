from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

from .views import (
    create_product,
    ProductListView,
)

urlpatterns = [
    path('create-product/', views.create_product, name='create-product'),
    
    path('product-list/', views.ProductListView.as_view(), name='product-list'),
]



