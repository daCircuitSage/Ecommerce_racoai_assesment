from django.shortcuts import render
#model and serialisers
from .models import Category
from .serializers import (CategoryDetailSerializer, CategoryListSerializer)

#views, responses, status
from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView)
from rest_framework.response import Response
from rest_framework import status





class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'slug'