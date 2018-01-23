from django.urls import include, re_path
from django.views import generic
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import EchoView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    re_path(r'^$', generic.RedirectView.as_view(url='/api/', permanent=False)),
    re_path(r'^api/$', get_schema_view()),
    re_path(r'^api/auth/', include('rest_framework.urls'), name='rest_framework'),
    re_path(r'^api/auth/token/obtain/$', TokenObtainPairView.as_view()),
    re_path(r'^api/auth/token/refresh/$', TokenRefreshView.as_view()),
    re_path(r'^api/echo/$', EchoView.as_view())
]
