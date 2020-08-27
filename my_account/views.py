from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView, DetailView
from django.views import View
from datetime import timedelta
from django.utils import timezone
from django.core.paginator import Paginator

from my_account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm, CheckPasswordForm
from my_account.models import Account


def home(request):

    return render(request, 'account/home.html')


class HomeView(ListView):
    template_name = 'account/home.html'
    model = Account

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
