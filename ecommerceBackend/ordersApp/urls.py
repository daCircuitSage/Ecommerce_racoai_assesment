from django.urls import path
from .views import (CheckoutView,
                    MyOrdersView,
                    OrderDetailView,
                    CancelOrderView)

urlpatterns = [
    path('orders/checkout/', CheckoutView.as_view(), name='checkout'),
    path('orders/checkout/cancel/<int:pk>/', CancelOrderView.as_view(), name='cancel_order_view'),
    path('orders/all', MyOrdersView.as_view(), name='all_orders'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    

    
]