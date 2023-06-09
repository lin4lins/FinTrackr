from django.core.management import BaseCommand

from core.models import Currency

DEFAULT_CURRENCIES = [
    {"name": "долар США", "code": "USD", "symbol": "$"},
    {"name": "євро", "code": "EUR", "symbol": "€"},
    {"name": "гривня", "code": "UAH", "symbol": "₴"},
]


class Command(BaseCommand):
    help = "Populates database with currencies"

    def handle(self, *args, **options):
        for currency in DEFAULT_CURRENCIES:
            Currency.objects.create(
                symbol=currency.get("symbol"), code=currency.get("code"), name=currency.get("name")
            )

        self.stdout.write("Currencies created successfully")
