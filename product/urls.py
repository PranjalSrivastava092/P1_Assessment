from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView, CategoryCreateView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('categories/', CategoryCreateView.as_view(), name='category-create')
]