from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("Cannabis/", views.Cannabis, name="cannabisinfos"),
    path("About/", views.About, name="about")
]