from django.urls import path
from .views import RegisterUser, LoginUser, logout_user, home, detail_user, detail_response

urlpatterns = [
    path('', home, name='home'),
    path('sing_up/', RegisterUser.as_view(), name='sign_up'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', detail_user, name='detail_user'),
    path('response/<int:pk>/', detail_response, name='detail_response')
]