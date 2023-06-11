from datetime import datetime

from django.db.models import Sum
from django.utils import timezone

from core.models import Transaction, Category


class CategoryStructureGenerator:
    def __init__(self, categories, account):
        self.__categories = categories
        self.__account = account

        self.__current_timezone = timezone.get_current_timezone()
        self.__datetime_now = datetime.now(tz=self.__current_timezone)
        self.__datetime_start_current_month = datetime(
            self.__datetime_now.year, self.__datetime_now.month, 1, tzinfo=self.__current_timezone
        )

        self.expense_structure_data = [["Категорія", "Сума"]]
        self.income_structure_data = [["Категорія", "Сума"]]

        self.__process_categories()

    def __process_categories(self):
        for category in self.__categories:
            self.__process_category(category)

    def __compute_transactions_sum(self, category):
        transaction_sum = Transaction.objects.filter(
            category=category,
            account=self.__account,
            created_at__range=(self.__datetime_start_current_month, self.__datetime_now),
        ).aggregate(total_amount=Sum("amount"))

        total_amount = transaction_sum["total_amount"] or 0
        total_amount = round(total_amount, 2)

        return total_amount

    def __process_category(self, category):
        total_amount = self.__compute_transactions_sum(category)

        if category.type == Category.EXPENSE:
            self.expense_structure_data.append([category.name, total_amount])
        if category.type == Category.INCOME:
            self.income_structure_data.append([category.name, total_amount])


class CashFlowData:
    def __init__(self, account):
        self.__account = account

        income_color = "#28CB7C"
        expense_color = "#E74C3C"
        headers = ["Type", "Value", {"role": "style"}]

        self.data = [
            headers,
            ["Дохід", self.__get_total_amount(expense=False), income_color],
            ["Витрати", self.__get_total_amount(expense=True), expense_color],
        ]

    def __get_total_amount(self, expense=False):
        category_type = Category.EXPENSE if expense else Category.INCOME
        expenses = Transaction.objects.filter(
            account=self.__account, category__type=category_type
        ).aggregate(total_amount=Sum("amount"))

        total_amount = expenses["total_amount"] or 0
        total_expenses = round(total_amount, 2)

        return total_expenses
