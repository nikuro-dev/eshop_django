from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Avg
from .models import Product
# Create your views here.

def product_list(request):
    products = Product.objects.all().order_by('price')
    return render(request, 'product_module/product_list.html',{
        "products":products,
        
    })

def product_detail(request, slug):
    product = get_object_or_404(Product,slug=slug)
    return render(request,'product_module/product_detail.html',{
        'product': product
    })
