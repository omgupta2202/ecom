from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    
    path('', views.all_products, name='all_products'),
    path('all-products/', views.all_products, name='all_products'),
    
]
