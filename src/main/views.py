from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView, FormView
from .models import ProductModel
from .forms import SearchForm, CreateEvaluationForm
from django.db.models import Q
from shops.models import ShopModel

# Create your views here.

class CatalogView(ListView):
    template_name = "catalog.html"
    queryset = ProductModel.objects.all()

class ProductDetailView(DetailView):
    template_name = "details.html"
    queryset = ProductModel.objects.all()
    
    # detailview takes slug wihout def. it. (autom.)
   
    #   def get_object(self, *args , **kwargs):
    #     slug = self.kwargs.get('slug')
    #     obj = get_object_or_404(ProductModel, slug = slug)
    #     return obj



def productSearchView(request):

    template_name = "search.html"
    form = SearchForm(request.POST)
    search = None
    
    search = request.POST.get('search')
    
    if form.errors:
        print (form.errors)
        errors = form.errors
        context = {}
    
    if search != None:
        queryset = ProductModel.objects.filter(Q(name__icontains = search) | Q(name__icontains = search))
        queryset2 = ShopModel.objects.filter(Q(name__icontains = search) | Q(name__icontains = search))
        context = {'queryset' : queryset, 'queryset2' : queryset2}

    else:
        context = {}

    return render(request, template_name, context)

class CreateEvaluation(CreateView):
    template_name = "create.html"
    model = ProductModel
    fields = ['name','price','category','mark','evaluation']