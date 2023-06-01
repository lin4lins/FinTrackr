from django.urls import path

from core.views.home import HomeView
from core.views.category import CategoryCreateView

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("category/", CategoryCreateView.as_view(), name="category"),
]
