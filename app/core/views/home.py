import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from core.helpers.home.money_structure import (
    CashFlowData,
    CategoryStructureGenerator,
    MonthlyBalance,
)
from core.models import Account, Transaction


class HomeView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")
    template_name = "core/home.html"
    redirect_url = reverse_lazy("home")

    def get(self, request):
        selected_account = None
        user_accounts = Account.objects.filter(user=request.user)
        if user_accounts:
            selected_account = user_accounts[0]

        account_id = request.GET.get("account-id")
        if account_id:
            selected_account = Account.objects.get(user=request.user, id=account_id)

        user_categories = request.user.categories.all()
        if selected_account:
            structure_generator = CategoryStructureGenerator(
                categories=user_categories, account=selected_account
            )
            expense_structure_data = json.dumps(structure_generator.expense_structure_data)
            income_structure_data = json.dumps(structure_generator.income_structure_data)

            last_transactions = Transaction.objects.filter(account=selected_account).order_by(
                "-created_at"
            )[:4]

            cash_flow_data = json.dumps(CashFlowData(account=selected_account).data)
            balance_dynamics = json.dumps(MonthlyBalance(account=selected_account).data)
        else:
            expense_structure_data = ""
            income_structure_data = ""
            cash_flow_data = ""
            balance_dynamics = ""
            last_transactions = []

        template_data = {
            "active_page": "home",
            "accounts": user_accounts,
            "cash_flow_data": cash_flow_data,
            "balance_dynamics_data": balance_dynamics,
            "expense_structure_data": expense_structure_data,
            "income_structure_data": income_structure_data,
            "last_transactions": last_transactions,
        }

        return render(request, self.template_name, template_data)
