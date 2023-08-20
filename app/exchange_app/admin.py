from django.contrib import admin
from django.contrib.admin import ModelAdmin

from exchange_app.models import CurrencyDirectory, CurrencyExchangeRateDirectory

# Register your models here.


@admin.register(CurrencyDirectory)
class CurrencyDirectoryModelAdmin(ModelAdmin):
    model = CurrencyDirectory


@admin.register(CurrencyExchangeRateDirectory)
class CurrencyExchangeRateDirectoryModelAdmin(ModelAdmin):
    model = CurrencyExchangeRateDirectory
