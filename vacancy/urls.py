from django.urls import path
from .views import vacancy, create_vacancy, detail, filter

urlpatterns = [
    path('', vacancy, name='vacancy'),
    path('create/', create_vacancy, name='create_vacancy'),
    path('<int:pk>/', detail, name='detail_vacancy'),
    path('filters/', filter, name='filters')
]