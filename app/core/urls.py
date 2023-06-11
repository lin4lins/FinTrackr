from core.views.account import (
    AccountListView,
    FirstAccountView,
    AccountCreateView,
    AccountDetailView,
)
from core.views.category import CategoryDetailView, CategoryView
from core.views.home import HomeView
from django.urls import path

from core.views.transaction import TransactionCreateView, TransactionListView

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("category/", CategoryView.as_view(), name="category"),
    path("account/first/", FirstAccountView.as_view(), name="account-create-first"),
    path("account/create/", AccountCreateView.as_view(), name="account-create"),
    path("account/<int:account_id>/", AccountDetailView.as_view(), name="account-detail"),
    path("account/", AccountListView.as_view(), name="account"),
    path("category/<int:category_id>/", CategoryDetailView.as_view(), name="category-detail"),
    path("transaction/create/", TransactionCreateView.as_view(), name="transaction-create"),
    path("transaction/", TransactionListView.as_view(), name="transaction"),
]
