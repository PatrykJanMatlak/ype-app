from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from .models import ShopModel
# Create your views here.

class ShopListView(ListView):
    template_name="shop_list.html"
    queryset = ShopModel.objects.all()


class ShopDetailView(DetailView):
    template_name="shop_detail.html"
    queryset = ShopModel.objects.all()


class ShopCreateView(CreateView):
    pass