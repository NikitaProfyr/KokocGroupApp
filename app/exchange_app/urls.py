from django.urls import path

from exchange_app.views import CurrencyExchangeRateDirectoryListApiView

app_name = "exchange_app"

urlpatterns = [path("show_rates", CurrencyExchangeRateDirectoryListApiView.as_view())]
