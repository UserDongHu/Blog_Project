from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CreateUserForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

signup = CreateView.as_view(
    form_class = CreateUserForm,
    template_name = 'accounts/form.html',
    success_url = reverse_lazy('accounts:login')
)

login = LoginView.as_view(
    template_name = 'accounts/form.html',
)

class MyLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('accounts:login')
    
logout = MyLogoutView.as_view()

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

profile = ProfileView.as_view()