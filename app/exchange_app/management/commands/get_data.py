from django.core.management import BaseCommand

from exchange_app.models import CurrencyExchangeRateDirectory
from exchange_app.serializers import CurrencyDirectorySerializer
import requests


class Command(BaseCommand):
    """Команда для получения данных из внешнего ресурса"""

    help = "получение данных с внешнего сервиса"

    url = "https://www.cbr-xml-daily.ru/daily_json.js"

    data = requests.get(url=url).json()["Valute"]

    def handle(self, *args, **options):
        for key, value in self.data.items():
            serializer = CurrencyDirectorySerializer(data=value)
            if serializer.is_valid():
                сurrency = serializer.save()
                exchange_rate = CurrencyExchangeRateDirectory.objects.create(
                    Currency=сurrency
                )
                exchange_rate.save()
                self.stdout.write("данные успешно внесены в базу")
            else:
                self.stdout.write("ошибка валидации")
