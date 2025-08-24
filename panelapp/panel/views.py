from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from panel.models import Panel, Category

# Create your views here.
def index(request):
    context = {
        "panels": Panel.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "panel/index.html", context)

def panels(request):
    context = {
        "panels": Panel.objects.all(),
        "categories": Category.objects.all()
    }
    return render(request, "panel/panels.html", context)

def my_panels(request):
    if not request.user.is_authenticated:
        return redirect("home")
    context = {
        "panels": Panel.objects.filter(is_joined=True)
    }
    return render(request, "panel/my_panels.html", context)

def panel_details(request, slug):

    panel = Panel.objects.get(slug=slug)

    return render(request, "panel/panel_details.html", {"panel": panel})

def panels_by_category(request, slug):
    context = {
        #2.seçenek: "panels": Category.objects.get(slug=slug).panel_set.all(),
        "panels": Category.objects.get(slug=slug).panel_set.filter(is_active=True),
        #"panels": Panel.objects.filter(is_active=True, category__slug=slug),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "panel/panels.html", context)