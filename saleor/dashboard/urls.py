from django.conf import settings
from django.urls import include, re_path
from graphene_django.views import GraphQLView

from . import views as core_views
from .category.urls import urlpatterns as category_urls
from .collection.urls import urlpatterns as collection_urls
from .customer.urls import urlpatterns as customer_urls
from .discount.urls import urlpatterns as discount_urls
from .graphql.api import schema
from .group.urls import urlpatterns as groups_urls
from .order.urls import urlpatterns as order_urls
from .page.urls import urlpatterns as page_urls
from .product.urls import urlpatterns as product_urls
from .search.urls import urlpatterns as search_urls
from .shipping.urls import urlpatterns as shipping_urls
from .sites.urls import urlpatterns as site_urls
from .staff.urls import urlpatterns as staff_urls

urlpatterns = [
    re_path(r'^$', core_views.index, name='index'),
    re_path(r'^categories/', include(category_urls)),
    re_path(r'^collections/', include(collection_urls)),
    re_path(r'^orders/', include(order_urls)),
    re_path(r'^page/', include(page_urls)),
    re_path(r'^products/', include(product_urls)),
    re_path(r'^customers/', include(customer_urls)),
    re_path(r'^staff/', include(staff_urls)),
    re_path(r'^graphql/', GraphQLView.as_view(
        schema=schema, graphiql=settings.DEBUG), name='api'),
    re_path(r'^groups/', include(groups_urls)),
    re_path(r'^discounts/', include(discount_urls)),
    re_path(r'^settings/', include(site_urls)),
    re_path(r'^shipping/', include(shipping_urls)),
    re_path(r'^style-guide/', core_views.styleguide, name='styleguide'),
    re_path(r'^search/', include(search_urls)),
]
