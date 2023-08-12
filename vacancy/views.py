from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import VacancyForm
from .models import Vacancy


def vacancy(request):
    model = Vacancy.objects.all()
    return render(request, 'vacancy/vacancy.html', {'model': model})


def create_vacancy(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacancy')
    else:
        form = VacancyForm()
    return render(request, 'vacancy/create_vacancy.html', {'form': form})


def detail(request, pk):
    model = Vacancy.objects.get(pk=pk)
    model.views += 1
    model.save()
    return render(request, 'vacancy/detail.html', {'model': model})
