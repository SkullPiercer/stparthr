from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ['name', 'city']


class ShopSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(write_only=True)
    street_name = serializers.CharField(write_only=True)
    city = serializers.PrimaryKeyRelatedField(read_only=True)
    street = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Shop
        fields = ['name', 'city', 'city_name', 'street', 'street_name',
                  'house_number', 'opening_time', 'closing_time']

    def validate(self, data):
        shop_name = data.get('name')
        if Shop.objects.filter(name=shop_name).exists():
            raise ValidationError('This shopname already in use!')
        return data

    def create(self, validated_data):
        city_name = validated_data.pop('city_name')
        street_name = validated_data.pop('street_name')
        city, created = City.objects.get_or_create(name=city_name)
        street, created = Street.objects.get_or_create(
            name=street_name, city=city
        )
        shop = Shop.objects.create(city=city, street=street, **validated_data)
        return shop
