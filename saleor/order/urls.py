from django.urls import re_path

from . import views
from ..core import TOKEN_PATTERN

urlpatterns = [
    re_path(r'^%s/$' % (TOKEN_PATTERN,), views.details, name='details'),
    re_path(r'^%s/payment/$' % (TOKEN_PATTERN,),
        views.payment, name='payment'),
    re_path(r'^%s/payment/(?P<variant>[-\w]+)/$' % (TOKEN_PATTERN,),
        views.start_payment, name='payment'),
    re_path(r'^%s/cancel-payment/$' % (TOKEN_PATTERN,), views.cancel_payment,
        name='cancel-payment'),
    re_path(r'^%s/checkout-success/$' % (TOKEN_PATTERN,),
        views.checkout_success, name='checkout-success'),
    re_path(r'^%s/attach/$' % (TOKEN_PATTERN,),
        views.connect_order_with_user, name='connect-order-with-user'),
]
