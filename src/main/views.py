from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import ProductModel

# Create your views here.

class CatalogView(ListView):
    template_name = "catalog.html"
    queryset = ProductModel.objects.all()