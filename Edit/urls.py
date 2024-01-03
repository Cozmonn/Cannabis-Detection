from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("prof/", views.prof, name="prof")
]