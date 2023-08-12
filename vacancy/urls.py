from django.urls import path
from .views import vacancy, create_vacancy, detail

urlpatterns = [
    path('', vacancy, name='vacancy'),
    path('create/', create_vacancy, name='create_vacancy'),
    path('<int:pk>/', detail, name='detail_vacancy'),
]