from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index_view, name='index'),
    re_path(r'^shipping-address/', views.shipping_address_view,
        name='shipping-address'),
    re_path(r'^shipping-method/', views.shipping_method_view,
        name='shipping-method'),
    re_path(r'^summary/', views.summary_view, name='summary'),
    re_path(r'^remove_voucher/', views.discount.remove_voucher_view,
        name='remove-voucher'),
    re_path(r'^login/', views.login, name='login')]
