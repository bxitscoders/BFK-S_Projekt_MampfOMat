from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "preis", "beschreibung")


# Serializer für Bestellungen
class OrderSerializer(serializers.ModelSerializer):
    produkt_name = serializers.CharField(source="produkt.name", read_only=True)
    class Meta:
        model = Order
        fields = ("id", "produkt", "produkt_name", "menge", "kunde", "timestamp")