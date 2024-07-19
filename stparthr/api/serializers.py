from rest_framework import serializers

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
    city = serializers.CharField(source='city.name', read_only=True)
    street = serializers.CharField(source='street.name', read_only=True)
    city_name = serializers.CharField(write_only=True)
    street_name = serializers.CharField(write_only=True)

    class Meta:
        model = Shop
        fields = [
            'name', 'city', 'street', 'house_number', 'opening_time',
            'closing_time', 'city_name', 'street_name'
        ]

    def validate(self, data):
        shop_name = data.get('name')
        city = data.get('city_name')
        street = data.get('street_name')

        if not Street.objects.filter(name=street).exists():
            raise serializers.ValidationError(
                'Street does`t exists'
            )

        if not City.objects.filter(name=city).exists():
            raise serializers.ValidationError(
                'City does`t exists'
            )

        if Shop.objects.filter(name=shop_name).exists():
            raise serializers.ValidationError(
                'This shop name is already in use!'
            )
        return data

    def create(self, validated_data):
        city_name = validated_data.pop('city_name')
        street_name = validated_data.pop('street_name')

        city, created = City.objects.get_or_create(name=city_name)
        street, created = Street.objects.get_or_create(name=street_name,
                                                       city=city)

        shop = Shop.objects.create(city=city, street=street, **validated_data)
        return shop
