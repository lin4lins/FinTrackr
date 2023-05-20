from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)
