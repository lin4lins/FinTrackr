from django import forms
from django.core.validators import MinValueValidator

from .models import Category, Account, Currency, Transaction


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "type"]

        labels = {
            "name": "Ім'я",
        }


class AccountForm(forms.ModelForm):
    currency = forms.ModelChoiceField(
        queryset=Currency.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Валюта",
        to_field_name="code",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["currency"].label_from_instance = lambda obj: obj.code

    class Meta:
        model = Account
        fields = ["name", "balance", "currency"]
        labels = {"name": "Назва", "balance": "Баланс", "currency": "Валюта"}


class TransactionForm(forms.ModelForm):
    amount = forms.FloatField(label="Сума", validators=[MinValueValidator(0)])

    account = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Рахунок",
        to_field_name="id",
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Категорія",
        to_field_name="id",
    )

    note = forms.CharField(
        label="Коментар",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["account"].label_from_instance = lambda obj: obj.name
        self.fields["category"].label_from_instance = lambda obj: obj.name

    class Meta:
        model = Transaction
        fields = ["amount", "account", "category", "note"]
