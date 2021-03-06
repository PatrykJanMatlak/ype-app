"""ype URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from .views import CatalogView, ProductDetailView, productSearchView, CreateEvaluation


urlpatterns = [
    url(r'^search/$',productSearchView, name = "search"),
    url(r'^create/$',CreateEvaluation.as_view(), name = "create"),
    url(r'^(?P<slug>[\w-]+)/$',ProductDetailView.as_view(), name = "details"),
    url(r'$',CatalogView.as_view(), name = "list")

]
