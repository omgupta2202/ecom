from .models import UserProfile  # Import the UserProfile model
from cart.models import Cart

def cart_items_count(request):
    cart_items_count = 0
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items_count = cart.cartitem_set.count()
    return {'cart_items_count': cart_items_count}

def user_profile_context(request):
    user_profile = None

    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)

    return {'user_profile': user_profile}
