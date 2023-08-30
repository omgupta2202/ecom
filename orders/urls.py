from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('place-order/', views.place_order, name='place_order'),
    path('order-history/', views.order_history, name='order_history'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
]
