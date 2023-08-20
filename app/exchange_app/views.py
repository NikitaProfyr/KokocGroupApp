from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import response
from rest_framework.generics import ListAPIView

from exchange_app.serializers import CurrencyExchangeRateDirectorySerializer
from exchange_app.servieces import get_data, get_dates
from exchange_app.models import CurrencyDirectory, CurrencyExchangeRateDirectory


# Create your views here.


class CurrencyExchangeRateDirectoryListApiView(ListAPIView):
    queryset = get_dates(CurrencyExchangeRateDirectory)
    serializer_class = CurrencyExchangeRateDirectorySerializer
    filterset_fields = [
        "Date",
    ]
