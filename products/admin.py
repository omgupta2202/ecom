from django.contrib import admin
from .models import Category, Tag, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')  # Display these fields in the admin list view

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product, ProductAdmin)
