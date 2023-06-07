from core.forms import CategoryCreateForm, CategoryUpdateForm
from core.models import Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View


class CategoryListView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")
    template_name = "core/category.html"
    success_url = reverse_lazy("category")

    def get(self, request):
        user = request.user
        user_categories = Category.objects.filter(user=user).all()
        form = CategoryForm()
        return render(request, self.template_name, {"categories": user_categories, "form": form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            try:
                category.save()
                return redirect(self.success_url)

            except IntegrityError:
                form.add_error("name", "Така категорія вже існує")

        user_categories = Category.objects.filter(user=request.user).all()
        return render(request, self.template_name, {"categories": user_categories, "form": form})


class CategoryDetailView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("category")

    def post(self):
        pass

    def delete(self, request, category_id):
        category = get_object_or_404(Category, id=category_id, user=request.user)
        category.delete()
        return HttpResponse(status=204)
