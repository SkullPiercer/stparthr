from django.db.models import Q
from django.utils import timezone
from rest_framework import generics, status, viewsets

from .serializers import CitySerializer, ShopSerializer, StreetSerializer
from core.models import City, Shop, Street


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StreetSerializer

    def get_queryset(self):
        city_id = self.kwargs.get('city_id')
        return Street.objects.filter(city_id=city_id)


class ShopListCreateView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get_queryset(self):
        street_id = self.request.query_params.get('street')
        city_id = self.request.query_params.get('city')
        open_status = self.request.query_params.get('open')

        current_time = timezone.now().time()

        filters = Q()
        if street_id:
            filters &= Q(street_id=street_id)
        if city_id:
            filters &= Q(city_id=city_id)
        if open_status is not None:
            if open_status == '1':
                filters &= (
                    Q(opening_time__lte=current_time,
                      closing_time__gte=current_time)
                )
            else:
                filters &= (
                        Q(opening_time__gt=current_time)
                        | Q(closing_time__lt=current_time)
                )

        return Shop.objects.filter(filters)
