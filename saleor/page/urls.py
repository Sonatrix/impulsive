from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^(?P<slug>[a-z0-9-_]+?)/$',
        views.page_detail, name='details')]
