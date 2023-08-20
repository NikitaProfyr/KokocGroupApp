from django.db import models


class CurrencyDirectory(models.Model):
    """Модель справочника валют"""
    CharCode = models.CharField(max_length=5, verbose_name="Символьное обозначение")
    Name = models.CharField(max_length=90, verbose_name="Наименование")
    Value = models.DecimalField(decimal_places=4, max_digits=9, default=0, verbose_name="Значение")

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = "Валюты"


class CurrencyExchangeRateDirectory(models.Model):
    """Модель справочника курса валют"""
    Currency = models.ForeignKey(CurrencyDirectory, on_delete=models.CASCADE)
    Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.Date} {self.Currency.Name}'

    class Meta:
        verbose_name = 'Справочник курсы валют'
        verbose_name_plural = "Справочники курсов валют"
        unique_together = ['Date', 'Currency']

