from django.urls import path
from .views import CategoryListView, CategoryDetailView

urlpatterns = [
    path('category_list', CategoryListView.as_view(),name='category_list'),
    path('category_detail/<slug:slug>', CategoryDetailView.as_view(),name='category_detail')
    
]