
from rest_framework import viewsets
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer


# ViewSet für Bestellungen
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by("-timestamp")
    serializer_class = OrderSerializer