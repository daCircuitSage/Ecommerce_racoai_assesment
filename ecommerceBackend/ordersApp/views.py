from django.shortcuts import render
#response and status and permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import transaction
#view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView

#models and serializers
from cartApp.models import Cart
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer

#payment factory
from paymentsApp.services import payment_factory


class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]
    @transaction.atomic
    def post(self, request):
        cart = get_object_or_404(Cart, user=request.user)
        cart_items = cart.cartitems.all()

        if not cart_items.exists():
            return Response(
                {'detail':'your cart is empty'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        order = Order.objects.create(
            user=request.user,
            total_price = 0
        )
        total_price = 0

        for item in cart_items:

            #checking the stock---
            if item.product.stock < item.quantity:
                return Response(
                    {
                        'message':f'{item.product.name} is out of stock'
                    },
                    status= status.HTTP_400_BAD_REQUEST
                )

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            total_price += item.product.price * item.quantity

        order.total_price = total_price
        order.save()

        provider = request.data.get('provider', 'stripe')
        if not provider:
            return Response(
                {'message':'payment provider is required!'},
                status= status.HTTP_400_BAD_REQUEST
            )
        try:
            strategy = payment_factory.PaymentFactory.get_payment_strategy(provider)
        except ValueError as e:
            return Response(
                {'message':str(e)},
                status= status.HTTP_400_BAD_REQUEST
            )
        
        payment_data = strategy.create_payment(order)

        return Response(
            {
                'message':'proceed to payment',
                'order':OrderSerializer(order).data,
                'checkout_url':payment_data['checkout_url'],
            },
            status=status.HTTP_200_OK
        )

class MyOrdersView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-created_at")
    

class OrderDetailView(RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    

class CancelOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):

        order = get_object_or_404(
            Order,
            id=pk,
            user=request.user
        )

        if order.status != Order.Status.PENDING:
            return Response(
                {'message':"only pending order can be cancelled!"},
                status= status.HTTP_400_BAD_REQUEST
            )

        order.status = Order.Status.CANCELLED
        order.save()

        return Response(
            {
                "message": "Order cancelled successfully."
            },
            status=status.HTTP_200_OK
        )