from django.db import models
from django.contrib.auth.models import User
from products.models import Product  # Import the Product model

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other fields like total price, created_at, etc.

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)  # Default value
