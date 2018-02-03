from django.urls import path
from .views import index

app_name = 'Loan'

urlpatterns = [
    path('', index, name='index'),
]