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
    city_name = serializers.CharField(source='city.name', read_only=True)
    street_name = serializers.CharField(source='street.name', read_only=True)
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(), write_only=True
    )
    street_id = serializers.PrimaryKeyRelatedField(
        queryset=Street.objects.all(), write_only=True
    )

    class Meta:
        model = Shop
        fields = ['name', 'city_id', 'city_name', 'street_id', 'street_name',
                  'house_number', 'opening_time', 'closing_time']

    def validate(self, data):
        shop_name = data.get('name')
        if Shop.objects.filter(name=shop_name).exists():
            raise serializers.ValidationError('This shop name is already in use!')
        return data

    def create(self, validated_data):
        city = validated_data.pop('city_id')
        street = validated_data.pop('street_id')
        shop = Shop.objects.create(city=city, street=street, **validated_data)
        return shop