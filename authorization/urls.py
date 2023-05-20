from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='authorization/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
