from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from members.forms import SignUpForm
from django.urls import reverse_lazy
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signupform.html'
    success_url = reverse_lazy('login')