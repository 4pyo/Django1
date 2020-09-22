from django.shortcuts import render
from .models import Product
# Create your views here.
def product_list(request):
    product_list = Product.objects.all()
    context = {
        'Product_list': product_list
    }
    return render (request , 'product/product_list.html' , context)
def product_detail(request , id):
    product_detail = Product.objects.filter(id = id)
    context = {
        'Product_detail':product_detail
    }
    return render (request , 'Product/product_detail.html' , context)
    