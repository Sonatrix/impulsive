from django.urls import path
from .views import index, SignUp
from django.contrib.auth import views as auth_views

app_name = 'Loan'

urlpatterns = [
    path('', index, name='index'),
]

#login views
urlpatterns += [
    path('login/', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'index.html'}, name='logout'),
    path('signup/', SignUp.as_view(), name='signup')
]