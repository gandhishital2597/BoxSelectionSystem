from django.contrib import admin

# Register your models here.

from .models import Product, Box, Order, OrderItem
admin.site.register(Product)
admin.site.register(Box)
admin.site.register(Order)
admin.site.register(OrderItem)