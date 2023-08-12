from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm, LoginUserForm


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'client/sign_up.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'client/login.html'

    def get_success_url(self):
        return '/'


def logout_user(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'client/home_page.html', {'link': 'home page'})


def detail_user(request):
    return render(request, 'client/detail_user.html')

