import random
from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils import timezone

from authorization.models import User
from core.models import Currency, Category, Account, Transaction


class Command(BaseCommand):
    help = "Deletes all data from the tables and fills the database with test data."

    __user = None
    __currencies = None
    __categories = None
    __accounts = None
    __transactions = None

    def handle(self, *args, **options):
        User.objects.all().delete()
        Currency.objects.all().delete()
        Category.objects.all().delete()
        Account.objects.all().delete()
        Transaction.objects.all().delete()

        self.stdout.write(
            self.style.SUCCESS(
                "The following tables have been cleaned:\n"
                "User, Currency, Category, Account, Transaction."
            )
        )

        self.__create_user()
        self.__create_currencies()
        self.__create_categories()
        self.__create_accounts()
        self.__create_transactions()

        self.stdout.write(self.style.SUCCESS("\nDatabase has been filled"))

    def __create_user(self):
        email = "test@test.com"
        password = "test_password"
        self.__user = User(email=email)
        self.__user.set_password(password)
        self.__user.save()

        self.stdout.write(self.style.SUCCESS(f"User({email=}; {password=}) have been created"))

    def __create_currencies(self):
        self.__currencies = [
            Currency(symbol="₴", code="UAH", name="Гривня"),
            Currency(symbol="$", code="USD", name="Долар США"),
            Currency(symbol="€", code="EUR", name="Євро"),
        ]

        [currency.save() for currency in self.__currencies]
        self.stdout.write(self.style.SUCCESS("currencies have been added"))

    def __create_categories(self):
        self.__categories = [
            Category(name="Заробітня плата", type="i", user=self.__user),
            Category(name="Фріланс", type="i", user=self.__user),
            Category(name="Стипендія", type="i", user=self.__user),
            Category(name="Соціальні виплати", type="i", user=self.__user),
            Category(name="Продукти харчування", type="e", user=self.__user),
            Category(name="Ресторани та кафе", type="e", user=self.__user),
            Category(name="Дім", type="e", user=self.__user),
            Category(name="Транспорт", type="e", user=self.__user),
            Category(name="Здоров'я", type="e", user=self.__user),
            Category(name="Підписки", type="e", user=self.__user),
            Category(name="Покупки", type="e", user=self.__user),
            Category(name="Дозвілля", type="e", user=self.__user),
            Category(name="Домашні тварини", type="e", user=self.__user),
            Category(name="Інші витрати", type="e", user=self.__user),
        ]

        [category.save() for category in self.__categories]
        self.stdout.write(self.style.SUCCESS("categories have been added"))

    def __create_accounts(self):
        uah_currency = self.__currencies[0]
        usd_currency = self.__currencies[1]
        self.__accounts = [
            Account(name="Готівка", balance=0.0, currency=uah_currency, user=self.__user),
            Account(name="Картка", balance=0.0, currency=uah_currency, user=self.__user),
            Account(name="Збереження", balance=0.0, currency=usd_currency, user=self.__user),
        ]

        [account.save() for account in self.__accounts]

        self.stdout.write(self.style.SUCCESS("accounts have been added"))

    def __create_transactions(self):
        cash_account = self.__accounts[0]
        card_account = self.__accounts[1]
        savings_account = self.__accounts[2]

        food_category = self.__categories[4]
        home_category = self.__categories[6]
        transport_category = self.__categories[7]
        shopping_category = self.__categories[10]

        income_category = self.__categories[0]
        freelance_category = self.__categories[1]

        self.__transactions = (
            self.__generate_transactions(category=food_category, account=cash_account, limit=50)
            + self.__generate_transactions(category=food_category, account=card_account, limit=20)
            + self.__generate_transactions(category=home_category, account=cash_account, limit=10)
            + self.__generate_transactions(category=home_category, account=card_account, limit=10)
            + self.__generate_transactions(
                category=transport_category, account=cash_account, limit=60
            )
            + self.__generate_transactions(
                category=transport_category, account=card_account, limit=10
            )
            + self.__generate_transactions(
                category=shopping_category, account=cash_account, limit=5
            )
            + self.__generate_transactions(
                category=shopping_category, account=card_account, limit=15
            )
            + self.__generate_transactions(
                category=income_category, account=cash_account, limit=2, income=True
            )
            + self.__generate_transactions(
                category=income_category, account=card_account, limit=5, income=True
            )
            + self.__generate_transactions(
                category=income_category, account=savings_account, limit=2, income=True
            )
            + self.__generate_transactions(
                category=freelance_category, account=cash_account, limit=2, income=True
            )
            + self.__generate_transactions(
                category=freelance_category, account=card_account, limit=5, income=True
            )
            + self.__generate_transactions(
                category=freelance_category, account=savings_account, limit=2, income=True
            )
        )

        [transactions.save() for transactions in self.__transactions]
        self.__update_transactions_datetime()

        self.stdout.write(self.style.SUCCESS("transactions have been added"))

    def __update_transactions_datetime(self):
        for transaction in self.__transactions:
            transaction.created_at = self.__get_random_datetime()
            transaction.save()

    def __generate_transactions(self, category, account, limit, income=False):
        amount_getter = (
            self.__get_random_income_amount if income else self.__get_random_expense_amount
        )
        transactions = []
        for i in range(1, limit + 1):
            transaction = Transaction(amount=amount_getter(), category=category, account=account)
            transactions.append(transaction)
        return transactions

    def __get_random_expense_amount(self):
        return round(random.uniform(1.00, 5000.00), 2)

    def __get_random_income_amount(self):
        return round(random.uniform(50_000.00, 150_000.00), 2)

    def __get_random_datetime(self):
        now_datetime = datetime.now()
        random_day = random.randint(1, datetime.now().day)
        random_hour = random.randint(0, 23)
        random_minutes = random.randint(0, 59)
        random_seconds = random.randint(0, 59)
        return datetime(
            now_datetime.year,
            now_datetime.month,
            random_day,
            random_hour,
            random_minutes,
            random_seconds,
            tzinfo=timezone.get_current_timezone(),
        )
