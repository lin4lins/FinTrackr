from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].label = "Електронна пошта"
        self.fields["password1"].label = "Пароль"
        self.fields["password2"].label = "Повторіть пароль"

    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Електронна пошта"
        self.fields["password"].label = "Пароль"
