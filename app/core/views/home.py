from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from core.models import Account


class HomeView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")
    template_name = "core/home.html"
    redirect_url = reverse_lazy("home")

    def get(self, request):
        user_accounts = Account.objects.filter(user=request.user)
        return render(
            request, self.template_name, {"active_page": "home", "accounts": user_accounts}
        )
