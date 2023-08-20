from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from exchange_app.models import CurrencyDirectory, CurrencyExchangeRateDirectory
from exchange_app.servieces import get_data


class CurrencyDirectorySerializer(ModelSerializer):

    def create(self, validated_data):
        return CurrencyDirectory.objects.create(**validated_data)

    class Meta:
        model = CurrencyDirectory
        fields = ['CharCode', 'Name', 'Value']
        many = True


class CurrencyExchangeRateDirectorySerializer(ModelSerializer):
    Currency = CurrencyDirectorySerializer()

    class Meta:
        model = CurrencyExchangeRateDirectory
        fields = ['Date', 'Currency']
