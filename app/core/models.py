from django.db import models, transaction
from colorfield.fields import ColorField

from authorization.models import User


class Currency(models.Model):
    symbol = models.CharField(max_length=1)
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"currency:name={self.name};symbol={self.symbol};code={self.code}"


class Category(models.Model):
    name = models.CharField(max_length=25)
    INCOME = "i"
    EXPENSE = "e"
    TYPE = (
        (INCOME, "Дохід"),
        (EXPENSE, "Витрата"),
    )
    type = models.CharField(max_length=1, choices=TYPE, default=EXPENSE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")

    class Meta:
        unique_together = (
            "name",
            "user",
        )

    def __str__(self):
        return f"category:name={self.name};type={self.type};user={self.user}"


class Account(models.Model):
    name = models.CharField(max_length=50)
    balance = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="accounts")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")
    color = ColorField(default="#FF0000")

    def __str__(self):
        return (
            f"account:name={self.name};balance={self.balance};currency={self.currency};"
            f"user={self.user}"
        )


class Transaction(models.Model):
    amount = models.FloatField()
    note = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="transactions")
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transactions")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"transaction:amount={self.amount};category={self.category};account={self.account};"
            f"note={self.note};created_at={self.created_at}"
        )

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self.category.type == Category.EXPENSE:
                self.amount *= -1
            super().save(*args, **kwargs)

            self.account.balance += self.amount
            self.account.save()

    def delete(self, *args, **kwargs):
        with transaction.atomic():
            self.account.balance -= self.amount
            self.account.save()
            super().delete(*args, **kwargs)
