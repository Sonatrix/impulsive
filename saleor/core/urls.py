from django.urls import re_path
from impersonate.views import stop_impersonate

from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^style-guide/', views.styleguide, name='styleguide'),
    re_path(r'^impersonate/(?P<uid>\d+)/', views.impersonate,
        name='impersonate-start'),
    re_path(r'^impersonate/stop/$', stop_impersonate,
        name='impersonate-stop'),
    re_path(r'^404', views.handle_404, name='handle-404'),
    re_path(r'^manifest\.json$', views.manifest, name='manifest'),
]
