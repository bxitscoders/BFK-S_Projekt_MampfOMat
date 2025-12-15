from django.urls import include, path
from rest_framework import routers
from .views import ProductViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r"produkte", ProductViewSet, basename="produkt")
router.register(r"bestellungen", OrderViewSet, basename="bestellung")

urlpatterns = [
    path("", include(router.urls)),
]