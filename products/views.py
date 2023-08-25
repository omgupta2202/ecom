from django.shortcuts import render
from .models import Product


def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/all_products.html', {'products': products})

def home_view(request):
    return render(request, 'accounts/profile.html')


