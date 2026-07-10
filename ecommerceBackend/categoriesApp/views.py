from django.shortcuts import render, get_object_or_404
#model and serialisers
from .models import Category
from .serializers import (CategoryDetailSerializer, CategoryListSerializer)
from productsApp.models import Product
from productsApp.serializers import ProductListSerializer
from .utils import category_descendants

#views, responses, status
from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView)
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page





@method_decorator(cache_page(60 * 5), name='dispatch')
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


@method_decorator(cache_page(60 * 5), name='dispatch')
class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.prefetch_related('products').all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'slug'


@method_decorator(cache_page(60 * 5), name='dispatch')
class CategoryProductsView(ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=slug)

        cats = Category.objects.values_list('id', 'parent_id')
        desc = category_descendants(cats, category.id)
        ids = list(desc) + [category.id]

        return Product.objects.filter(category_id__in=ids).select_related('category')
