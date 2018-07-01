from django.shortcuts import render

# Create your views here.


def About(request):
    template_name = "about.html"
    context = {

    }

    return render(request, template_name, context)