from django.db.models import F, Sum, DecimalField
from rest_framework import serializers
from .models import Cart, CartItems
from productsApp.serializers import ProductListSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    sub_total = serializers.SerializerMethodField()
    class Meta:
        model = CartItems
        fields = ['id',
                  'product',
                  'quantity',
                  'sub_total']
        
    def get_sub_total(self, cartitem):
        totoal = cartitem.product.price * cartitem.quantity
        return totoal
        

class CartSerializer(serializers.ModelSerializer):
    cartitems = CartItemSerializer(read_only=True, many=True)
    cart_total = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'cartitems',
            'cart_total'
        ]

    def get_cart_total(self, cart):
        total = cart.cartitems.select_related('product').aggregate(
            total=Sum(
                F('quantity') * F('product__price'),
                output_field=DecimalField(max_digits=20, decimal_places=2),
            )
        )['total']
        return total or 0
    

class CartQuantitySerizlizer(serializers.ModelSerializer):
    total_quantity = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'total_quantity',
        ]
    
    def get_total_quantity(self, cart):
        total = cart.cartitems.aggregate(total=Sum('quantity'))['total']
        return total or 0