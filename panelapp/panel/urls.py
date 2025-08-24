from django.urls import path
from . import views

# http://127.0.0.1:8000/              => homepage
# http://127.0.0.1:8000/index         => homepage
# http://127.0.0.1:8000/panels        => panels
# http://127.0.0.1:8000/panels/3      => panels-details
# http://127.0.0.1:8000/my_panels     => my_panels

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("panels", views.panels, name="panels"),
    path("category/<slug:slug>", views.panels_by_category, name="panels_by_category"),
    path("panels/<slug:slug>", views.panel_details, name="panel_details"),
    path("my_panels", views.my_panels, name="my_panels"),
]