from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required
def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/all_products.html', {'products': products})

@login_required
def home_view(request):
    return render(request, 'accounts/profile.html')


