from django.shortcuts import render
from .models import Products

# Create your views here.
def all_products(request):
    """View to show all products, including sorting and search"""

    products = Products.objects.all()

    context = {
        'products':products,
    }
    return render(request, 'products/products.html', context)
