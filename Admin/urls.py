from django.urls import path
from .views import index, userDetail

app_name = 'Admin'

urlpatterns = [
    path('', index, name='index'),
    path('detail', userDetail, name='user_detail'),
]
