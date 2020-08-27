from django.urls import path
from django.contrib.auth import views as auth_views

from my_account import views

urlpatterns = [
    # path('', views.HomeView.as_view(), name='home'),
    path('', views.home, name='home'),
]