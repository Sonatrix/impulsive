from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from Loan.forms import CreateUserForm

def index(request):
    return render(request, 'comingsoon.html', {})

def about(request):
    return render(request, 'about.html', {})


def handler404(request):
    return render(request, 'Loan/404.html',{})


def handler500(request):
    return render(request,'Loan/500.html', {})

class SignUp(generic.CreateView):
    form_class = CreateUserForm
    success_url = '/login'
    template_name = 'registration/signup.html'

