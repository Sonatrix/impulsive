from django.urls import path
from .views import index

app_name = 'Admin'

urlpatterns = [
    path('', index, name='index'),
]
