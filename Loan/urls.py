from django.urls import path
from .views.default import index, SignUp, about
from .views.products import loan, insurance, cards, products
from django.contrib.auth import views as auth_views

app_name = 'Loan'

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
]

#products views
urlpatterns += [
	path('products', products, name='products'),
    path('products/loan', loan, name='loan'),
    path('products/insurance', insurance, name='insurance'),
    path('products/cards', cards, name='cards'),
]
#login views
urlpatterns += [
    path('login/', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'index.html'}, name='logout'),
    path('signup/', SignUp.as_view(), name='signup')
]