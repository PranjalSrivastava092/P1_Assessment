from django.urls import path
from .views import CartItemCreateView, CartDetailView, OrderCreateView, OrderHistoryView

urlpatterns = [
    path('cart/items/', CartItemCreateView.as_view(), name='cart-item-create'),
    path('cart/', CartDetailView.as_view(), name='cart-detail'),
    path('order/', OrderCreateView.as_view(), name='order-create'),
    path('order/history/', OrderHistoryView.as_view(), name='order-history'),
]
