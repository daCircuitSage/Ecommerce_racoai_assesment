#model and serialisers
from .models import (Cart,
                     CartItems)
from productsApp.models import Product
from .serializers import (CartSerializer,
                          CartItemSerializer,
                          CartQuantitySerizlizer)

#views, responses, status
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

#pemissions
from rest_framework.permissions import IsAuthenticated


class AddToCart(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        product_id = request.data.get('product_id')
        cart, created = Cart.objects.prefetch_related('cartitems__product').get_or_create(user=request.user)
        product = get_object_or_404(Product, id=product_id)
        cartitem, created = CartItems.objects.get_or_create(
            cart=cart,
            product=product
        )
        if created:
            cartitem.quantity = 1
        else:
            cartitem.quantity += 1

        cartitem.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateItemQuantity(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request):
        cartitem_id = request.data.get('item_id')
        quantity = int(request.data.get('quantity'))

        cart_item = get_object_or_404(CartItems.objects.select_related('product'), id=cartitem_id, cart__user=request.user)
        if quantity < 1:
            return Response(
                {'detail': 'quantity must be at least 1'},
                status=status.HTTP_400_BAD_REQUEST
            )
        cart_item.quantity = quantity
        cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response({
            'data':serializer.data,
            'message':'cart item updated!',},
            status=status.HTTP_200_OK)

class DeleteCartItem(DestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItems.objects.filter(
            cart__user=self.request.user
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(
            {"message": "Cart item deleted successfully."},
            status=status.HTTP_200_OK
        )
