from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "type"]

        labels = {
            "name": "Ім'я",
            "type": "Тип",
        }

        widgets = {
            "type": forms.RadioSelect(
                choices=Category.TYPE,
            ),
        }
