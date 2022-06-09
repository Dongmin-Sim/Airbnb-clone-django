from tkinter.tix import Form
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from . import forms

# Create your views here.
class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = forms.LoginForm
    success_url = reverse_lazy('core:home')
    initial = {
        'email': 'codongmin@gmail.com'
    }

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)
            
        return super().form_valid(form)

    
def logout_view(request):
    logout(request)
    return redirect(reverse('core:home'))


class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = forms.SignUpForm
    success_url = reverse_lazy('core:home')
    initial = {
        'first_name':'sim',
        'last_name': 'dongmin',
        'email': 'codongmin@gmail.com'
    }

    def form_valid(self, form):
        form.save()
        
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
