from django.shortcuts import render
from django.http import HttpResponse

def index(request) :
	return render(request, 'home.html', {})

def userDetail(request):
	return render(request, 'user/user_details.html', {})