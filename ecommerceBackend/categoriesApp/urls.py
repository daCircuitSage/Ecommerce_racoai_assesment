from django.urls import path
from .views import CategoryListView, CategoryDetailView, CategoryProductsView

urlpatterns = [
    path('category_list', CategoryListView.as_view(), name='category_list'),
    path('category_detail/<slug:slug>', CategoryDetailView.as_view(), name='category_detail'),
    path('category/<slug:slug>/products', CategoryProductsView.as_view(), name='category_products'),
]