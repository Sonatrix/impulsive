from django.conf import settings
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.views import serve
from django.http import HttpResponse
from django.views.i18n import JavaScriptCatalog
from graphene_django.views import GraphQLView

from .account.urls import urlpatterns as account_urls
from .cart.urls import urlpatterns as cart_urls
from .checkout.urls import urlpatterns as checkout_urls
from .core.sitemaps import sitemaps
from .core.urls import urlpatterns as core_urls
from .dashboard.urls import urlpatterns as dashboard_urls
from .data_feeds.urls import urlpatterns as feed_urls
from .graphql.api import schema
from .order.urls import urlpatterns as order_urls
from .page.urls import urlpatterns as page_urls
from .product.urls import urlpatterns as product_urls
from .search.urls import urlpatterns as search_urls

handler404 = 'saleor.core.views.handle_404'

urlpatterns = [
    re_path(r'^', include(core_urls)),
    path('robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow:", content_type="text/plain"), name="robots_file"),
    re_path(r'^cart/', include((cart_urls, 'cart'), namespace='cart')),
    re_path(r'^checkout/',
        include((checkout_urls, 'checkout'), namespace='checkout')),
    re_path(r'^dashboard/',
        include((dashboard_urls, 'dashboard'), namespace='dashboard')),
    re_path(r'^graphql', GraphQLView.as_view(
        schema=schema, graphiql=settings.DEBUG), name='api'),
    re_path(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    re_path(r'^order/', include((order_urls, 'order'), namespace='order')),
    re_path(r'^page/', include((page_urls, 'page'), namespace='page')),
    re_path(r'^products/',
        include((product_urls, 'product'), namespace='product')),
    re_path(r'^account/',
        include((account_urls, 'account'), namespace='account')),
    re_path(r'^feeds/',
        include((feed_urls, 'data_feeds'), namespace='data_feeds')),
    re_path(r'^search/', include((search_urls, 'search'), namespace='search')),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'', include('payments.urls')),
    re_path('', include('social_django.urls', namespace='social'))]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve)] + static(
            settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)