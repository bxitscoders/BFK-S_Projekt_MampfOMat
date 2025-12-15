from django.conf import settings
from django.db import models

class Product(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    preis = models.DecimalField(max_digits=6, decimal_places=2)
    beschreibung = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "produkte"
        verbose_name = "Produkt"
        verbose_name_plural = "Produkte"

    def __str__(self):
        return self.name
    
    # Bestellungen (Order)
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    produkt = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders")
    menge = models.PositiveIntegerField(default=1)
    kunde = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "bestellungen"
        verbose_name = "Bestellung"
        verbose_name_plural = "Bestellungen"

    def __str__(self):
        return f"{self.kunde or 'Unbekannt'} bestellt {self.menge}x {self.produkt.name} am {self.timestamp:%Y-%m-%d %H:%M}"

