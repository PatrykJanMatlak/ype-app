from django.conf.urls import url, include
from .views import ShopDetailView, ShopListView


urlpatterns = [

    url(r'^(?P<pk>\d+)',ShopDetailView.as_view(), name = "details"),
    url(r'$',ShopListView.as_view(), name = "list")

]
