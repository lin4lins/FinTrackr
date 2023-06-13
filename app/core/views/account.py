from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View

from authorization.models import User
from core.forms import AccountForm
from core.models import Account


class FirstAccountView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")
    template_name = "core/account-create-first.html"
    success_url = reverse_lazy("account")

    def get(self, request):
        if self.__has_user_accounts(request.user):
            return redirect(self.success_url)

        form = AccountForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            return redirect(self.success_url)

        return render(request, self.template_name, {"form": form})

    @staticmethod
    def __has_user_accounts(user: User):
        accounts = Account.objects.filter(user=user)
        return len(accounts) != 0


class AccountListView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")
    template_name = "core/account.html"
    success_url = reverse_lazy("account")

    def get(self, request):
        form = AccountForm()
        user_accounts = Account.objects.filter(user=request.user).all()
        return render(request, self.template_name, {"accounts": user_accounts, "form": form})


class AccountCreateView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")
    template_name = "core/account-create.html"
    success_url = reverse_lazy("account")

    def get(self, request):
        form = AccountForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            return redirect(self.success_url)

        return render(request, self.template_name, {"form": form})


class AccountDetailView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("category")

    def delete(self, request, account_id: int):
        category = get_object_or_404(Account, id=account_id, user=request.user)
        category.delete()
        return HttpResponse(status=204)
