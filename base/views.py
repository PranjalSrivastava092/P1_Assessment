# views.py (inside the base app)
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem, Order
from .serializers import CartSerializer, CartItemSerializer, OrderSerializer
from rest_framework import status
from rest_framework.response import Response

class CartItemCreateView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cart = self.request.user.cart
        product = serializer.validated_data['product']
        quantity = serializer.validated_data.get('quantity', 1)

        if product.quantity < quantity:
            return Response({"error": "Not enough quantity available"}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(cart=cart)

        # Update the quantity of the product
        product.quantity -= quantity
        product.save()


class CartDetailView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.cart

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderHistoryView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

