from django import template

register = template.Library()

@register.filter
def total_price(cart_items):
    return sum(item.product.price * item.quantity for item in cart_items)

@register.filter
def calculate_subtotal(cart_item):
    return cart_item.product.price * cart_item.quantity