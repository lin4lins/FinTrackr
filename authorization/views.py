from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View

from authorization.forms import SignUpForm


# Create your views here.


class SignUpView(View):
    form_class = SignUpForm
    template_name = 'authorization/signup.html'
    success_url_name = 'home'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url_name)

        return render(request, self.template_name, {'form': form})
