from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("Dashboard/", views.mainnDash, name="dash"),
    path("map1/", views.map1, name="map1"),
    path("map2/", views.map2, name="map2"),
    path("map3/", views.map3, name="map3")
]
