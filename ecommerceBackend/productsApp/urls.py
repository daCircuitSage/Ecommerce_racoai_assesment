from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
)


urlpatterns = [
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
    path("products/<slug:slug>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<slug:slug>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]