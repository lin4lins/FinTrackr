from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View


class HomeView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")
    template_name = "core/home.html"
    redirect_url = reverse_lazy("feed")

    def get(self, request):
        return render(request, self.template_name, {"message": "Home page"})
