from django.shortcuts import render
# model and serializers
from .models import Product
from .serializers import (ProductDetailSerializer, ProductListSerializer)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# views, responses, status
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)
from rest_framework.response import Response
from rest_framework import status

# permissions and authentications
from .permissions import IsAdminUserOnly
from rest_framework.permissions import IsAuthenticated


@method_decorator(cache_page(60 * 5), name='dispatch')
class ProductListView(ListAPIView):
    queryset = Product.objects.filter(featured=True)
    serializer_class = ProductListSerializer


@method_decorator(cache_page(60 * 5), name='dispatch')
class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = "slug"


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

    permission_classes = [IsAuthenticated, IsAdminUserOnly]


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = "slug"

    permission_classes = [IsAuthenticated, IsAdminUserOnly]


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = "slug"

    permission_classes = [IsAuthenticated, IsAdminUserOnly]

