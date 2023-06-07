from django import forms
from .models import Category


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "type"]

        labels = {
            "name": "Ім'я",
        }


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

        labels = {
            "name": "Ім'я",
        }
