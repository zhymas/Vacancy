from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import VacancyForm
from .models import Vacancy
from client.models import UserProfile


def vacancy(request):
    model = Vacancy.objects.order_by('-id')
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        return render(request, 'vacancy/vacancy.html', {'model': model, 'user_profile': user_profile})
    else:
        return render(request, 'vacancy/vacancy.html', {'model': model})


def create_vacancy(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'You are not logged in'})

    user_profile = get_object_or_404(UserProfile, user=request.user)
    if user_profile.user_type != 'recruiter':
        return JsonResponse({'error': 'You are not a recruiter'})

    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.author = request.user
            form.save()

    else:
        form = VacancyForm()

    return render(request, 'vacancy/create_vacancy.html', {'form': form})


def detail(request, pk):
    model = Vacancy.objects.get(pk=pk)
    model.views += 1
    model.save()
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        return render(request, 'vacancy/detail.html', {'model': model, 'user_profile': user_profile})
    else:
        return render(request, 'vacancy/detail.html', {'model': model})
