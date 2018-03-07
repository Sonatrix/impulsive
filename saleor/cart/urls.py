from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^update/(?P<variant_id>\d+)/$', views.update, name='update-line'),
    re_path(r'^summary/$', views.summary, name='cart-summary'),
    re_path(r'^shipingoptions/$', views.get_shipping_options,
        name='shipping-options')]
