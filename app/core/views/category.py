from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from core.forms import CategoryForm


class CategoryCreateView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")
    template_name = "core/category-create.html"
    success_url = reverse_lazy("category")

    def get(self, request):
        form = CategoryForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            try:
                category.save()
                return redirect(self.success_url)

            except IntegrityError as exc:
                form.add_error("name", exc)

        return render(request, self.template_name, {"form": form})
