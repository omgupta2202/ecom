from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.models import Cart, CartItem
from products.models import Product

def place_order(request):
    if request.method == 'POST':
        user = request.user
        cart = Cart.objects.get(user=user)
        cart_items = cart.cartitem_set.all()

        # Create an order instance for the user
        order = Order.objects.create(user=user)

        # Loop through cart items and add them to the order
        for cart_item in cart_items:
            # Associate the cart item with the order
            cart_item.order = order
            cart_item.save()

        # Clear the cart items after placing the order
        cart_items.delete()

        return redirect('orders:order_history')  # Redirect to order history
    else:
        cart_items = CartItem.objects.filter(cart__user=request.user)
        return render(request, 'orders/place_order.html', {'cart_items': cart_items})



def order_history(request):
    if request.user.is_authenticated:
        user = request.user
        orders = Order.objects.filter(user=user).prefetch_related('items__product')  # Retrieve orders and related items
        return render(request, 'orders/order_history.html', {'orders': orders})
    else:
        return redirect('accounts:user_login')

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})
