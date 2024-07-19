from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CityViewSet, StreetViewSet, ShopListCreateView

router = DefaultRouter()
router.register(r'city', CityViewSet, basename='city')
router.register(r'city/(?P<city_id>\d+)/street', StreetViewSet,
                basename='city-street')

urlpatterns = [
    path('', include(router.urls)),
    path('shop/', ShopListCreateView.as_view(), name='shop-list-create'),
]
