from django.urls import path

from expiring_links.views import ExpiringLinkViewSet

expiring_link_create = ExpiringLinkViewSet.as_view({'post': 'create'})
expiring_link = ExpiringLinkViewSet.as_view({'get': 'retrieve'})
urlpatterns = [
    path('links/', expiring_link_create),
    path('links/<str:token>', expiring_link),
]
