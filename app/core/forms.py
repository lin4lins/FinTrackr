from django import forms
from .models import Category, Account, Currency


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
