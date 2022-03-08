"""Products Views"""
from django.shortcuts import render, get_object_or_404
from .models import Products


def all_products(request):
    """View to show all products, including sorting and search"""

    products = Products.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """View to show product details"""

    product = get_object_or_404(Products, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
