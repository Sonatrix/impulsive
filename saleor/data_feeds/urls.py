from django.urls import re_path
from django.views.generic.base import RedirectView

from .google_merchant import get_feed_file_url

urlpatterns = [
    re_path(r'google/$',
        RedirectView.as_view(
            get_redirect_url=get_feed_file_url, permanent=True),
        name='google-feed')]
