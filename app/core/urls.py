from core.views.category import CategoryDetailView, CategoryView
from core.views.home import HomeView
from django.urls import path

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("category/", CategoryView.as_view(), name="category"),
    path('category/<int:category_id>/', CategoryDetailView.as_view(), name='category-detail'),
]
