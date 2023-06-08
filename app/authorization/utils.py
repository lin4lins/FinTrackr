from authorization.models import User
from core.models import Category

EXPENSE_CATEGORIES = [
    "Продукти харчування",
    "Комунальні платежі",
    "Побутові товари",
    "Громадський транспорт",
    "Паливо",
    "Розваги",
    "Одяг та взуття",
    "Кафе та ресторани",
    "Краса та здоров'я",
    "Освіта",
]
INCOME_CATEGORIES = ["Зарплата", "Пенсія", "Стипендія", "Відсотки від депозитів", "Подарунки"]


def create_user_default_categories(user: User):
    for category_name in EXPENSE_CATEGORIES:
        Category.objects.create(user=user, name=category_name, type="e")

    for category_name in INCOME_CATEGORIES:
        Category.objects.create(user=user, name=category_name, type="i")
