from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("signin/", views.logform, name="login"),
    path("signup/", views.register_user, name="signup"),
    path("loout/", views.logoutt, name="logout"),
    path("Dashboard/", views.mainDash, name="dash"),
    path("edit/", views.edit_profile, name="edit")
]