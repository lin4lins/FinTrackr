from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View

from core.forms import TransactionForm
from core.models import Category, Transaction


class TransactionCreateView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")
    template_name = "core/transaction-create.html"
    success_url = reverse_lazy("transaction")
    fail_url = reverse_lazy("transaction-create")

    def get(self, request):
        user = request.user
        form = TransactionForm()
        income_categories = Category.objects.filter(user=user, type="i")
        expense_categories = Category.objects.filter(user=user, type="e")
        return render(
            request,
            self.template_name,
            {
                "income_categories": income_categories,
                "expense_categories": expense_categories,
                "accounts": user.accounts,
                "form": form,
            },
        )

    def post(self, request):
        corrected_post_data = self.__set_selected_category_id(request.POST)
        form = TransactionForm(corrected_post_data)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)

        return redirect(self.fail_url)

    @staticmethod
    def __set_selected_category_id(post_data):
        updated_post_data = post_data.copy()
        category_values = post_data.getlist("category")
        updated_category_values = [
            value for value in category_values if isinstance(value, str) and value.isnumeric()
        ]
        updated_post_data.setlist("category", updated_category_values)
        return updated_post_data


class TransactionListView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")
    template_name = "core/transaction.html"
    success_url = reverse_lazy("transaction")

    def get(self, request):
        user = request.user
        transactions = Transaction.objects.filter(account__in=user.accounts.all()).order_by(
            "-created_at"
        )
        return render(
            request,
            self.template_name,
            {
                "transactions": transactions,
            },
        )


class TransactionDetailView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")

    def delete(self, request, transaction_id):
        category = get_object_or_404(Transaction, id=transaction_id, account__user=request.user)
        category.delete()
        return HttpResponse(status=204)
