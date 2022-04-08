"""Checkout View"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """Checkout View"""
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KmI7nEliIrUhfhTsSRBAClkhpQg2DWTHBntfefm03IEul5Kh1ycjtkDE40wjAP17vJ17e5c1eugRBOi1vNAUgrE00oAyyxGYq',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
