from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm, LoginUserForm
from .models import UserProfile


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'client/sign_up.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user_type = form.cleaned_data.get('user_type')
        user = form.save()
        user.userprofile.user_type = user_type
        user.save()
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
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        return render(request, 'client/home_page.html', {'user_profile': user_profile})
    else:
        return render(request, 'client/home_page.html')


def detail_user(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        return render(request, 'client/detail_user.html', {'user_profile': user_profile})
    else:
        return render(request, 'client/detail_user.html')

