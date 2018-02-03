from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})


def handler404(request):
    return render(request, 'Loan/404.html',{})


def handler500(request):
    return render(request,'Loan/500.html', {})

