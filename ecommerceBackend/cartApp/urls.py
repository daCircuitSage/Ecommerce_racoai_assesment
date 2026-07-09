from django.urls import path
from .views import AddToCart, UpdateItemQuantity, DeleteCartItem
urlpatterns = [
    path('add_to_cart/', AddToCart.as_view(), name='add_to_cart'),
    path('update_quantity/', UpdateItemQuantity.as_view(), name='update_quantity'),
    path('delete_cartitem/<int:pk>/', DeleteCartItem.as_view(),name='delete_cartitem'),

]