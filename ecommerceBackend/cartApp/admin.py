from django.contrib import admin
from .models import Cart, CartItems

class CartAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'created_at',
        'updated_at'
    )
admin.site.register(Cart, CartAdmin)


class CartItemsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cart',
        'product',
        # 'price',
        'quantity'
    )
admin.site.register(CartItems, CartItemsAdmin)

