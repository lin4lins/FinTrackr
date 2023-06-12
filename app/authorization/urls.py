from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import CustomLoginView, SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", CustomLoginView.as_view(template_name="authorization/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
