from django.urls import path

from core.views.home import HomeView

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
]
