from django.urls import re_path
from django.contrib.auth import views as django_views

from . import views

urlpatterns = [
    re_path(r'^$', views.details, name='details'),

    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^logout/$', views.logout, name='logout'),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^password/reset/$', views.password_reset,
        name='reset-password'),
    re_path(r'^password/reset/done/$', django_views.PasswordResetDoneView.as_view(
        template_name='account/password_reset_done.html'),
        name='reset-password-done'),
    re_path(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',  # noqa
        views.password_reset_confirm, name='reset-password-confirm'),
    re_path(r'password/reset/complete/$', django_views.PasswordResetCompleteView.as_view(  # noqa
        template_name='account/password_reset_from_key_done.html'),
        name='reset-password-complete'),

    re_path(r'^address/(?P<pk>\d+)/edit/$', views.address_edit,
        name='address-edit'),
    re_path(r'^address/(?P<pk>\d+)/delete/$',
        views.address_delete, name='address-delete'),
]
