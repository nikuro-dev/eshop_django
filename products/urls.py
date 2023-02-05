from django.urls import path
from products.views import product_list, product_detail

#urls here

urlpatterns = [
    path('list', product_list),
    path('<slug:slug>', product_detail, name='product_detail'),
]
