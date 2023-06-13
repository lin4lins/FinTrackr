from django import template

from core.models import Category, Transaction

register = template.Library()


@register.filter
def transaction_color(transaction: Transaction):
    if transaction.category.type == Category.EXPENSE:
        return "expense-transaction-color"
    else:
        return "income-transaction-color"
