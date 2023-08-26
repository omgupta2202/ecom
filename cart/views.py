from django.shortcuts import get_object_or_404, redirect
from .models import Cart, CartItem
from products.models import Product  # Import the Product model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponse

@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        cart, created = Cart.objects.get_or_create(user=request.user)
        product = get_object_or_404(Product, pk=product_id)
        
        quantity = request.POST.get('quantity', 1)  # Default to 1 if not specified
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError("Quantity must be a positive integer")
        except ValueError:
            return HttpResponse("Invalid quantity")
        
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()
        return redirect('cart:view_cart')
    else:
        return HttpResponse("Invalid request method")



@login_required
def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    if cart_item.cart.user == request.user:
        quantity = request.POST.get('quantity')
        cart_item.quantity = quantity
        cart_item.save()
    return redirect('cart:view_cart')  # Redirect to cart view

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    if cart_item.cart.user == request.user:
        cart_item.delete()
    return redirect('cart:view_cart')  # Redirect to cart view

@login_required
def view_cart(request):
    user = request.user
    if user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=user)
        cart_items = cart.cartitem_set.all()
        cart_items_count = cart_items.count()
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        return render(request, 'cart/view_cart.html', {'cart_items': cart_items, 'total_price': total_price, 'cart_items_count': cart_items_count})
    else:
        return HttpResponse("Please log in to view your cart.")

