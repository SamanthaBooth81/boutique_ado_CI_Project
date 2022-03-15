""" Shopping Bag Views """
from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """View to return the shopping bag contents page"""
    return render(request, 'bag/bag.html')
