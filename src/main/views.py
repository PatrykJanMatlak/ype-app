from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import ProductModel

# Create your views here.

class CatalogView(ListView):
    template_name = "catalog.html"
    queryset = ProductModel.objects.all()

class ProductDetailView(DetailView):
    template_name = "details.html"
    queryset = ProductModel.objects.all()
    
    # detailview takes slug wihout def. it.
   
    #   def get_object(self, *args , **kwargs):
    #     slug = self.kwargs.get('slug')
    #     obj = get_object_or_404(ProductModel, slug = slug)
    #     return obj
