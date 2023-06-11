import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from core.helpers.home.money_structure import CategoryStructureGenerator
from core.models import Account, Transaction


class HomeView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")
    template_name = "core/home.html"
    redirect_url = reverse_lazy("home")

    def get(self, request):
        user_accounts = Account.objects.filter(user=request.user)
        selected_account = user_accounts[0]

        user_categories = request.user.categories.all()
        structure_generator = CategoryStructureGenerator(
            categories=user_categories, account=selected_account
        )

        last_transactions = Transaction.objects.filter(account=selected_account).order_by(
            "-created_at"
        )[:4]

        template_data = {
            "active_page": "home",
            "accounts": user_accounts,
            "expense_structure_data": json.dumps(structure_generator.expense_structure_data),
            "income_structure_data": json.dumps(structure_generator.income_structure_data),
            "last_transactions": last_transactions,
        }

        return render(request, self.template_name, template_data)
